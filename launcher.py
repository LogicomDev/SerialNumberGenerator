# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog,
                             QTreeWidgetItem, QInputDialog, QMessageBox, QDialog,
                             QLineEdit, QPushButton, QVBoxLayout
                             )
from PyQt5.QtCore import QObject, pyqtSignal, QFile, QFileInfo, QSettings, Qt, QTextStream

import json
from netaddr import EUI, AddrFormatError
import os
import itertools
import logging
import time
from enum import Enum

# Windows imports
import main_windows_ui as main_ui
import user_logging as user_logging

# File imports
from src.lsng.database.models import Database
from src.lsng.database.sql_handler import SQLHandler
from src.lsng.database.models import *

__version__ = "3.0b"


class UserRight(Enum):
    Admin = 0
    Manager = 1
    Tester = 2


class NoMoreMACAdressAvailable(Exception):
    pass


class NoMoreIMEIAdressAvailable(Exception):
    pass


class Login(QDialog):

    def __init__(self, db_handler, parent=None):
        super(Login, self).__init__(parent)

        self.db = db_handler
        self.user = ()
        self.uic = user_logging.Ui_user_logging()
        self.uic.setupUi(self)

        self.uic.btn_login.clicked.connect(self.handleLogin)
        self.uic.btn_exit.clicked.connect(self.quitLogin)

    def handleLogin(self):
        user_data = self.db.is_valid_user(self.uic.txt_login.text(), self.uic.txt_password.text())
        if user_data:
            self.user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[5])
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Bad user or password')

    def quitLogin(self):
        exit(0)


class StdErrHandler(QObject):
    '''
    This class provides an alternate write() method for stderr messages.
    Messages are sent by pyqtSignal to the pyqtSlot in the main window.
    '''
    err_msg = pyqtSignal(str)

    def __init__(self, parent=None):
        QObject.__init__(self)

    def write(self, msg):
        # stderr messages are sent to this method.
        self.err_msg.emit(msg)


class LogicomSerialGenerator(QMainWindow):
    """
        This is the main Class
    """

    def __init__(self, db_handler, user):
        QMainWindow.__init__(self)
        self.showMaximized()
        self.uic = main_ui.Ui_MainWindow()
        self.uic.setupUi(self)
        self.connection()

        self.sql_db = db_handler
        self.user = user
        self.supplier = None
        self.device = None
        self.db = Database()

        self.load_user()
        self.load_database()
        self.populate_treeview()

        self.setWindowTitle("Logicom Serial Generator - v." + __version__)
        self.log_info("Welcome to the LOGICOM Serial Generator Tool")
        self.log_info("Please select a supplier and a model before starting", logging.WARNING)
        self.uic.prg_generation.setHidden(True)

    def connection(self):
        self.uic.btn_generate.clicked.connect(self.generation_start)
        self.uic.btn_add.clicked.connect(self.add_item_to_list)
        self.uic.btn_remove.clicked.connect(self.remove_item_from_list)
        self.uic.btn_edit.clicked.connect(self.edit_item)
        self.uic.tree_devices.itemSelectionChanged.connect(self.update_selected_item)

    def log_info(self, message, level=logging.DEBUG):
        if level == logging.DEBUG:
            message_html = "<span style=\" color:black;\">{}</span>".format(message)
        elif level == logging.CRITICAL:
            message_html = "<span style=\" color:red;\">{}</span>".format(message)
        elif level == logging.WARNING:
            message_html = "<span style=\" color:purple;\">{}</span>".format(message)
        elif level == logging.ERROR:
            message_html = "<span style=\" color:orange;\">{}</span>".format(message)
        elif level == logging.INFO:
            message_html = "<span style=\" color:green;\">{}</span>".format(message)

        self.uic.txt_log.append(message_html)
        self.uic.txt_log.verticalScrollBar().setValue(self.uic.txt_log.maximumHeight())

    def load_user(self):
        '''
        Displays a nice "f_name l_name (login) - (level)" prompt at the top of screen
        '''
        self.uic.txt_user.setText("{} {} ({}) - {}".format(self.user.first_name,
                                                           self.user.last_name,
                                                           self.user.login,
                                                           UserRight(self.user.level).name)
                                  )

    def add_item_to_list(self):
        self.log_info("Adding Item", logging.ERROR)
        # User select if he wants a Device or a     

    def remove_item_from_list(self):
        self.log_info("Removing Item", logging.CRITICAL)

    def edit_item(self):
        self.log_info("Edit Item", logging.INFO)

    def load_database(self):
        '''
        Creates SQL tables (if not existing) and read them
        '''
        self.sql_db.create_table()

        suppliers = self.sql_db.read_suppliers()
        for supplier in suppliers:
            db_sup = self.db.add_supplier(supplier[1], supplier[2], supplier[3], supplier[4], supplier[0])

        devices = self.sql_db.read_devices()
        for device in devices:
            db_sup = self.db.get_supplier_by_id(device[8])
            db_sup.add_device(device[1], device[2], device[4], device[3], device[5], device[6], device[7], device[0])

    def populate_treeview(self):
        self.uic.tree_devices.clear()
        for supplier, infos in self.db.get_suppliers().items():
            supplier_item = QTreeWidgetItem(self.uic.tree_devices, [supplier])
            for model in infos.devices:
                QTreeWidgetItem(supplier_item, [model])

    def generation_start(self):        
        if self.uic.txt_po_number.text() and self.uic.txt_color.text() and self.uic.sp_qty.value():
            self.uic.prg_generation.setHidden(False)
            self.log_info("Generation started", logging.INFO)
            QApplication.setOverrideCursor(Qt.WaitCursor)
            
            # Start subsidiary Thread
            run = GenerationRun(self.supplier, self.device, self.uic.txt_po_number.text(),
                            self.uic.txt_color.text(), self.uic.sp_week.value(),
                            self.uic.sp_year.value(), self.uic.sp_qty.value())
            try:
                run.generate()
                time.sleep(2)
                data = run.get_results()
                for result in data:
                    self.log_info(result)
                # Returns from subsidiary Thread
                self.generation_finished()
                
            except NoMoreMACAdressAvailable:
                self.log_info("No more MAC adress available : Please update MAC datas and MAC attribution table", logging.CRITICAL)
            except NoMoreIMEIAdressAvailable:
                self.log_info("No more IMEI adress available : Please get a new IMEI for your device", logging.CRITICAL)
        else:
            self.log_info("Please make sure to fill every field before running a generation ;)", logging.ERROR)

    def generation_finished(self):
        QApplication.restoreOverrideCursor()
        self.log_info("Generation finished", logging.INFO)

    def update_selected_item(self):
        item_name = self.uic.tree_devices.currentItem().text(0)
        if self.db.get_device(item_name):
            # Only update data if you select a device
            supplier_name = self.uic.tree_devices.currentItem().parent().text(0)
            device_name = self.uic.tree_devices.currentItem().text(0)
            self.log_info("Selecting device {} from supplier {}".format(device_name, supplier_name))
            self.supplier = self.db.get_supplier(supplier_name)
            self.device = self.db.get_device(device_name)
            self.uic.sp_supplier.setValue(self.supplier.code)
            self.uic.sp_model.setValue(self.device.code)
            self.uic.sp_mac_left.setValue(self.supplier.get_mac_address_left())
            if self.supplier.get_mac_address_left() == 0 or self.supplier.get_mac_address_left() > 200001:
                self.log_info("This supplier has no more MAC adresses available or a wrong MAC range. Please provide a new MAC range.", logging.CRITICAL)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    db_handler = SQLHandler(r"src\lsng\database\logicom_database.db")

    #db_handler.add_user("Jeremy", "Marchal", "Admin", "Logicom", 0)

    login = Login(db_handler)

    if login.exec_() == QDialog.Accepted:
        frame = LogicomSerialGenerator(db_handler, login.user)
        frame.show()
    #     # Create the stderr handler and point stderr to it
    #     std_err_handler = StdErrHandler()
    #     sys.stderr = std_err_handler
    #
    #     # Connect err_msg signal to message box method in main window
    #     std_err_handler.err_msg.connect(frame.std_err_post)

        sys.exit(app.exec_())
