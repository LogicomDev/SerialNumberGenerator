# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QTreeWidgetItem, QShortcut, QDialog)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import pyqtSlot, Qt
# from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog,
#                              QTreeWidgetItem, QInputDialog, QMessageBox, QDialog,
#                              QLineEdit, QPushButton, QVBoxLayout, QErrorMessage,
#                              QSplashScreen, QShortcut)
# from PyQt5.QtGui import QMovie, QPixmap, QPainter, QKeySequence
# from PyQt5.QtCore import QObject, pyqtSignal, QFile, QFileInfo, QSettings, Qt, QTextStream, pyqtSlot

import logging
from enum import Enum
import os

# Windows imports
from hmi.main_window import main_windows_ui as main_ui
from hmi.edit_model_hmi import AddModel
from hmi.edit_supplier_hmi import AddSupplier

# File imports
from database.models import Database, GenerationRunBasic
from log.log_manager import LogManager
from export.export import Exporter
from generation.generation_handler import GenerationHandler

__version__ = "3.0b"


class UserRight(Enum):
    Admin = 0
    Manager = 1
    Tester = 2


class NoMoreMACAdressAvailable(Exception):
    pass


class NoMoreIMEIAdressAvailable(Exception):
    pass


class LogicomSerialGenerator(QMainWindow):
    """
        This is the main Class
    """

    def __init__(self, db_handler, user):
        QMainWindow.__init__(self)
        self.uic = main_ui.Ui_MainWindow()
        self.uic.setupUi(self)

        # Basic objects attributes
        self.basefolder = os.getcwd()
        self.generations = []

        # Complex attributes
        self.current_generation = None
        self.no_change = False
        self.log = LogManager(self)
        self.generator = GenerationHandler(self)
        self.exporter = Exporter("csv", self)  # CSV is default export type
        self.sql_db = db_handler
        self.user = user
        self.supplier = None
        self.device = None
        self.db = Database()

        self.load_user()
        self.load_database()
        self.populate_treeview()

        self.setWindowTitle("Logicom Serial Generator - v." + __version__)
        self.log.add_trace("Welcome to the LOGICOM Serial Generator Tool")
        self.log.add_trace("Please select a supplier and a model before starting", logging.WARNING)
        self.uic.lbl_pool_unsaved.setText("{} generations not saved".format(len(self.generations)))
        self.generation_infos_visibility(False)

        self.connection()
        # self.showMaximized()

    def connection(self):
        self.uic.btn_generate.clicked.connect(self.generation_start)
        self.uic.btn_add_supplier.clicked.connect(self.add_supplier)
        self.uic.btn_add_device.clicked.connect(self.add_device)
        self.uic.tree_devices.itemSelectionChanged.connect(self.update_selected_item)
        self.uic.btn_save.clicked.connect(self.save_and_export)

        # Custom slots/signals
        self.generator.event_trace.connect(self.log.add_trace)
        self.generator.session_finished.connect(self.generation_finished)
        self.generator.session_progression.connect(self.update_progbar)
        self.generator.event_errors.connect(self.add_error_trace)

        self.uic.tree_devices.itemSelectionChanged.connect(self.release_generation_button)
        self.uic.txt_po_number.textChanged.connect(self.release_generation_button)
        self.uic.txt_color.textChanged.connect(self.release_generation_button)
        self.uic.sp_week.valueChanged.connect(self.release_generation_button)
        self.uic.sp_year.valueChanged.connect(self.release_generation_button)
        self.uic.sp_qty.valueChanged.connect(self.release_generation_button)

        # Shortcuts connection
        QShortcut(QKeySequence("Ctrl+q"), self, self.close)

    def load_user(self):
        '''
        Displays a nice "f_name l_name (login) - (level)" prompt at the top of screen
        '''
        self.uic.txt_user.setText("{} {} ({}) - {}".format(self.user.first_name,
                                                           self.user.last_name,
                                                           self.user.login,
                                                           UserRight(self.user.level).name)
        )
        # This ensure the ID of current user is correct (at the cost of another SQL request)
        self.user.id = self.sql_db.get_user_id(self.user.login)[0]

    def add_supplier(self):
        supplier = AddSupplier(self)
        if supplier.exec_() == QDialog.Accepted:
            # self.db.add_supplier()
            # self.sql_db.add_supplier(supplier, self.user)
            print("Add supplier")
            self.populate_treeview()

    def add_device(self):
        '''
        Calls Remove windows
        '''
        device = AddModel(self)
        if device.exec_() == QDialog.Accepted:
            # supplier.add_device()
            # self.sql_db.add_device(device, self.user)
            print("Add device")
            self.populate_treeview()

    def edit_item(self):
        '''
        Calls Edit windows
        '''
        self.log.add_trace("Edit Item", logging.INFO)

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
            db_sup.add_device(device[1], device[2], device[4], device[5], device[6], device[7], device[3], device[0])

        updates = self.sql_db.read_generations_summary()
        for update in updates:
            if update[1] is None:
                continue
            db_dev = self.db.get_device_by_id(update[1])
            sup_id = self.sql_db.get_device_by_id(update[1])
            if sup_id:
                db_sup = self.db.get_supplier_by_id(sup_id[-2])
                db_sup.add_generation(update[1:])
                db_dev.add_generation(update[1:])
            else:
                self.log.add_trace("Can't find supplier : {}".format(update[1:]), logging.ERROR)

    def populate_treeview(self):
        self.uic.tree_devices.clear()
        for supplier, infos in self.db.get_suppliers().items():
            supplier_item = QTreeWidgetItem(self.uic.tree_devices, [supplier])
            for model in infos.devices:
                QTreeWidgetItem(supplier_item, [model])

    def generation_infos_visibility(self, state=True):
        self.uic.prg_generation.setHidden(not state)
        self.uic.lbl_info_pool_unsaved.setHidden(not state)
        self.uic.lbl_pool_unsaved.setHidden(not state)
        self.uic.btn_save.setHidden(not state)

    def release_generation_button(self):
        self.uic.btn_generate.setEnabled(True)

    def generation_start(self):
        if self.uic.txt_po_number.text() and self.uic.txt_color.text() and self.uic.sp_qty.value() and self.device:
            self.uic.btn_generate.setEnabled(False)
            self.generation_infos_visibility(True)
            self.uic.prg_generation.setMinimum(0)
            self.uic.prg_generation.setMaximum(self.uic.sp_qty.value())
            self.uic.prg_generation.setValue(0)
            self.log.add_trace("Generation started", logging.INFO)
            QApplication.setOverrideCursor(Qt.WaitCursor)
            # Start subsidiary Thread
            try:
                self.generator.load_values(self.supplier, self.device, self.uic.txt_po_number.text(),
                                           self.uic.txt_color.text(), self.uic.sp_week.value(),
                                           self.uic.sp_year.value(), self.uic.sp_qty.value())
                self.generator.start()
            except NoMoreMACAdressAvailable:
                self.log.add_trace("No more MAC adress available : Please update MAC datas and MAC attribution table", logging.CRITICAL)
            except NoMoreIMEIAdressAvailable:
                self.log.add_trace("No more IMEI adress available : Please get a new IMEI for your device", logging.CRITICAL)
            except Exception as ex:
                # Catch all other stuff !
                self.log.add_trace(ex, logging.CRITICAL)
        else:
            self.log.add_trace("Please make sure to fill every field before running a generation ;)", logging.ERROR)

    def generation_finished(self):
        QApplication.restoreOverrideCursor()
        # saves the results
        self.generations.append(self.generator.get_results())

        self.uic.lbl_pool_unsaved.setText("{} generations not saved".format(len(self.generations)))
        self.log.add_trace_with_box("Generation have successfully ended ! :)")

    @pyqtSlot(int)
    def update_progbar(self, value):
        self.uic.prg_generation.setValue(value)

    def update_selected_item(self):
        item_name = self.uic.tree_devices.currentItem().text(0)
        if self.db.get_device(item_name):
            # Only update data if you select a device
            supplier_name = self.uic.tree_devices.currentItem().parent().text(0)
            device_name = self.uic.tree_devices.currentItem().text(0)
            self.log.add_trace("Selecting device {} from supplier {}".format(device_name, supplier_name))
            self.supplier = self.db.get_supplier(supplier_name)
            self.device = self.db.get_device(device_name)
            self.uic.txt_supplier.setText("{:02}".format(self.supplier.code))
            self.uic.txt_model.setText("{:02}".format(self.device.code))
            self.uic.sp_mac_left.setValue(self.supplier.get_mac_address_left())
            self.uic.sp_imei_left.setValue(self.device.get_imei_left())
            if self.supplier.get_mac_address_left() == 0 or self.supplier.get_mac_address_left() > 200001:
                self.log.add_trace("This supplier has no more MAC adresses available or a wrong MAC range. Please provide a new MAC range.", logging.CRITICAL)

    def save_and_export(self):        
        for raw_generation in self.generations:
            generation = GenerationRunBasic(raw_generation.get("supplier"),
                                            raw_generation.get("device"),
                                            raw_generation.get("po_number"),
                                            raw_generation.get("color"),
                                            raw_generation.get("prod_week"),
                                            raw_generation.get("prod_year") if len(str(raw_generation.get("prod_year"))) == 2 else str(raw_generation.get("prod_year"))[2:],
                                            raw_generation.get("qty"))
            generation.generated_values = raw_generation.get("values")
            
            self.save_generation(generation)
            self.create_generation_reports(generation)
            self.load_database()

        # Clears the generation buffer
        self.generations = []
        self.generation_infos_visibility(False)

    def save_generation(self, generation):
        '''
        Save the generation results to the SQL database
        '''
        self.log.add_trace("Saving generation for {}-{}-{}".format(generation.po_number, generation.color, generation.qty))
        self.sql_db.add_generation(generation, self.user)
        self.log.add_trace("Saving successful")

    def create_generation_reports(self, generation):
        self.log.add_trace("Creating CSV generation report for {}-{}-{}".format(generation.po_number, generation.color, generation.qty))
        path = self.exporter.export_generation(generation)
        self.log.add_trace("Creation of generation report successful.")
        self.log.add_trace("File path is : {}".format(path))
    
    def add_error_trace(self, msg):
        '''
        Something went wrong, so this method returns the program to a useable state
        '''
        self.log.add_trace_with_box(msg, logging.CRITICAL)
        QApplication.restoreOverrideCursor()
        self.generation_infos_visibility(False)
        self.uic.btn_generate.setEnabled(True)

    ###################################################################################
    #                Standardized callbacks
    ###################################################################################
    def closeEvent(self, event):
        """
            Callback on application closing
        """
        quit_window = self.log.add_trace_with_question_box("Leaving so soon", "Are you sure you want to quit ? :(")
        if quit_window:
            self.close()
        else:
            event.ignore()
