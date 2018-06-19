# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\J_MARCHAL\workspace\SerialNumberGenerator\src\lsng\hmi\edit_supplier\edit_supplier_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_edit_supplier(object):
    def setupUi(self, edit_supplier):
        edit_supplier.setObjectName("edit_supplier")
        edit_supplier.setWindowModality(QtCore.Qt.WindowModal)
        edit_supplier.resize(470, 210)
        edit_supplier.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        edit_supplier.setStyleSheet("QDialog\n"
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
        edit_supplier.setModal(True)
        self.lbl_title = QtWidgets.QLabel(edit_supplier)
        self.lbl_title.setGeometry(QtCore.QRect(10, 0, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(130, 186, 23);")
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayoutWidget = QtWidgets.QWidget(edit_supplier)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 451, 154))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_last_mac = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_last_mac.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.txt_last_mac.setFont(font)
        self.txt_last_mac.setStyleSheet("")
        self.txt_last_mac.setInputMask("")
        self.txt_last_mac.setObjectName("txt_last_mac")
        self.gridLayout.addWidget(self.txt_last_mac, 3, 1, 1, 1)
        self.lbl_code = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_code.sizePolicy().hasHeightForWidth())
        self.lbl_code.setSizePolicy(sizePolicy)
        self.lbl_code.setMinimumSize(QtCore.QSize(200, 30))
        self.lbl_code.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_code.setFont(font)
        self.lbl_code.setStyleSheet("")
        self.lbl_code.setObjectName("lbl_code")
        self.gridLayout.addWidget(self.lbl_code, 1, 0, 1, 1)
        self.txt_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_name.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.txt_name.setFont(font)
        self.txt_name.setStyleSheet("")
        self.txt_name.setObjectName("txt_name")
        self.gridLayout.addWidget(self.txt_name, 0, 1, 1, 1)
        self.lbl_name = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_name.sizePolicy().hasHeightForWidth())
        self.lbl_name.setSizePolicy(sizePolicy)
        self.lbl_name.setMinimumSize(QtCore.QSize(200, 30))
        self.lbl_name.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet("")
        self.lbl_name.setObjectName("lbl_name")
        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 1)
        self.lbl_last_mac = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_last_mac.sizePolicy().hasHeightForWidth())
        self.lbl_last_mac.setSizePolicy(sizePolicy)
        self.lbl_last_mac.setMinimumSize(QtCore.QSize(200, 30))
        self.lbl_last_mac.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_last_mac.setFont(font)
        self.lbl_last_mac.setStyleSheet("")
        self.lbl_last_mac.setObjectName("lbl_last_mac")
        self.gridLayout.addWidget(self.lbl_last_mac, 3, 0, 1, 1)
        self.sp_code = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sp_code.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.sp_code.setFont(font)
        self.sp_code.setStyleSheet("")
        self.sp_code.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_code.setMinimum(1)
        self.sp_code.setObjectName("sp_code")
        self.gridLayout.addWidget(self.sp_code, 1, 1, 1, 1)
        self.txt_first_mac = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_first_mac.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.txt_first_mac.setFont(font)
        self.txt_first_mac.setStyleSheet("")
        self.txt_first_mac.setInputMask("")
        self.txt_first_mac.setObjectName("txt_first_mac")
        self.gridLayout.addWidget(self.txt_first_mac, 2, 1, 1, 1)
        self.lbl_first_mac = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_first_mac.sizePolicy().hasHeightForWidth())
        self.lbl_first_mac.setSizePolicy(sizePolicy)
        self.lbl_first_mac.setMinimumSize(QtCore.QSize(200, 30))
        self.lbl_first_mac.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_first_mac.setFont(font)
        self.lbl_first_mac.setStyleSheet("")
        self.lbl_first_mac.setObjectName("lbl_first_mac")
        self.gridLayout.addWidget(self.lbl_first_mac, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("")
        self.btn_save.setFlat(True)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_cancel = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_cancel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("")
        self.btn_cancel.setFlat(True)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)

        self.retranslateUi(edit_supplier)
        QtCore.QMetaObject.connectSlotsByName(edit_supplier)
        edit_supplier.setTabOrder(self.txt_name, self.sp_code)
        edit_supplier.setTabOrder(self.sp_code, self.txt_first_mac)
        edit_supplier.setTabOrder(self.txt_first_mac, self.txt_last_mac)
        edit_supplier.setTabOrder(self.txt_last_mac, self.btn_save)
        edit_supplier.setTabOrder(self.btn_save, self.btn_cancel)

    def retranslateUi(self, edit_supplier):
        _translate = QtCore.QCoreApplication.translate
        edit_supplier.setWindowTitle(_translate("edit_supplier", "Create Supplier"))
        self.lbl_title.setText(_translate("edit_supplier", "Supplier Creation"))
        self.txt_last_mac.setPlaceholderText(_translate("edit_supplier", "AA-BB-CC-DD-EE"))
        self.lbl_code.setText(_translate("edit_supplier", "Supplier code"))
        self.lbl_name.setText(_translate("edit_supplier", "Supplier Name"))
        self.lbl_last_mac.setText(_translate("edit_supplier", "Last MAC"))
        self.txt_first_mac.setPlaceholderText(_translate("edit_supplier", "AA-BB-CC-DD-EE"))
        self.lbl_first_mac.setText(_translate("edit_supplier", "First MAC"))
        self.btn_save.setText(_translate("edit_supplier", "Save"))
        self.btn_cancel.setText(_translate("edit_supplier", "Cancel"))

