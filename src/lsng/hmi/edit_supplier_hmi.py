'''
Created on 10 avr. 2018

@author: Djer
'''

from PyQt5.QtWidgets import QDialog
from hmi.edit_supplier import Ui_edit_supplier
from database.models import Supplier


class AddSupplier(QDialog):
    '''
    classdocs
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(AddSupplier, self).__init__(parent)
        self.supplier_values = None
        self.uic = Ui_edit_supplier()
        self.uic.setupUi(self)

        self.uic.btn_save.clicked.connect(self.create_supplier)
        self.uic.btn_cancel.clicked.connect(self.quitLogin)

    def create_supplier(self):
        self.supplier_values = Supplier(self.uic.txt_name.text(), self.uic.sp_code.value(), self.uic.txt_first_mac.text(), self.uic.txt_last_mac.text())
        self.accept()

    def quitLogin(self):
        exit(0)
