# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_supplier.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_edit_supplier(object):
    def setupUi(self, edit_supplier):
        edit_supplier.setObjectName("edit_supplier")
        edit_supplier.resize(470, 210)
        edit_supplier.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        edit_supplier.setStyleSheet("background-color: rgb(255, 255, 255);")
        edit_supplier.setModal(True)
        self.lbl_title = QtWidgets.QLabel(edit_supplier)
        self.lbl_title.setGeometry(QtCore.QRect(0, 0, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(26)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: rgb(85, 170, 0);")
        self.lbl_title.setObjectName("lbl_title")
        self.gridLayoutWidget = QtWidgets.QWidget(edit_supplier)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 50, 461, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
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
        self.gridLayout.addWidget(self.lbl_name, 0, 0, 1, 1)
        self.txt_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
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
        self.gridLayout.addWidget(self.txt_name, 0, 2, 1, 1)
        self.txt_last_mac = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_last_mac.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
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
        self.txt_last_mac.setObjectName("txt_last_mac")
        self.gridLayout.addWidget(self.txt_last_mac, 3, 2, 1, 1)
        self.lbl_code = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_code.setFont(font)
        self.lbl_code.setStyleSheet("color: rgb(85, 170, 0);")
        self.lbl_code.setObjectName("lbl_code")
        self.gridLayout.addWidget(self.lbl_code, 1, 0, 1, 1)
        self.sp_code = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sp_code.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.sp_code.setFont(font)
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
        self.gridLayout.addWidget(self.sp_code, 1, 2, 1, 1)
        self.txt_first_mac = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_first_mac.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
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
        self.txt_first_mac.setObjectName("txt_first_mac")
        self.gridLayout.addWidget(self.txt_first_mac, 2, 2, 1, 1)
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
        self.gridLayout.addWidget(self.lbl_last_mac, 3, 0, 1, 1)
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
        self.gridLayout.addWidget(self.lbl_first_mac, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.btn_save = QtWidgets.QPushButton(edit_supplier)
        self.btn_save.setGeometry(QtCore.QRect(280, 180, 91, 23))
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
        self.btn_cancel = QtWidgets.QPushButton(edit_supplier)
        self.btn_cancel.setGeometry(QtCore.QRect(380, 180, 81, 23))
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

        self.retranslateUi(edit_supplier)
        QtCore.QMetaObject.connectSlotsByName(edit_supplier)

    def retranslateUi(self, edit_supplier):
        _translate = QtCore.QCoreApplication.translate
        edit_supplier.setWindowTitle(_translate("edit_supplier", "Create Supplier"))
        self.lbl_title.setText(_translate("edit_supplier", "Supplier Creation"))
        self.lbl_name.setText(_translate("edit_supplier", "Supplier Name"))
        self.txt_last_mac.setInputMask(_translate("edit_supplier", "xx-xx-xx-xx-xx"))
        self.lbl_code.setText(_translate("edit_supplier", "Supplier code"))
        self.txt_first_mac.setInputMask(_translate("edit_supplier", "xx-xx-xx-xx-xx"))
        self.lbl_last_mac.setText(_translate("edit_supplier", "Last MAC"))
        self.lbl_first_mac.setText(_translate("edit_supplier", "First MAC"))
        self.btn_save.setText(_translate("edit_supplier", "Save"))
        self.btn_cancel.setText(_translate("edit_supplier", "Cancel"))

