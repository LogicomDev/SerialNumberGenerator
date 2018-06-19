# -*- coding: utf-8 -*-

import sys
import os
import json
from pathlib import Path

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QObject, pyqtSignal

# Windows imports
from src.lsng.hmi.lsng_hmi import LogicomSerialGenerator
from src.lsng.hmi.login_hmi import Login
from src.lsng.database.sql_handler import SQLHandler
from src.lsng.database.models import User
from mailcap import show


class StdErrHandler(QObject):
    '''
    This class provides an alternate write() method for stderr messages.
    Messages are sent by pyqtSignal to the pyqtSlot in the main window.
    '''
    err_msg = pyqtSignal(str)

    def __init__(self, parent=None):
        QObject.__init__(self)

    def write(self, msg):
        # stderr messages are sent to this method.
        self.err_msg.emit(msg)

# Use this to add a splash screen in case opening the database takes too long !
# class MovieSplashScreen(QSplashScreen):
#
#     def __init__(self, movie, parent=None):
#
#         movie.jumpToFrame(0)
#         pixmap = QPixmap(movie.frameRect().size())
#
#         QSplashScreen.__init__(self, pixmap)
#         self.movie = movie
#         self.movie.frameChanged.connect(self.repaint)
#
#     def showEvent(self, event):
#         self.movie.start()
#
#     def hideEvent(self, event):
#         self.movie.stop()
#
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         pixmap = self.movie.currentPixmap()
#         self.setMask(pixmap.mask())
#         painter.drawPixmap(0, 0, pixmap)
#
#     def sizeHint(self):
#
#         return self.movie.scaledSize()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    sys.excepthook = except_hook
    
    app = QApplication(sys.argv)    

    # Problematic
    db_handler = SQLHandler()
    
    filepath = os.path.join(str(Path.home()), ".lsng_credential.inf")
    show_login = True
    
    if os.path.isfile(filepath):
        with open(filepath, "r") as fic:
            jsondata = json.load(fic)
            
        if jsondata.get("login") and jsondata.get("password"):
            print("found credentials")
            user_data = db_handler.is_valid_user(jsondata.get("login"), jsondata.get("password"))
            if user_data:
                show_login = False
                print("credentials are valid")
                user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[5])
                frame = LogicomSerialGenerator(db_handler, user)
                frame.show()
            else:
                print("credentials doesn't correspond to a defined user")
        else:
            print("Couldn't load the previous credentials because file was damaged")
    
    if show_login:
        print("No existing credentials found")
        login = Login(db_handler)
        if login.exec_() == QDialog.Accepted:
            frame = LogicomSerialGenerator(db_handler, login.user)
            frame.show()

    # # Create the stderr handler and point stderr to it
    # std_err_handler = StdErrHandler()
    # sys.stderr = std_err_handler

    # # Connect err_msg signal to message box method in main window
    # std_err_handler.err_msg.connect(frame.std_err_post)

    try:
        sys.exit(app.exec_())
    except Exception as ex:
        print(ex)
