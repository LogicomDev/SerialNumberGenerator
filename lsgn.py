# -*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QObject, pyqtSignal

# Windows imports
from src.lsng.hmi.lsgn_hmi import LogicomSerialGenerator
from src.lsng.hmi.login_hmi import Login
from src.lsng.database.sql_handler import SQLHandler


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

if __name__ == '__main__':
    app = QApplication(sys.argv)    

    # Problematic
    db_handler = SQLHandler(os.path.join(os.getcwd(), "logicom_database.db"))

    # for debug only
    # from src.lsng.database.models import User
    # frame = LogicomSerialGenerator(db_handler, User(0, "Jeremy", "Marchal", "Admin", 0))  # For debug only
    # frame.show()
    # Fin debug

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
