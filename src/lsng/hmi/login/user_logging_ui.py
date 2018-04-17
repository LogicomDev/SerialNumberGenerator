# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\J_MARCHAL\eclipse-workspace\lsng\src\lsng\hmi\login\user_logging_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_user_logging(object):
    def setupUi(self, user_logging):
        user_logging.setObjectName("user_logging")
        user_logging.resize(481, 150)
        user_logging.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.gridLayoutWidget = QtWidgets.QWidget(user_logging)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 461, 64))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_login = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_login.sizePolicy().hasHeightForWidth())
        self.lbl_login.setSizePolicy(sizePolicy)
        self.lbl_login.setObjectName("lbl_login")
        self.gridLayout.addWidget(self.lbl_login, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.txt_password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.gridLayout.addWidget(self.txt_password, 2, 1, 1, 1)
        self.lbl_password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_password.setObjectName("lbl_password")
        self.gridLayout.addWidget(self.lbl_password, 2, 0, 1, 1)
        self.txt_login = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_login.setObjectName("txt_login")
        self.gridLayout.addWidget(self.txt_login, 0, 1, 1, 1)
        self.lbl_title = QtWidgets.QLabel(user_logging)
        self.lbl_title.setGeometry(QtCore.QRect(10, 0, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lbl_title.setFont(font)
        self.lbl_title.setObjectName("lbl_title")
        self.horizontalLayoutWidget = QtWidgets.QWidget(user_logging)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 120, 461, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_login = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.btn_exit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)

        self.retranslateUi(user_logging)
        QtCore.QMetaObject.connectSlotsByName(user_logging)
        user_logging.setTabOrder(self.txt_login, self.txt_password)
        user_logging.setTabOrder(self.txt_password, self.btn_login)
        user_logging.setTabOrder(self.btn_login, self.btn_exit)

    def retranslateUi(self, user_logging):
        _translate = QtCore.QCoreApplication.translate
        user_logging.setWindowTitle(_translate("user_logging", "Dialog"))
        user_logging.setWhatsThis(_translate("user_logging", "Enter here the name of the model"))
        self.lbl_login.setText(_translate("user_logging", "Login :"))
        self.lbl_password.setText(_translate("user_logging", "Password :"))
        self.lbl_title.setText(_translate("user_logging", "Login"))
        self.btn_login.setText(_translate("user_logging", "Login"))
        self.btn_exit.setText(_translate("user_logging", "Exit"))

