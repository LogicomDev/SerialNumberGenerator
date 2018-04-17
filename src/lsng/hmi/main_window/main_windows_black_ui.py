# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\J_MARCHAL\eclipse-workspace\lsng\src\lsng\hmi\main_window\main_windows_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(962, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 700))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../res/lsng_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n"
"QMainWindow\n"
"{\n"
"background-color: rgb(237,241,242);\n"
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
"QPushButton, QPushButton:focus, QPushButton:focus {\n"
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
"}\n"
"\n"
"QTreeWidget{\n"
"    background-color: rgb(59, 59, 59);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTreeWidget:item:hover,QTreeWidget:item:focus {\n"
"    background-color: rgb(58, 176, 0);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    selection-background-color: rgb(130, 186, 23);\n"
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
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl_tree = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_tree.setFont(font)
        self.lbl_tree.setStyleSheet("background-color: rgb(56, 56, 56);\n"
"color: rgb(131, 186, 22);")
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
        self.tree_devices.setStyleSheet("")
        self.tree_devices.setFrameShape(QtWidgets.QFrame.NoFrame)
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
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 310))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 651, 222))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txt_supplier = QtWidgets.QLineEdit(self.gridLayoutWidget)
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
        self.txt_supplier.setStyleSheet("")
        self.txt_supplier.setText("")
        self.txt_supplier.setReadOnly(True)
        self.txt_supplier.setObjectName("txt_supplier")
        self.gridLayout_3.addWidget(self.txt_supplier, 3, 2, 1, 1)
        self.lbl_po_number = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
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
        self.lbl_po_number.setStyleSheet("")
        self.lbl_po_number.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_po_number.setObjectName("lbl_po_number")
        self.gridLayout_3.addWidget(self.lbl_po_number, 6, 0, 1, 1)
        self.lbl_prod_date = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_prod_date.sizePolicy().hasHeightForWidth())
        self.lbl_prod_date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_prod_date.setFont(font)
        self.lbl_prod_date.setStyleSheet("")
        self.lbl_prod_date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_prod_date.setObjectName("lbl_prod_date")
        self.gridLayout_3.addWidget(self.lbl_prod_date, 5, 0, 1, 1)
        self.sp_year = QtWidgets.QSpinBox(self.gridLayoutWidget)
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
        self.gridLayout_3.addWidget(self.sp_year, 5, 3, 1, 1)
        self.sp_imei_left = QtWidgets.QSpinBox(self.gridLayoutWidget)
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
        self.sp_imei_left.setStyleSheet("")
        self.sp_imei_left.setReadOnly(True)
        self.sp_imei_left.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sp_imei_left.setMaximum(1000000000)
        self.sp_imei_left.setObjectName("sp_imei_left")
        self.gridLayout_3.addWidget(self.sp_imei_left, 2, 3, 1, 1)
        self.sp_mac_left = QtWidgets.QSpinBox(self.gridLayoutWidget)
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
        self.gridLayout_3.addWidget(self.sp_mac_left, 2, 2, 1, 1)
        self.lbl_color = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
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
        self.lbl_color.setStyleSheet("")
        self.lbl_color.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_color.setObjectName("lbl_color")
        self.gridLayout_3.addWidget(self.lbl_color, 7, 0, 1, 1)
        self.lbl_mac_left = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_mac_left.sizePolicy().hasHeightForWidth())
        self.lbl_mac_left.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mac_left.setFont(font)
        self.lbl_mac_left.setStyleSheet("")
        self.lbl_mac_left.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_mac_left.setObjectName("lbl_mac_left")
        self.gridLayout_3.addWidget(self.lbl_mac_left, 2, 0, 1, 1)
        self.txt_user = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
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
        self.gridLayout_3.addWidget(self.txt_user, 0, 2, 1, 2)
        self.lbl_connect = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_connect.sizePolicy().hasHeightForWidth())
        self.lbl_connect.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_connect.setFont(font)
        self.lbl_connect.setStyleSheet("")
        self.lbl_connect.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_connect.setObjectName("lbl_connect")
        self.gridLayout_3.addWidget(self.lbl_connect, 0, 0, 1, 1)
        self.txt_color = QtWidgets.QLineEdit(self.gridLayoutWidget)
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
        self.txt_color.setStyleSheet("")
        self.txt_color.setInputMask("")
        self.txt_color.setText("")
        self.txt_color.setMaxLength(32767)
        self.txt_color.setObjectName("txt_color")
        self.gridLayout_3.addWidget(self.txt_color, 7, 2, 1, 2)
        self.sp_week = QtWidgets.QSpinBox(self.gridLayoutWidget)
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
        self.sp_week.setStyleSheet("")
        self.sp_week.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_week.setMinimum(1)
        self.sp_week.setMaximum(54)
        self.sp_week.setObjectName("sp_week")
        self.gridLayout_3.addWidget(self.sp_week, 5, 2, 1, 1)
        self.sp_qty = QtWidgets.QSpinBox(self.gridLayoutWidget)
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
        self.sp_qty.setStyleSheet("")
        self.sp_qty.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sp_qty.setMinimum(1)
        self.sp_qty.setMaximum(100000)
        self.sp_qty.setObjectName("sp_qty")
        self.gridLayout_3.addWidget(self.sp_qty, 8, 2, 1, 2)
        self.txt_po_number = QtWidgets.QLineEdit(self.gridLayoutWidget)
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
        self.txt_po_number.setStyleSheet("")
        self.txt_po_number.setText("")
        self.txt_po_number.setObjectName("txt_po_number")
        self.gridLayout_3.addWidget(self.txt_po_number, 6, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)
        self.txt_model = QtWidgets.QLineEdit(self.gridLayoutWidget)
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
        self.txt_model.setStyleSheet("")
        self.txt_model.setReadOnly(True)
        self.txt_model.setObjectName("txt_model")
        self.gridLayout_3.addWidget(self.txt_model, 3, 3, 1, 1)
        self.lbl_qty = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setBold(True)
        font.setWeight(75)
        self.lbl_qty.setFont(font)
        self.lbl_qty.setStyleSheet("")
        self.lbl_qty.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_qty.setObjectName("lbl_qty")
        self.gridLayout_3.addWidget(self.lbl_qty, 8, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setSpacing(6)
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
        self.btn_generate.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../res/settings-gears.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_generate.setIcon(icon1)
        self.btn_generate.setFlat(True)
        self.btn_generate.setObjectName("btn_generate")
        self.horizontalLayout_2.addWidget(self.btn_generate)
        self.prg_generation = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prg_generation.sizePolicy().hasHeightForWidth())
        self.prg_generation.setSizePolicy(sizePolicy)
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
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 661, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.txt_log = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.txt_log.setFont(font)
        self.txt_log.setStyleSheet("")
        self.txt_log.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txt_log.setFrameShadow(QtWidgets.QFrame.Plain)
        self.txt_log.setLineWidth(2)
        self.txt_log.setProperty("showDropIndicator", False)
        self.txt_log.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.txt_log.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.txt_log.setShowGrid(False)
        self.txt_log.setGridStyle(QtCore.Qt.NoPen)
        self.txt_log.setWordWrap(False)
        self.txt_log.setCornerButtonEnabled(False)
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
        self.horizontalLayout_7.addWidget(self.txt_log)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_info_pool_unsaved = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_info_pool_unsaved.setFont(font)
        self.lbl_info_pool_unsaved.setObjectName("lbl_info_pool_unsaved")
        self.horizontalLayout_6.addWidget(self.lbl_info_pool_unsaved)
        self.lbl_pool_unsaved = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_pool_unsaved.setFont(font)
        self.lbl_pool_unsaved.setObjectName("lbl_pool_unsaved")
        self.horizontalLayout_6.addWidget(self.lbl_pool_unsaved)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_add_device = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_device.sizePolicy().hasHeightForWidth())
        self.btn_add_device.setSizePolicy(sizePolicy)
        self.btn_add_device.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_device.setFont(font)
        self.btn_add_device.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../res/smartphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_device.setIcon(icon2)
        self.btn_add_device.setObjectName("btn_add_device")
        self.horizontalLayout_4.addWidget(self.btn_add_device)
        self.btn_add_supplier = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_supplier.sizePolicy().hasHeightForWidth())
        self.btn_add_supplier.setSizePolicy(sizePolicy)
        self.btn_add_supplier.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_supplier.setFont(font)
        self.btn_add_supplier.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../res/factory-building.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_supplier.setIcon(icon3)
        self.btn_add_supplier.setObjectName("btn_add_supplier")
        self.horizontalLayout_4.addWidget(self.btn_add_supplier)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../res/download-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon4)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_4.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_6.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(100, 80))
        self.frame.setStyleSheet("background-color: rgb(48, 48, 48)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_logicom_2 = QtWidgets.QLabel(self.frame)
        self.lbl_logicom_2.setGeometry(QtCore.QRect(10, 20, 200, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_logicom_2.sizePolicy().hasHeightForWidth())
        self.lbl_logicom_2.setSizePolicy(sizePolicy)
        self.lbl_logicom_2.setMinimumSize(QtCore.QSize(200, 50))
        self.lbl_logicom_2.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_logicom_2.setFont(font)
        self.lbl_logicom_2.setText("")
        self.lbl_logicom_2.setPixmap(QtGui.QPixmap("../../res/Logicom.png"))
        self.lbl_logicom_2.setScaledContents(True)
        self.lbl_logicom_2.setObjectName("lbl_logicom_2")
        self.gridLayout_6.addWidget(self.frame, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LSNG - Logicom Serial Number Generator - v.3.0"))
        self.lbl_tree.setText(_translate("MainWindow", "Choose a device"))
        self.tree_devices.headerItem().setText(0, _translate("MainWindow", "Logicom"))
        __sortingEnabled = self.tree_devices.isSortingEnabled()
        self.tree_devices.setSortingEnabled(False)
        self.tree_devices.topLevelItem(0).setText(0, _translate("MainWindow", "1"))
        self.tree_devices.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "11"))
        self.tree_devices.topLevelItem(1).setText(0, _translate("MainWindow", "2"))
        self.tree_devices.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "21"))
        self.tree_devices.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "22"))
        self.tree_devices.topLevelItem(2).setText(0, _translate("MainWindow", "3"))
        self.tree_devices.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "31"))
        self.tree_devices.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "32"))
        self.tree_devices.topLevelItem(2).child(2).setText(0, _translate("MainWindow", "33"))
        self.tree_devices.topLevelItem(3).setText(0, _translate("MainWindow", "4"))
        self.tree_devices.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "41"))
        self.tree_devices.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "42"))
        self.tree_devices.topLevelItem(4).setText(0, _translate("MainWindow", "5"))
        self.tree_devices.topLevelItem(4).child(0).setText(0, _translate("MainWindow", "51"))
        self.tree_devices.setSortingEnabled(__sortingEnabled)
        self.txt_supplier.setPlaceholderText(_translate("MainWindow", "00"))
        self.lbl_po_number.setText(_translate("MainWindow", "PO Number"))
        self.lbl_prod_date.setText(_translate("MainWindow", "Production week / year"))
        self.lbl_color.setText(_translate("MainWindow", "Color"))
        self.lbl_mac_left.setText(_translate("MainWindow", "MAC / IMEIs address left"))
        self.txt_user.setText(_translate("MainWindow", "Unknown User"))
        self.lbl_connect.setText(_translate("MainWindow", "Connected as"))
        self.txt_color.setPlaceholderText(_translate("MainWindow", "Fill me"))
        self.txt_po_number.setPlaceholderText(_translate("MainWindow", "Fill me"))
        self.label_2.setText(_translate("MainWindow", "Supplier code / Model code"))
        self.txt_model.setPlaceholderText(_translate("MainWindow", "00"))
        self.lbl_qty.setText(_translate("MainWindow", "Quantity"))
        self.btn_generate.setText(_translate("MainWindow", "Generate Serial Numbers"))
        item = self.txt_log.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time"))
        item = self.txt_log.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Info"))
        self.lbl_info_pool_unsaved.setText(_translate("MainWindow", "Unsaved modification (generations) :"))
        self.lbl_pool_unsaved.setText(_translate("MainWindow", "TextLabel"))
        self.btn_add_device.setText(_translate("MainWindow", "Add Device"))
        self.btn_add_supplier.setText(_translate("MainWindow", "Add Supplier"))
        self.btn_save.setText(_translate("MainWindow", "Create run report(s) and save Generation(s)"))

