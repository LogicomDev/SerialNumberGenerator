# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\J_MARCHAL\workspace\SerialNumberGenerator\src\lsng\hmi\edit_model\edit_model_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_edit_model(object):
    def setupUi(self, edit_model):
        edit_model.setObjectName("edit_model")
        edit_model.setWindowModality(QtCore.Qt.ApplicationModal)
        edit_model.resize(470, 446)
        edit_model.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        edit_model.setStyleSheet("QDialog\n"
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
        edit_model.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        edit_model.setModal(True)
        self.gridLayoutWidget = QtWidgets.QWidget(edit_model)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 451, 392))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.sp_code = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sp_code.setMinimumSize(QtCore.QSize(0, 30))
        self.sp_code.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.sp_code.setFont(font)
        self.sp_code.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sp_code.setStyleSheet("")
        self.sp_code.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_code.setMinimum(1)
        self.sp_code.setObjectName("sp_code")
        self.gridLayout.addWidget(self.sp_code, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(200, 30))
        self.label_3.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lbl_supplier = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_supplier.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_supplier.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_supplier.setFont(font)
        self.lbl_supplier.setStyleSheet("")
        self.lbl_supplier.setObjectName("lbl_supplier")
        self.gridLayout.addWidget(self.lbl_supplier, 0, 1, 1, 1)
        self.lbl_first_mac = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_first_mac.sizePolicy().hasHeightForWidth())
        self.lbl_first_mac.setSizePolicy(sizePolicy)
        self.lbl_first_mac.setMinimumSize(QtCore.QSize(200, 30))
        self.lbl_first_mac.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_first_mac.setFont(font)
        self.lbl_first_mac.setStyleSheet("")
        self.lbl_first_mac.setObjectName("lbl_first_mac")
        self.gridLayout.addWidget(self.lbl_first_mac, 4, 0, 1, 1)
        self.lbl_code = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_code.setMinimumSize(QtCore.QSize(200, 30))
        self.lbl_code.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_code.setFont(font)
        self.lbl_code.setStyleSheet("")
        self.lbl_code.setObjectName("lbl_code")
        self.gridLayout.addWidget(self.lbl_code, 3, 0, 1, 1)
        self.lbl_name = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_name.sizePolicy().hasHeightForWidth())
        self.lbl_name.setSizePolicy(sizePolicy)
        self.lbl_name.setMinimumSize(QtCore.QSize(200, 30))
        self.lbl_name.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet("")
        self.lbl_name.setObjectName("lbl_name")
        self.gridLayout.addWidget(self.lbl_name, 1, 0, 1, 1)
        self.txt_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_name.setMinimumSize(QtCore.QSize(0, 30))
        self.txt_name.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.txt_name.setFont(font)
        self.txt_name.setStyleSheet("")
        self.txt_name.setObjectName("txt_name")
        self.gridLayout.addWidget(self.txt_name, 1, 1, 1, 1)
        self.sp_sim = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sp_sim.setMinimumSize(QtCore.QSize(0, 30))
        self.sp_sim.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.sp_sim.setFont(font)
        self.sp_sim.setStyleSheet("")
        self.sp_sim.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_sim.setMaximum(2)
        self.sp_sim.setProperty("value", 2)
        self.sp_sim.setObjectName("sp_sim")
        self.gridLayout.addWidget(self.sp_sim, 4, 1, 1, 1)
        self.cb_type = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cb_type.setMinimumSize(QtCore.QSize(0, 30))
        self.cb_type.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.cb_type.setFont(font)
        self.cb_type.setStyleSheet("")
        self.cb_type.setFrame(False)
        self.cb_type.setObjectName("cb_type")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.gridLayout.addWidget(self.cb_type, 9, 1, 1, 1)
        self.cb_wifi = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cb_wifi.setMinimumSize(QtCore.QSize(0, 30))
        self.cb_wifi.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.cb_wifi.setFont(font)
        self.cb_wifi.setStyleSheet("")
        self.cb_wifi.setFrame(False)
        self.cb_wifi.setObjectName("cb_wifi")
        self.cb_wifi.addItem("")
        self.cb_wifi.addItem("")
        self.gridLayout.addWidget(self.cb_wifi, 7, 1, 1, 1)
        self.lbl_tac_code = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lbl_tac_code.setMinimumSize(QtCore.QSize(200, 30))
        self.lbl_tac_code.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tac_code.setFont(font)
        self.lbl_tac_code.setStyleSheet("")
        self.lbl_tac_code.setObjectName("lbl_tac_code")
        self.gridLayout.addWidget(self.lbl_tac_code, 5, 0, 1, 1)
        self.sp_tac_code = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sp_tac_code.setMinimumSize(QtCore.QSize(0, 30))
        self.sp_tac_code.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.sp_tac_code.setFont(font)
        self.sp_tac_code.setStyleSheet("")
        self.sp_tac_code.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_tac_code.setMinimum(0)
        self.sp_tac_code.setMaximum(99999999)
        self.sp_tac_code.setObjectName("sp_tac_code")
        self.gridLayout.addWidget(self.sp_tac_code, 5, 1, 1, 1)
        self.lbl_last_mac = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_last_mac.sizePolicy().hasHeightForWidth())
        self.lbl_last_mac.setSizePolicy(sizePolicy)
        self.lbl_last_mac.setMinimumSize(QtCore.QSize(200, 30))
        self.lbl_last_mac.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_last_mac.setFont(font)
        self.lbl_last_mac.setStyleSheet("")
        self.lbl_last_mac.setObjectName("lbl_last_mac")
        self.gridLayout.addWidget(self.lbl_last_mac, 7, 0, 1, 1)
        self.cb_bt = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cb_bt.setMinimumSize(QtCore.QSize(0, 30))
        self.cb_bt.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.cb_bt.setFont(font)
        self.cb_bt.setStyleSheet("")
        self.cb_bt.setFrame(False)
        self.cb_bt.setObjectName("cb_bt")
        self.cb_bt.addItem("")
        self.cb_bt.addItem("")
        self.gridLayout.addWidget(self.cb_bt, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(200, 30))
        self.label.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(200, 30))
        self.label_4.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("")
        self.btn_save.setFlat(True)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 10, 0, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_cancel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("")
        self.btn_cancel.setFlat(True)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout.addWidget(self.btn_cancel, 10, 1, 1, 1)
        self.lbl_title = QtWidgets.QLabel(edit_model)
        self.lbl_title.setGeometry(QtCore.QRect(10, 0, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(130, 186, 23);")
        self.lbl_title.setObjectName("lbl_title")

        self.retranslateUi(edit_model)
        self.cb_type.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(edit_model)
        edit_model.setTabOrder(self.txt_name, self.sp_code)
        edit_model.setTabOrder(self.sp_code, self.sp_sim)
        edit_model.setTabOrder(self.sp_sim, self.sp_tac_code)
        edit_model.setTabOrder(self.sp_tac_code, self.cb_wifi)
        edit_model.setTabOrder(self.cb_wifi, self.cb_bt)
        edit_model.setTabOrder(self.cb_bt, self.cb_type)
        edit_model.setTabOrder(self.cb_type, self.btn_save)
        edit_model.setTabOrder(self.btn_save, self.btn_cancel)

    def retranslateUi(self, edit_model):
        _translate = QtCore.QCoreApplication.translate
        edit_model.setWindowTitle(_translate("edit_model", "Dialog"))
        edit_model.setWhatsThis(_translate("edit_model", "Enter here the name of the model"))
        self.sp_code.setToolTip(_translate("edit_model", "Model\'s code"))
        self.label_3.setText(_translate("edit_model", "Supplier"))
        self.lbl_supplier.setText(_translate("edit_model", "TextLabel"))
        self.lbl_first_mac.setText(_translate("edit_model", "SIM Number"))
        self.lbl_code.setText(_translate("edit_model", "Model code"))
        self.lbl_name.setText(_translate("edit_model", "Model Name"))
        self.txt_name.setPlaceholderText(_translate("edit_model", "Enter the name of Model here"))
        self.cb_type.setItemText(0, _translate("edit_model", "FEATURE PHONE"))
        self.cb_type.setItemText(1, _translate("edit_model", "SMARTPHONE"))
        self.cb_type.setItemText(2, _translate("edit_model", "TABLET"))
        self.cb_type.setItemText(3, _translate("edit_model", "OTHER"))
        self.cb_wifi.setItemText(0, _translate("edit_model", "Yes"))
        self.cb_wifi.setItemText(1, _translate("edit_model", "No"))
        self.lbl_tac_code.setText(_translate("edit_model", "Base TAC code"))
        self.lbl_last_mac.setText(_translate("edit_model", "WIFI availability"))
        self.cb_bt.setItemText(0, _translate("edit_model", "Yes"))
        self.cb_bt.setItemText(1, _translate("edit_model", "No"))
        self.label.setText(_translate("edit_model", "Bluetooth availability"))
        self.label_4.setText(_translate("edit_model", "Device type"))
        self.btn_save.setText(_translate("edit_model", "Save"))
        self.btn_cancel.setText(_translate("edit_model", "Cancel"))
        self.lbl_title.setText(_translate("edit_model", "Model Creation"))

