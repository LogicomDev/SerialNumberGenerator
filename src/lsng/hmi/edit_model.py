# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_model.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_edit_model(object):
    def setupUi(self, edit_model):
        edit_model.setObjectName("edit_model")
        edit_model.setWindowModality(QtCore.Qt.ApplicationModal)
        edit_model.resize(470, 289)
        edit_model.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        edit_model.setStyleSheet("background-color: rgb(255, 255, 255);")
        edit_model.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        edit_model.setModal(True)
        self.gridLayoutWidget = QtWidgets.QWidget(edit_model)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 50, 461, 202))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(85, 170, 0);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.sp_code = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sp_code.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.sp_code.setFont(font)
        self.sp_code.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sp_code.setStyleSheet("QSpinBox, QSpinBox:hover {\n"
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
"    font-size: 20px;\n"
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
"")
        self.sp_code.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_code.setObjectName("sp_code")
        self.gridLayout.addWidget(self.sp_code, 3, 1, 1, 1)
        self.lbl_code = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_code.setFont(font)
        self.lbl_code.setStyleSheet("color: rgb(85, 170, 0);")
        self.lbl_code.setObjectName("lbl_code")
        self.gridLayout.addWidget(self.lbl_code, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.lbl_first_mac = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_first_mac.sizePolicy().hasHeightForWidth())
        self.lbl_first_mac.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_first_mac.setFont(font)
        self.lbl_first_mac.setStyleSheet("color: rgb(85, 170, 0);")
        self.lbl_first_mac.setObjectName("lbl_first_mac")
        self.gridLayout.addWidget(self.lbl_first_mac, 4, 0, 1, 1)
        self.lbl_name = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_name.sizePolicy().hasHeightForWidth())
        self.lbl_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet("color: rgb(85, 170, 0);")
        self.lbl_name.setObjectName("lbl_name")
        self.gridLayout.addWidget(self.lbl_name, 1, 0, 1, 1)
        self.txt_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.txt_name.setFont(font)
        self.txt_name.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
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
"")
        self.txt_name.setObjectName("txt_name")
        self.gridLayout.addWidget(self.txt_name, 1, 1, 1, 1)
        self.sp_sim = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.sp_sim.setFont(font)
        self.sp_sim.setStyleSheet("QSpinBox, QSpinBox:hover {\n"
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
"    font-size: 20px;\n"
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
"")
        self.sp_sim.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_sim.setMaximum(2)
        self.sp_sim.setProperty("value", 2)
        self.sp_sim.setObjectName("sp_sim")
        self.gridLayout.addWidget(self.sp_sim, 4, 1, 1, 1)
        self.cb_type = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.cb_type.setFont(font)
        self.cb_type.setStyleSheet("background-color: rgba(250, 250, 250, 250);")
        self.cb_type.setFrame(False)
        self.cb_type.setObjectName("cb_type")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.gridLayout.addWidget(self.cb_type, 9, 1, 1, 1)
        self.cb_wifi = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.cb_wifi.setFont(font)
        self.cb_wifi.setStyleSheet("background-color: rgba(250, 250, 250, 250);")
        self.cb_wifi.setFrame(False)
        self.cb_wifi.setObjectName("cb_wifi")
        self.cb_wifi.addItem("")
        self.cb_wifi.addItem("")
        self.gridLayout.addWidget(self.cb_wifi, 7, 1, 1, 1)
        self.lbl_tac_code = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_tac_code.setFont(font)
        self.lbl_tac_code.setStyleSheet("color: rgb(85, 170, 0);")
        self.lbl_tac_code.setObjectName("lbl_tac_code")
        self.gridLayout.addWidget(self.lbl_tac_code, 5, 0, 1, 1)
        self.sp_tac_code = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.sp_tac_code.setFont(font)
        self.sp_tac_code.setStyleSheet("QSpinBox, QSpinBox:hover {\n"
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
"    font-size: 20px;\n"
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
"")
        self.sp_tac_code.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_tac_code.setObjectName("sp_tac_code")
        self.gridLayout.addWidget(self.sp_tac_code, 5, 1, 1, 1)
        self.lbl_last_mac = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_last_mac.sizePolicy().hasHeightForWidth())
        self.lbl_last_mac.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_last_mac.setFont(font)
        self.lbl_last_mac.setStyleSheet("color: rgb(85, 170, 0);")
        self.lbl_last_mac.setObjectName("lbl_last_mac")
        self.gridLayout.addWidget(self.lbl_last_mac, 7, 0, 1, 1)
        self.cb_bt = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.cb_bt.setFont(font)
        self.cb_bt.setStyleSheet("background-color: rgba(250, 250, 250, 250);")
        self.cb_bt.setFrame(False)
        self.cb_bt.setObjectName("cb_bt")
        self.cb_bt.addItem("")
        self.cb_bt.addItem("")
        self.gridLayout.addWidget(self.cb_bt, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 170, 0);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(85, 170, 0);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)
        self.lbl_title = QtWidgets.QLabel(edit_model)
        self.lbl_title.setGeometry(QtCore.QRect(0, 0, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(26)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(85, 170, 0);")
        self.lbl_title.setObjectName("lbl_title")
        self.btn_cancel = QtWidgets.QPushButton(edit_model)
        self.btn_cancel.setGeometry(QtCore.QRect(380, 260, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
"  border: none;\n"
"  color: black;\n"
"  padding: 3px 20px;\n"
"    background-color: rgba(250, 250, 250, 250);\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:hover:focus {\n"
"  background-color: rgb(131, 186, 23);\n"
"  border-color: #ffffff\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:pressed:focus {\n"
"  background-color: #2196f3;\n"
"  border: none;\n"
"  color: white\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: rgb(131, 186, 23);\n"
"    border: none\n"
"}")
        self.btn_cancel.setFlat(True)
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_save = QtWidgets.QPushButton(edit_model)
        self.btn_save.setGeometry(QtCore.QRect(280, 260, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
"  border: none;\n"
"  color: black;\n"
"  padding: 3px 20px;\n"
"    background-color: rgba(250, 250, 250, 250);\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:hover:focus {\n"
"  background-color: rgb(131, 186, 23);\n"
"  border-color: #ffffff\n"
"}\n"
"\n"
"QPushButton:pressed,\n"
"QPushButton:pressed:focus {\n"
"  background-color: #2196f3;\n"
"  border: none;\n"
"  color: white\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: rgb(131, 186, 23);\n"
"    border: none\n"
"}")
        self.btn_save.setFlat(True)
        self.btn_save.setObjectName("btn_save")

        self.retranslateUi(edit_model)
        self.cb_type.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(edit_model)

    def retranslateUi(self, edit_model):
        _translate = QtCore.QCoreApplication.translate
        edit_model.setWindowTitle(_translate("edit_model", "Dialog"))
        edit_model.setWhatsThis(_translate("edit_model", "Enter here the name of the model"))
        self.label_3.setText(_translate("edit_model", "Supplier"))
        self.sp_code.setToolTip(_translate("edit_model", "Model\'s code"))
        self.lbl_code.setText(_translate("edit_model", "Model code"))
        self.label_2.setText(_translate("edit_model", "TextLabel"))
        self.lbl_first_mac.setText(_translate("edit_model", "SIM Number"))
        self.lbl_name.setText(_translate("edit_model", "Model Name"))
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
        self.lbl_title.setText(_translate("edit_model", "Model Creation"))
        self.btn_cancel.setText(_translate("edit_model", "Cancel"))
        self.btn_save.setText(_translate("edit_model", "Save"))

