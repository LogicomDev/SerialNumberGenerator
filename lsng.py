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
import logging
from logging.handlers import RotatingFileHandler
from hmi.lsng_hmi import lsng_logger


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
    logging.critical(str(exception))


def set_logger(sys_args):
    if "-d" in sys_args:
        level=logging.DEBUG
    else:
        level=logging.WARNING
    print("set_logger")
    # création de l'objet logger qui va nous servir à écrire dans les logs
    lsng_logger = logging.getLogger()
    # on met le niveau du logger à DEBUG, comme ça il écrit tout
    lsng_logger.setLevel(logging.DEBUG)
     
    # création d'un formateur qui va ajouter le temps, le niveau
    # de chaque message quand on écrira un message dans le log
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    # création d'un handler qui va rediriger une écriture du log vers
    # un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
    file_handler = RotatingFileHandler(os.path.join(os.path.expanduser("~"), 'lsng_activity.log'), 'a', 10000000, 1)
    # on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
    # créé précédement et on ajoute ce handler au logger
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    lsng_logger.addHandler(file_handler)
     
    # création d'un second handler qui va rediriger chaque écriture de log sur la console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    lsng_logger.addHandler(stream_handler)
    return lsng_logger

sys.excepthook = except_hook

if __name__ == '__main__':
    lsng_logger = set_logger(sys.argv)
    app = QApplication(sys.argv)    

    db_handler = SQLHandler()
    
    filepath = os.path.join(str(Path.home()), ".lsng_credential.inf")
    show_login = True    

    if os.path.isfile(filepath):
        with open(filepath, "r") as fic:
            jsondata = json.load(fic)
            
        if jsondata.get("login") and jsondata.get("password"):
            lsng_logger.debug("Existing credentials found")
            user_data = db_handler.is_valid_user(jsondata.get("login"), jsondata.get("password"))
            if user_data:
                show_login = False
                lsng_logger.debug("Credentials are valid")
                user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[5])
                frame = LogicomSerialGenerator(db_handler, user, lsng_logger)
                frame.show()
            else:
                lsng_logger.error("Saved credentials doesn't match to a defined user")
        else:
            lsng_logger.error("Couldn't load the previous credentials because file was damaged")
    
    if show_login:
        lsng_logger.info("No existing credentials found.")
        login = Login(db_handler)
        if login.exec_() == QDialog.Accepted:
            frame = LogicomSerialGenerator(db_handler, login.user, lsng_logger)
            frame.show()

    sys.exit(app.exec_())
