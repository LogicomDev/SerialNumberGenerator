'''
Created on 6 avr. 2018

@author: Djer
'''

from PyQt5.QtWidgets import QMessageBox, QDialog

from src.lsng.hmi.login import user_logging_ui as user_logging
from src.lsng.database.models import User


class Login(QDialog):

    def __init__(self, db_handler, parent=None):
        super(Login, self).__init__(parent)

        self.db = db_handler
        self.user = None
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
