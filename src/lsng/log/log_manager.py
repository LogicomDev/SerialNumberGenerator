'''
Created on 5 avr. 2018

@author: Djer
'''
import datetime
import os
import logging

from PyQt5.QtWidgets import (QTableWidgetItem, QMessageBox)
from PyQt5.QtGui import (QPixmap, QColor, QIcon)
from PyQt5.QtCore import (Qt)

RESSOURCE_PATH = r"res"  # TODO: fix the path once the launcher is fixed

DEBUG = 0
INFO = 1
OK = 2
WARNING = 3
KO = 4
ERROR = 5
CRITICAL = 6

class LogManager(object):
    '''
        This class was designed to handle all logs/warning that will be used in application
    ''' 

    def __init__(self, parent, logger):
        self.logger = logger
        self.parent = parent
        self.parent.uic.txt_log.setColumnWidth(0, 24)  # icon col
        self.parent.uic.txt_log.setColumnWidth(1, 154)  # time col
    
    def add_trace(self, to_write, scope=DEBUG):
        
        timing = str(datetime.datetime.now())
                
        rows = self.parent.uic.txt_log.rowCount()
        self.parent.uic.txt_log.setRowCount(rows + 1)
        
        if scope == DEBUG:
            self.logger.debug(to_write)
            color = Qt.black
            pixmap = QPixmap("")
        elif scope == OK:
            self.logger.info(to_write)
            color = Qt.green
            iconpath = os.path.join(RESSOURCE_PATH, "log_ok.png")
            pixmap = QPixmap(iconpath)
        elif scope == INFO:
            self.logger.info(to_write)
            color = Qt.blue
            iconpath = os.path.join(RESSOURCE_PATH, "log_info.png")
            pixmap = QPixmap(iconpath)
        elif scope == CRITICAL:
            self.logger.critical(to_write)
            color = Qt.red
            iconpath = os.path.join(RESSOURCE_PATH, "log_critical.png")
            pixmap = QPixmap(iconpath)
        elif scope == WARNING:
            self.logger.warning(to_write)
            color = Qt.red
            iconpath = os.path.join(RESSOURCE_PATH, "log_error.png")
            pixmap = QPixmap(iconpath)
        elif scope == ERROR:
            self.logger.error(to_write)
            color = QColor("Orange")
            iconpath = os.path.join(RESSOURCE_PATH, "log_error.png")
            pixmap = QPixmap(iconpath)
            
        icon = QIcon()
        icon.addPixmap(pixmap, QIcon.Normal, QIcon.Off)
        icon_item = QTableWidgetItem(icon, '')

        self.parent.uic.txt_log.setItem(rows, 0, icon_item)

        time_item = QTableWidgetItem(timing)
        time_item.setForeground(color)
        self.parent.uic.txt_log.setItem(rows, 1, time_item)

        content_item = QTableWidgetItem(to_write)
        content_item.setForeground(color)
        self.parent.uic.txt_log.setItem(rows, 2, content_item)

        self.parent.uic.txt_log.scrollToBottom()
        
    def add_trace_with_question_box(self, title, msg):
        """
            Add a trace to log and show a popup
        """
        ret = QMessageBox.question(self.parent, title, msg, QMessageBox.Yes, QMessageBox.No)
        if ret == QMessageBox.Yes:
            return True
        else:
            return False
    
    def add_trace_with_box(self, msg, scope=OK):
        if scope == OK:
            QMessageBox.information(self.parent, "Information", msg)
        elif scope == WARNING:
            QMessageBox.warning(self.parent, "Warning", msg)
        else:
            QMessageBox.critical(self.parent, "Error", msg)
        self.add_trace(msg, scope)
        
