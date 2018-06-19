# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\J_MARCHAL\workspace\SerialNumberGenerator\src\lsng\hmi\login\user_logging_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_user_logging(object):
    def setupUi(self, user_logging):
        user_logging.setObjectName("user_logging")
        user_logging.resize(479, 217)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/lsng_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        user_logging.setWindowIcon(icon)
        user_logging.setStyleSheet("QDialog\n"
"{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"color: rgb(138, 138, 138);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit, QLineEdit:hover {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 1px solid #dddddd;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QLineEdit:editable{\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #b2dfdb;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #eeeeee;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"    color: #111111;\n"
"}\n"
"QLineEdit:pressed {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"}\n"
"\n"
"QSpinBox, QSpinBox:hover {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 1px solid #dddddd;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QSpinBox:editable{\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #b2dfdb;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #eeeeee;\n"
"}\n"
"\n"
"QSpinBox:focus{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"    color: #111111;\n"
"}\n"
"QSpinBox:pressed {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(230, 230, 230);;    \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: rgb(130, 186, 23);\n"
"    width: 20px;\n"
"}\n"
"\n"
"QPushButton, QPushButton:focus {\n"
"  border: none;\n"
"  color: black;\n"
"  padding: 3px 20px\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:hover:focus {\n"
"  background-color: rgb(130, 186, 23);\n"
"  border-color: #ffffff\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: rgb(131, 186, 23);\n"
"    border: none\n"
"}\n"
"\n"
"QTreeWidget{\n"
"    background-color: rgb(150,150, 150);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTreeWidget:item:hover,QTreeWidget:item:focus {\n"
"    background-color: rgb(58, 176, 0);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    selection-background-color: rgb(150,150, 150);\n"
"}\n"
"\n"
"QTableWidgetItem:hover{\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: red;\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 4px; right: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background: green;\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: pink;\n"
"}\n"
"\n"
"QGroupBox{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(217, 217, 217);\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QCheckBox, QCheckBox:hover {\\n    border: none;\\n    padding-bottom: 2px;\\n    border-bottom: 1px solid #dddddd;\\n    background-color:rgba(0,0,0,0);\\n}\\n\\nQCheckBox:editable{\\n    border: none;\\n    padding-bottom: 2px;\\n    border-bottom: 2px solid #b2dfdb;\\n\\n}\\n\\nQCheckBox:disabled{\\n    border: 0px solid white;\\n    padding-bottom: 2px;\\n    border-bottom: 2px solid #eeeeee;\\n}\\n\\nQCheckBox:focus{\\n    border: 0px solid white;\\n    padding-bottom: 2px;\\n    border-bottom: 2px solid #00695c;\\n    color: #111111;\\n}\\n\\nQCheckBox:pressed {\\n    border: none;\\n    padding-bottom: 2px;\\n    border-bottom: 2px solid #00695c;\\n}\\n\n"
"")
        user_logging.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.gridLayoutWidget = QtWidgets.QWidget(user_logging)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 461, 158))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_login = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_login.setMinimumSize(QtCore.QSize(0, 30))
        self.txt_login.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.txt_login.setFont(font)
        self.txt_login.setStyleSheet("")
        self.txt_login.setFrame(False)
        self.txt_login.setObjectName("txt_login")
        self.gridLayout.addWidget(self.txt_login, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.lbl_password = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")
        self.gridLayout.addWidget(self.lbl_password, 2, 0, 1, 1)
        self.txt_password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_password.setMinimumSize(QtCore.QSize(0, 30))
        self.txt_password.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet("")
        self.txt_password.setFrame(False)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.gridLayout.addWidget(self.txt_password, 2, 2, 1, 1)
        self.lbl_login = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_login.sizePolicy().hasHeightForWidth())
        self.lbl_login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_login.setFont(font)
        self.lbl_login.setObjectName("lbl_login")
        self.gridLayout.addWidget(self.lbl_login, 0, 0, 1, 1)
        self.cb_remember = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.cb_remember.setMinimumSize(QtCore.QSize(0, 30))
        self.cb_remember.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.cb_remember.setFont(font)
        self.cb_remember.setObjectName("cb_remember")
        self.gridLayout.addWidget(self.cb_remember, 3, 1, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_login = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_login.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_login.setFont(font)
        self.btn_login.setFlat(True)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout.addWidget(self.btn_login)
        self.btn_exit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_exit.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_exit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setFlat(True)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 3)
        self.lbl_title = QtWidgets.QLabel(user_logging)
        self.lbl_title.setGeometry(QtCore.QRect(10, 0, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(130, 186, 23);")
        self.lbl_title.setObjectName("lbl_title")

        self.retranslateUi(user_logging)
        QtCore.QMetaObject.connectSlotsByName(user_logging)
        user_logging.setTabOrder(self.txt_login, self.txt_password)
        user_logging.setTabOrder(self.txt_password, self.btn_login)
        user_logging.setTabOrder(self.btn_login, self.btn_exit)

    def retranslateUi(self, user_logging):
        _translate = QtCore.QCoreApplication.translate
        user_logging.setWindowTitle(_translate("user_logging", "Login"))
        user_logging.setWhatsThis(_translate("user_logging", "Enter here the name of the model"))
        self.lbl_password.setText(_translate("user_logging", "Password :"))
        self.lbl_login.setText(_translate("user_logging", "Login :"))
        self.cb_remember.setText(_translate("user_logging", "Remember Me"))
        self.btn_login.setText(_translate("user_logging", "Login"))
        self.btn_exit.setText(_translate("user_logging", "Exit"))
        self.lbl_title.setText(_translate("user_logging", "Login"))

