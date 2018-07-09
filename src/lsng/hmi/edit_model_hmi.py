'''
Created on 10 avr. 2018

@author: Djer
'''

from PyQt5.QtWidgets import QDialog, QMessageBox

from src.lsng.hmi.edit_model.edit_model_ui import Ui_edit_model
from src.lsng.database.models import DeviceType


class AddModel(QDialog):
    '''
    classdocs
    '''

    def __init__(self, supplier, parent=None):
        '''
        Constructor
        '''
        super(AddModel, self).__init__(parent)
        self.supplier = supplier
        self.model_values = None
        self.uic = Ui_edit_model()
        self.uic.setupUi(self)
        
        self.name = None
        self.code = None
        self.base_tac_number = None
        self.sim_number = None
        self.wifi = None
        self.bt = None
        self.device_type = None

        self.uic.lbl_supplier.setText(self.supplier)

        self.uic.btn_save.clicked.connect(self.create_model)
        self.uic.btn_cancel.clicked.connect(self.quitLogin)

    def create_model(self):
        if self.uic.cb_wifi.currentText() == "Yes":
            wifi = True
        else:
            wifi = False

        if self.uic.cb_bt.currentText() == "Yes":
            bt = True
        else:
            bt = False

        for item in list(DeviceType):
            if item.name == self.uic.cb_type.currentText():
                device_type = item.value
                break

        if not self.uic.txt_name.text():
            QMessageBox.warning(self, 'Error', 'Please enter a name !')
            return
        
        if self.uic.sp_sim.value() > 0:
            if not self.uic.sp_tac_code.value() or (len(str(self.uic.sp_tac_code.value())) != 8 ):
                QMessageBox.warning(self, 'Error', 'Please enter a valid TAC number !')
                return

        self.name = self.uic.txt_name.text()
        self.code = self.uic.sp_code.value()
        self.base_tac_number = self.uic.sp_tac_code.value()
        self.sim_number = self.uic.sp_sim.value()
        self.wifi = wifi
        self.bt = bt
        self.device_type = device_type
            
        self.accept()

    def quitLogin(self):
        self.close()
