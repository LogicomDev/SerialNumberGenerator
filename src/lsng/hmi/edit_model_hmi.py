'''
Created on 10 avr. 2018

@author: Djer
'''

from PyQt5.QtWidgets import QDialog
from hmi.edit_model import Ui_edit_model
from database.models import Device, DeviceType


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

        self.model_values = Device(self.uic.txt_name.text(), self.uic.sp_code.value(), self.uic.sp_tac_code.value(), self.uic.sp_sim.value(), wifi, bt, device_type)
        self.accept()

    def quitLogin(self):
        exit(0)
