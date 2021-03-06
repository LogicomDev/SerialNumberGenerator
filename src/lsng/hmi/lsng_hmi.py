# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QTreeWidgetItem, QShortcut, QDialog)
from PyQt5.QtGui import QKeySequence, QValidator
from PyQt5.QtCore import pyqtSlot, Qt
# from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog,
#                              QTreeWidgetItem, QInputDialog, QMessageBox, QDialog,
#                              QLineEdit, QPushButton, QVBoxLayout, QErrorMessage,
#                              QSplashScreen, QShortcut)
# from PyQt5.QtGui import QMovie, QPixmap, QPainter, QKeySequence
# from PyQt5.QtCore import QObject, pyqtSignal, QFile, QFileInfo, QSettings, Qt, QTextStream, pyqtSlot
    
import logging
# from logging.handlers import RotatingFileHandler
from enum import Enum
import os

# Windows imports
from src.lsng.hmi.main_window import main_windows_ui as main_ui
from src.lsng.hmi.edit_model_hmi import AddModel
from src.lsng.hmi.edit_supplier_hmi import AddSupplier

# File imports
from src.lsng.database.models import (Database, GenerationRunBasic)
from src.lsng.log.log_manager import (LogManager, DEBUG, INFO, OK, WARNING, KO, ERROR, CRITICAL)
from src.lsng.export.export import Exporter
from src.lsng.generation.generation_handler import (GenerationHandler, NoMoreMACAdressAvailable, NoMoreIMEIAdressAvailable, NoMoreSerialAvailable)

__version__ = "3.4"

# This is SPARTA ! (or our logger... your call !)
lsng_logger = None


class UserRight(Enum):
    Admin = 0
    Manager = 1
    Tester = 2
    Quality = 3

    
# Below are our decorators
def singleton(cls):
    instance = None

    def ctor(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return ctor


# Below are our classes
class UppercaseValidator(QValidator):
    """
    This is a Validator designed to handle the color input and make sure it's always uppercase
    """

    def validate(self, string, pos):
        return QValidator.Acceptable, string.upper(), pos
    

class LogicomSerialGenerator(QMainWindow):
    """
        This is the main Class
    """

    def __init__(self, db_handler, user, logger):
        QMainWindow.__init__(self)
        self.logger = logger
        self.uic = main_ui.Ui_MainWindow()
        self.uic.setupUi(self)

        # Basic objects attributes
        self.basefolder = os.getcwd()
#         self.generations = []
        self.let_user_generate = True

        # Complex attributes
        self.current_generation = None
        self.no_change = False
        self.log = LogManager(self, self.logger)
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
        self.log.add_trace("Please select a supplier and a model before starting", INFO)
        self.uic.lbl_pool_unsaved.setText("Waiting for a generation ... :(")
        self.generation_infos_visibility(False)
        self.hide_creation_button()

        self.connection()
        
        self.uppercase_validator = UppercaseValidator(self)
        self.uic.txt_color.setValidator(self.uppercase_validator)
        # self.showMaximized()

    def hide_creation_button(self):
        if self.user.level <= UserRight.Manager.value:
            self.uic.btn_add_device.setHidden(False)
            self.uic.btn_add_supplier.setHidden(False)
        else:
            self.uic.btn_add_device.setHidden(True)
            self.uic.btn_add_supplier.setHidden(True)

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

#         self.uic.tree_devices.itemSelectionChanged.connect(self.release_generation_button)
#         self.uic.txt_po_number.textChanged.connect(self.release_generation_button)
#         self.uic.txt_color.textChanged.connect(self.release_generation_button)
#         self.uic.sp_week.valueChanged.connect(self.release_generation_button)
#         self.uic.sp_year.valueChanged.connect(self.release_generation_button)
#         self.uic.sp_qty.valueChanged.connect(self.release_generation_button)

        # Shortcuts connection
        QShortcut(QKeySequence("Ctrl+q"), self, self.close)

    def load_user(self):
        '''
        Displays a nice "f_name l_name (login) - (level)" prompt at the top of screen
        '''
        self.uic.txt_user.setText("{} {} ({}) - {}".format(
            self.user.first_name,
            self.user.last_name,
            self.user.login,
            UserRight(self.user.level).name)
        )
        # This ensure the ID of current user is correct (at the cost of another SQL request)
        self.user.id = self.sql_db.get_user_id(self.user.login)[0]

    def add_supplier(self):
        supplier = AddSupplier(self)
        # supplier.setWindowFlags(Qt.CustomizeWindowHint)
        if supplier.exec_() == QDialog.Accepted and supplier.name:
            self.sql_db.add_supplier(supplier, self.user)
            self.load_database()
            self.populate_treeview()
            self.log.add_trace("Supplier successfully added !", OK)
        else:
            self.log.add_trace("Supplier creation canceled")

    def add_device(self):
        '''
        Calls Remove windows
        '''
        item_name = self.uic.tree_devices.currentItem()
        
        if not item_name:
            self.log.add_trace("Please select a supplier first in order to add a device to the database", WARNING)
            return
        supplier = self.db.get_supplier(item_name.text(0))
        if not supplier:
            # We have selected a device
            supplier_name = self.uic.tree_devices.currentItem().parent().text(0)
            supplier = self.db.get_supplier(supplier_name)
            self.log.add_trace("Please select a supplier first in order to add a device to the database", WARNING)
            return
        else:
            supplier_name = supplier.name
        
        # We have selected a supplier
        device = AddModel(supplier_name)
        device.setWindowFlags(Qt.CustomizeWindowHint)
        if device.exec_() == QDialog.Accepted and device.name:
            self.sql_db.add_device(device, supplier, self.user)
            self.load_database()
            self.populate_treeview()
            self.log.add_trace("Device successfully added !", OK)
        else:
            self.log.add_trace("Device creation canceled")

    def edit_item(self):
        '''
        Calls Edit windows
        '''
        self.log.add_trace("Edit Item", logging.INFO)

    def load_database(self):
        '''
        Creates SQL tables (if not existing) and read them
        '''
        self.sql = None

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
                self.log.add_trace("Can't find supplier : {}".format(update[1:]), ERROR)
            self.uic.btn_generate.setEnabled(False)

    def populate_treeview(self):
        self.uic.tree_devices.clear()
        for supplier, infos in self.db.get_suppliers().items():
            supplier_item = QTreeWidgetItem(self.uic.tree_devices, [supplier])
            for model in infos.devices:
                QTreeWidgetItem(supplier_item, [model])
        self.uic.tree_devices.sortItems(0, Qt.SortOrder(0))

    def generation_infos_visibility(self, state=True):
#         self.uic.prg_generation.setHidden(not state)
        self.uic.lbl_pool_unsaved.setHidden(not state)
        self.uic.btn_save.setHidden(not state)
        self.let_user_generate = not state

    def set_generation_info_enabled(self, state):
        self.uic.sp_mac_left.setEnabled(state)
        self.uic.sp_imei_left.setEnabled(state)
        self.uic.tree_devices.setEnabled(state)
        self.uic.txt_po_number.setEnabled(state)
        self.uic.txt_color.setEnabled(state)
        self.uic.sp_week.setEnabled(state)
        self.uic.sp_year.setEnabled(state)
        self.uic.sp_qty.setEnabled(state)
        self.uic.btn_add_device.setEnabled(state)
        self.uic.btn_add_supplier.setEnabled(state)  
    
    def release_generation_button(self):
        self.uic.btn_generate.setEnabled(True)

    def generation_start(self):
        # if self.uic.txt_po_number.text() and self.uic.txt_color.text() and self.uic.sp_qty.value() and self.device:
        if self.let_user_generate:
            # Start subsidiary Thread
            try:
                self.generator.load_values(self.supplier, self.device, self.uic.txt_po_number.text(),
                                           self.uic.txt_color.text(), self.uic.sp_week.value(),
                                           self.uic.sp_year.value(), self.uic.sp_qty.value())
                
                self.uic.btn_generate.setEnabled(False)
                self.generation_infos_visibility(True)
                self.set_generation_info_enabled(False)
                self.uic.prg_generation.setMinimum(0)
                self.uic.prg_generation.setMaximum(self.uic.sp_qty.value())
                self.uic.prg_generation.setValue(0)
                self.log.add_trace("Generation started", INFO)
                QApplication.setOverrideCursor(Qt.WaitCursor)
            
                self.generator.start()
            except NoMoreMACAdressAvailable:
                QApplication.restoreOverrideCursor()
                self.log.add_trace("Not enough MAC address available : Please update MAC attribution table", WARNING)
            except NoMoreIMEIAdressAvailable:
                QApplication.restoreOverrideCursor()
                self.log.add_trace("Not enough IMEI address available : Please get a new TAC code for your device", WARNING)
            except Exception as ex:
                # Catch all other stuff !
                self.log.add_trace(str(ex), CRITICAL)
        else:
            self.log.add_trace("Please make sure to fill every field before running a generation ;)", ERROR)

    def generation_finished(self):
        QApplication.restoreOverrideCursor()
        self.uic.lbl_pool_unsaved.setText("Please save your generation")
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
            if self.supplier.get_mac_address_left() == 0 or self.supplier.get_mac_address_left() > 223696:
                self.log.add_trace("This supplier has no more MAC adresses available or a wrong MAC range. Please provide a new MAC range.", WARNING)
            self.uic.btn_generate.setEnabled(True)

    def save_and_export(self):
        # for raw_generation in self.generations:
        raw_generation = self.generator.get_results()
        generation = GenerationRunBasic(raw_generation.get("supplier"),
                                        raw_generation.get("device"),
                                        raw_generation.get("po_number"),
                                        raw_generation.get("color"),
                                        raw_generation.get("prod_week"),
                                        raw_generation.get("prod_year") if len(str(raw_generation.get("prod_year"))) == 2 else str(raw_generation.get("prod_year"))[2:],
                                        raw_generation.get("qty"))
        generation.generated_values = raw_generation.get("values")

        try:
            self.save_generation_summary(generation)
            self.create_generation_reports(generation)
        except:
            self.log.add_trace("Error")
            # Must do a rollback on Database
#             self.sql_db.rollback()

        item_index = self.uic.tree_devices.currentItem()
        
        # Clears the generation buffer
        self.generation_infos_visibility(False)
        self.set_generation_info_enabled(True)
        self.load_database()
        
        self.release_generation_button()
        self.uic.tree_devices.setCurrentItem(item_index)
        self.uic.prg_generation.setValue(0)
        self.update_selected_item()

    def save_generation_summary(self, generation):
        '''
        Save the generation summary to the SQL database
        '''
        self.log.add_trace("Saving generation summary for {}-{}-{}".format(generation.po_number, generation.color, generation.qty))
        self.sql_db.add_generation(generation, self.user)
        self.log.add_trace("Saving successful")

    def create_generation_reports(self, generation):
        if self.uic.chk_seperator.isChecked():
            mac_seperator = "-"
        else:
            mac_seperator = ":"
        self.log.add_trace("Creating CSV generation report for {}-{}-{}".format(generation.po_number, generation.color, generation.qty))
        path = self.exporter.export_generation(generation, mac_seperator)
        self.log.add_trace("Creation of generation report successful")
        self.log.add_trace("File path is : {}".format(path))

    def add_error_trace(self, msg):
        '''
        Something went wrong, so this method returns the program to a useable state
        '''
        self.log.add_trace_with_box(msg, CRITICAL)
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
