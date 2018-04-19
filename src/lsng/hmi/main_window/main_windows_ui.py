# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Djer's PC\workspace\lsng\src\lsng\hmi\main_window\main_windows_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(750, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 700))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/lsng_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgba(250, 250, 250, 250);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl_logicom = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logicom.setEnabled(True)
        self.lbl_logicom.setMinimumSize(QtCore.QSize(200, 50))
        self.lbl_logicom.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_logicom.setFont(font)
        self.lbl_logicom.setText("")
        self.lbl_logicom.setPixmap(QtGui.QPixmap("res/Logicom.png"))
        self.lbl_logicom.setScaledContents(True)
        self.lbl_logicom.setObjectName("lbl_logicom")
        self.verticalLayout_6.addWidget(self.lbl_logicom)
        self.lbl_tree = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_tree.setFont(font)
        self.lbl_tree.setObjectName("lbl_tree")
        self.verticalLayout_6.addWidget(self.lbl_tree)
        self.tree_devices = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_devices.sizePolicy().hasHeightForWidth())
        self.tree_devices.setSizePolicy(sizePolicy)
        self.tree_devices.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.tree_devices.setFont(font)
        self.tree_devices.setStyleSheet("QTreeWidget{\n"
"    background-color: rgb(247, 247, 247);\n"
"}\n"
"\n"
"QTreeWidget:item:hover,QTreeWidget:item:focus {\n"
"    background-color: rgb(58, 176, 0);\n"
"}")
        self.tree_devices.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tree_devices.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tree_devices.setAnimated(True)
        self.tree_devices.setHeaderHidden(True)
        self.tree_devices.setObjectName("tree_devices")
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_devices)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_devices)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_devices)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_devices)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_devices)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout_6.addWidget(self.tree_devices)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_add_supplier = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_supplier.sizePolicy().hasHeightForWidth())
        self.btn_add_supplier.setSizePolicy(sizePolicy)
        self.btn_add_supplier.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_supplier.setFont(font)
        self.btn_add_supplier.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
"  border: none;\n"
"  color: black;\n"
"  padding: 3px 20px\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/factory-building.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_supplier.setIcon(icon1)
        self.btn_add_supplier.setObjectName("btn_add_supplier")
        self.horizontalLayout_3.addWidget(self.btn_add_supplier)
        self.btn_add_device = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_device.sizePolicy().hasHeightForWidth())
        self.btn_add_device.setSizePolicy(sizePolicy)
        self.btn_add_device.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_device.setFont(font)
        self.btn_add_device.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
"  border: none;\n"
"  color: black;\n"
"  padding: 3px 20px\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/smartphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_device.setIcon(icon2)
        self.btn_add_device.setObjectName("btn_add_device")
        self.horizontalLayout_3.addWidget(self.btn_add_device)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, 2, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(12, 2, -1, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_color = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_color.sizePolicy().hasHeightForWidth())
        self.lbl_color.setSizePolicy(sizePolicy)
        self.lbl_color.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_color.setFont(font)
        self.lbl_color.setStyleSheet("color: rgb(180, 180, 180);")
        self.lbl_color.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_color.setObjectName("lbl_color")
        self.gridLayout.addWidget(self.lbl_color, 7, 0, 1, 1)
        self.lbl_po_number = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_po_number.sizePolicy().hasHeightForWidth())
        self.lbl_po_number.setSizePolicy(sizePolicy)
        self.lbl_po_number.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_po_number.setFont(font)
        self.lbl_po_number.setStyleSheet("color: rgb(180, 180, 180);")
        self.lbl_po_number.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_po_number.setObjectName("lbl_po_number")
        self.gridLayout.addWidget(self.lbl_po_number, 6, 0, 1, 1)
        self.sp_mac_left = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sp_mac_left.sizePolicy().hasHeightForWidth())
        self.sp_mac_left.setSizePolicy(sizePolicy)
        self.sp_mac_left.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.sp_mac_left.setFont(font)
        self.sp_mac_left.setStyleSheet("QSpinBox, QSpinBox:hover {\n"
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
        self.sp_mac_left.setReadOnly(True)
        self.sp_mac_left.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sp_mac_left.setMaximum(1000000000)
        self.sp_mac_left.setObjectName("sp_mac_left")
        self.gridLayout.addWidget(self.sp_mac_left, 3, 1, 1, 1)
        self.lbl_prod_date = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_prod_date.setFont(font)
        self.lbl_prod_date.setStyleSheet("color: rgb(180, 180, 180);")
        self.lbl_prod_date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_prod_date.setObjectName("lbl_prod_date")
        self.gridLayout.addWidget(self.lbl_prod_date, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(180, 180, 180);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.sp_week = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sp_week.sizePolicy().hasHeightForWidth())
        self.sp_week.setSizePolicy(sizePolicy)
        self.sp_week.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.sp_week.setFont(font)
        self.sp_week.setStyleSheet("QSpinBox, QSpinBox:hover {\n"
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
        self.sp_week.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_week.setMinimum(1)
        self.sp_week.setMaximum(54)
        self.sp_week.setObjectName("sp_week")
        self.gridLayout.addWidget(self.sp_week, 8, 1, 1, 1)
        self.lbl_mac_left = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mac_left.setFont(font)
        self.lbl_mac_left.setStyleSheet("color: rgb(180, 180, 180);")
        self.lbl_mac_left.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_mac_left.setObjectName("lbl_mac_left")
        self.gridLayout.addWidget(self.lbl_mac_left, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        self.sp_imei_left = QtWidgets.QSpinBox(self.centralwidget)
        self.sp_imei_left.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sp_imei_left.sizePolicy().hasHeightForWidth())
        self.sp_imei_left.setSizePolicy(sizePolicy)
        self.sp_imei_left.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.sp_imei_left.setFont(font)
        self.sp_imei_left.setStyleSheet("QSpinBox, QSpinBox:hover {\n"
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
        self.sp_imei_left.setReadOnly(True)
        self.sp_imei_left.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sp_imei_left.setMaximum(1000000000)
        self.sp_imei_left.setObjectName("sp_imei_left")
        self.gridLayout.addWidget(self.sp_imei_left, 3, 2, 1, 1)
        self.lbl_connect = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_connect.setFont(font)
        self.lbl_connect.setStyleSheet("color: rgb(180, 180, 180);")
        self.lbl_connect.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_connect.setObjectName("lbl_connect")
        self.gridLayout.addWidget(self.lbl_connect, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 7, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 8, 3, 1, 1)
        self.sp_year = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sp_year.sizePolicy().hasHeightForWidth())
        self.sp_year.setSizePolicy(sizePolicy)
        self.sp_year.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.sp_year.setFont(font)
        self.sp_year.setStyleSheet("QSpinBox, QSpinBox:hover {\n"
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
        self.sp_year.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_year.setMinimum(18)
        self.sp_year.setMaximum(99)
        self.sp_year.setProperty("value", 18)
        self.sp_year.setObjectName("sp_year")
        self.gridLayout.addWidget(self.sp_year, 8, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 3, 3, 1, 1)
        self.txt_color = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_color.sizePolicy().hasHeightForWidth())
        self.txt_color.setSizePolicy(sizePolicy)
        self.txt_color.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.txt_color.setFont(font)
        self.txt_color.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
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
"\n"
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
        self.txt_color.setInputMask("")
        self.txt_color.setText("")
        self.txt_color.setMaxLength(32767)
        self.txt_color.setObjectName("txt_color")
        self.gridLayout.addWidget(self.txt_color, 7, 1, 1, 2)
        self.txt_user = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_user.sizePolicy().hasHeightForWidth())
        self.txt_user.setSizePolicy(sizePolicy)
        self.txt_user.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet("")
        self.txt_user.setObjectName("txt_user")
        self.gridLayout.addWidget(self.txt_user, 1, 1, 1, 2)
        self.txt_po_number = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_po_number.sizePolicy().hasHeightForWidth())
        self.txt_po_number.setSizePolicy(sizePolicy)
        self.txt_po_number.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.txt_po_number.setFont(font)
        self.txt_po_number.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
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
        self.txt_po_number.setText("")
        self.txt_po_number.setObjectName("txt_po_number")
        self.gridLayout.addWidget(self.txt_po_number, 6, 1, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 6, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 3, 1, 1)
        self.sp_qty = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sp_qty.sizePolicy().hasHeightForWidth())
        self.sp_qty.setSizePolicy(sizePolicy)
        self.sp_qty.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.sp_qty.setFont(font)
        self.sp_qty.setStyleSheet("QSpinBox, QSpinBox:hover {\n"
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
        self.sp_qty.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_qty.setMinimum(1)
        self.sp_qty.setMaximum(100000)
        self.sp_qty.setObjectName("sp_qty")
        self.gridLayout.addWidget(self.sp_qty, 10, 1, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 10, 3, 1, 1)
        self.lbl_qty = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_qty.setFont(font)
        self.lbl_qty.setStyleSheet("color: rgb(180, 180, 180);")
        self.lbl_qty.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_qty.setObjectName("lbl_qty")
        self.gridLayout.addWidget(self.lbl_qty, 10, 0, 1, 1)
        self.txt_model = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_model.sizePolicy().hasHeightForWidth())
        self.txt_model.setSizePolicy(sizePolicy)
        self.txt_model.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.txt_model.setFont(font)
        self.txt_model.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
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
"    font-size: 20px;\n"
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
        self.txt_model.setReadOnly(True)
        self.txt_model.setObjectName("txt_model")
        self.gridLayout.addWidget(self.txt_model, 4, 2, 1, 1)
        self.txt_supplier = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_supplier.sizePolicy().hasHeightForWidth())
        self.txt_supplier.setSizePolicy(sizePolicy)
        self.txt_supplier.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.txt_supplier.setFont(font)
        self.txt_supplier.setStyleSheet("QLineEdit, QLineEdit:hover {\n"
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
"    font-size: 20px;\n"
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
        self.txt_supplier.setText("")
        self.txt_supplier.setReadOnly(True)
        self.txt_supplier.setObjectName("txt_supplier")
        self.gridLayout.addWidget(self.txt_supplier, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_generate.sizePolicy().hasHeightForWidth())
        self.btn_generate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_generate.setFont(font)
        self.btn_generate.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
"  border: none;\n"
"  color: black;\n"
"  padding: 3px 20px\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("res/settings-gears.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_generate.setIcon(icon3)
        self.btn_generate.setFlat(True)
        self.btn_generate.setObjectName("btn_generate")
        self.horizontalLayout_2.addWidget(self.btn_generate)
        self.prg_generation = QtWidgets.QProgressBar(self.centralwidget)
        self.prg_generation.setMinimumSize(QtCore.QSize(0, 24))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.prg_generation.setFont(font)
        self.prg_generation.setStyleSheet("")
        self.prg_generation.setProperty("value", 0)
        self.prg_generation.setAlignment(QtCore.Qt.AlignCenter)
        self.prg_generation.setInvertedAppearance(False)
        self.prg_generation.setObjectName("prg_generation")
        self.horizontalLayout_2.addWidget(self.prg_generation)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.txt_log = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.txt_log.setFont(font)
        self.txt_log.setStyleSheet("QTableWidget {\n"
"    background-color: white;\n"
"    selection-background-color: rgb(131, 186, 23);\n"
"}\n"
"\n"
"QTableWidgetItem:hover{\n"
"    background-color: rgb(0, 170, 255);\n"
"}")
        self.txt_log.setFrameShape(QtWidgets.QFrame.Panel)
        self.txt_log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.txt_log.setLineWidth(2)
        self.txt_log.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.txt_log.setProperty("showDropIndicator", False)
        self.txt_log.setDragDropOverwriteMode(False)
        self.txt_log.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.txt_log.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.txt_log.setShowGrid(False)
        self.txt_log.setGridStyle(QtCore.Qt.SolidLine)
        self.txt_log.setWordWrap(True)
        self.txt_log.setObjectName("txt_log")
        self.txt_log.setColumnCount(3)
        self.txt_log.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.txt_log.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.txt_log.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.txt_log.setHorizontalHeaderItem(2, item)
        self.txt_log.horizontalHeader().setVisible(False)
        self.txt_log.horizontalHeader().setMinimumSectionSize(32)
        self.txt_log.horizontalHeader().setSortIndicatorShown(False)
        self.txt_log.horizontalHeader().setStretchLastSection(True)
        self.txt_log.verticalHeader().setVisible(False)
        self.txt_log.verticalHeader().setDefaultSectionSize(20)
        self.txt_log.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout.addWidget(self.txt_log)
        self.lyt_unsaved = QtWidgets.QHBoxLayout()
        self.lyt_unsaved.setContentsMargins(-1, 2, -1, 0)
        self.lyt_unsaved.setObjectName("lyt_unsaved")
        self.lbl_info_pool_unsaved = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_info_pool_unsaved.setFont(font)
        self.lbl_info_pool_unsaved.setObjectName("lbl_info_pool_unsaved")
        self.lyt_unsaved.addWidget(self.lbl_info_pool_unsaved)
        self.lbl_pool_unsaved = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_pool_unsaved.setFont(font)
        self.lbl_pool_unsaved.setObjectName("lbl_pool_unsaved")
        self.lyt_unsaved.addWidget(self.lbl_pool_unsaved)
        self.verticalLayout.addLayout(self.lyt_unsaved)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("QPushButton, QPushButton:focus, QPushButton:focus {\n"
"  border: none;\n"
"  color: black;\n"
"  padding: 3px 20px\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("res/download-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon4)
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout.addWidget(self.btn_save)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txt_po_number, self.txt_color)
        MainWindow.setTabOrder(self.txt_color, self.sp_week)
        MainWindow.setTabOrder(self.sp_week, self.sp_year)
        MainWindow.setTabOrder(self.sp_year, self.sp_qty)
        MainWindow.setTabOrder(self.sp_qty, self.btn_generate)
        MainWindow.setTabOrder(self.btn_generate, self.txt_log)
        MainWindow.setTabOrder(self.txt_log, self.tree_devices)
        MainWindow.setTabOrder(self.tree_devices, self.btn_save)
        MainWindow.setTabOrder(self.btn_save, self.sp_mac_left)
        MainWindow.setTabOrder(self.sp_mac_left, self.sp_imei_left)
        MainWindow.setTabOrder(self.sp_imei_left, self.txt_supplier)
        MainWindow.setTabOrder(self.txt_supplier, self.txt_model)
        MainWindow.setTabOrder(self.txt_model, self.btn_add_supplier)
        MainWindow.setTabOrder(self.btn_add_supplier, self.btn_add_device)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LSNG - Logicom Serial Number Generator - v.3.0"))
        self.lbl_tree.setText(_translate("MainWindow", "Choose a device :"))
        self.tree_devices.setSortingEnabled(True)
        self.tree_devices.headerItem().setText(0, _translate("MainWindow", "Logicom"))
        __sortingEnabled = self.tree_devices.isSortingEnabled()
        self.tree_devices.setSortingEnabled(False)
        self.tree_devices.topLevelItem(0).setText(0, _translate("MainWindow", "5"))
        self.tree_devices.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "51"))
        self.tree_devices.topLevelItem(1).setText(0, _translate("MainWindow", "4"))
        self.tree_devices.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "42"))
        self.tree_devices.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "41"))
        self.tree_devices.topLevelItem(2).setText(0, _translate("MainWindow", "3"))
        self.tree_devices.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "33"))
        self.tree_devices.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "32"))
        self.tree_devices.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "31"))
        self.tree_devices.topLevelItem(3).setText(0, _translate("MainWindow", "2"))
        self.tree_devices.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "22"))
        self.tree_devices.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "21"))
        self.tree_devices.topLevelItem(4).setText(0, _translate("MainWindow", "1"))
        self.tree_devices.topLevelItem(4).child(0).setText(0, _translate("MainWindow", "11"))
        self.tree_devices.setSortingEnabled(__sortingEnabled)
        self.btn_add_supplier.setText(_translate("MainWindow", "Add Supplier"))
        self.btn_add_device.setText(_translate("MainWindow", "Add Device"))
        self.lbl_color.setText(_translate("MainWindow", "Color"))
        self.lbl_po_number.setText(_translate("MainWindow", "PO Number"))
        self.lbl_prod_date.setText(_translate("MainWindow", "Production week / year"))
        self.label_2.setText(_translate("MainWindow", "Supplier code / Model code"))
        self.lbl_mac_left.setText(_translate("MainWindow", "MAC / IMEIs address left"))
        self.lbl_connect.setText(_translate("MainWindow", "Connected as"))
        self.txt_color.setPlaceholderText(_translate("MainWindow", "Fill me"))
        self.txt_user.setText(_translate("MainWindow", "Unknown User"))
        self.txt_po_number.setPlaceholderText(_translate("MainWindow", "Fill me"))
        self.lbl_qty.setText(_translate("MainWindow", "Quantity"))
        self.txt_model.setPlaceholderText(_translate("MainWindow", "00"))
        self.txt_supplier.setPlaceholderText(_translate("MainWindow", "00"))
        self.btn_generate.setText(_translate("MainWindow", "Generate Serial Numbers"))
        item = self.txt_log.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time"))
        item = self.txt_log.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Info"))
        self.lbl_info_pool_unsaved.setText(_translate("MainWindow", "Unsaved modification (generations) :"))
        self.lbl_pool_unsaved.setText(_translate("MainWindow", "TextLabel"))
        self.btn_save.setText(_translate("MainWindow", "Create run report(s) and save Generation(s)"))

