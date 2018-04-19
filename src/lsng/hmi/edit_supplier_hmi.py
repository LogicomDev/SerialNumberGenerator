'''
Created on 10 avr. 2018

@author: Djer
'''

from PyQt5.QtWidgets import QDialog, QMessageBox
from hmi.edit_supplier.edit_supplier_ui import Ui_edit_supplier

import re

class AddSupplier(QDialog):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(AddSupplier, self).__init__(parent)
        self.name = ""
        self.code = 0
        self.mac_min = ""
        self.mac_max = ""
        self.uic = Ui_edit_supplier()
        self.uic.setupUi(self)

        self.uic.btn_save.clicked.connect(self.create_supplier)
        self.uic.btn_cancel.clicked.connect(self.quitLogin)

    def create_supplier(self):
        if not self.uic.txt_name :
            QMessageBox.warning(self, 'Error', 'Please enter a name !')
            return
        
        if self.uic.txt_first_mac.text() == self.uic.txt_last_mac.text():
            QMessageBox.warning(self, 'Error', 'Please enter a valid MAC range !')
            return
        
        if not self.uic.txt_first_mac.text() or not self.uic.txt_last_mac.text():
            QMessageBox.warning(self, 'Error', 'Please enter a valid MAC range !')
            return
        
        mac_pattern = re.compile("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")
        
        if mac_pattern.match(self.uic.txt_first_mac.text()) and mac_pattern.match(self.uic.txt_last_mac.text()):
            self.name = self.uic.txt_name.text()
            self.code = self.uic.sp_code.value()
            self.mac_min = self.uic.txt_first_mac.text()
            self.mac_max = self.uic.txt_last_mac.text()
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Please enter a MAC with valid format !')
            return

    def quitLogin(self):
        self.close()
