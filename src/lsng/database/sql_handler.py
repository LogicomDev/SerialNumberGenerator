# -*- coding: utf-8 -*-

# Global imports
# import sqlite3
import MySQLdb
import time
import os

# Local imports
from src.lsng.helpers import singleton, untextify_mac
from src.lsng.database.models import User, Database, GenerationData, GenerationRunBasic


def load_json():
    import json
    with open("database.logicom", "r") as fic:
        data_json = json.loads(fic.read())
    return data_json


def load_summary():
    with open("summary.csv", "r") as fic:
        data_csv = fic.readlines()
    # Removes first item (title)
    data_csv = data_csv[1:]
    return data_csv


@singleton
class SQLHandler(object):
    '''
    classdocs
    '''
    database = None

    def __init__(self):
        '''
        Init the Database and cursor so we can deal with SQL database
        '''
        self.logfile = "query_log.txt"
        self.database = MySQLdb.connect("pma", "Jeremy", "VuLYG7rdDhWrQdeh", "serials")
        self.cursor = self.database.cursor()
        if not self.check_table_presence():
            self.create_table()

    def check_table_presence(self):
        return True

    def exec_cmd(self, cmd):
        if not os.path.exists(self.logfile):
            with open(self.logfile, "w") as fic:
                fic.write("")
        # Do not write the SELECT request or otherwise it'll clog the file quickly
        if not "SELECT" in cmd:
            with open(self.logfile, "a") as fic:
                fic.write(cmd.replace("\t", "").replace("\n", "") + "\n")
        self.cursor.execute(cmd)
        self.database.commit()

    def create_table(self):
        '''
        Create required tables if not present in database
        '''
        # Create the Users table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(\
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,\
            first_name TEXT,\
            last_name TEXT,\
            login TEXT,\
            password TEXT,\
            Level INTERGER,\
            Active BOOLEAN\
        )""")
        self.database.commit()

        # Create the Suppliers table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS suppliers(\
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,\
            name TEXT,\
            code INTERGER,\
            mac_min INTERGER,\
            mac_max INTERGER,\
            created_by INTERGER\          
        )""")
        self.database.commit()

        # Create the Devices table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS devices(\
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,\
            name TEXT,\
            code INTERGER,\
            type INTERGER,\
            tac_number INTERGER,\
            sim_nb INTERGER,\
            wifi BOOLEAN,\
            bt BOOLEAN,\
            supplier INTERGER,\
            created_by INTERGER\
        )""")
        self.database.commit()

        # Create the Updates table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS updates(\
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,\
            device_id INTERGER,\
            po_number TEXT,\
            quantity INTERGER,\
            color TEXT,\
            prod_year INTERGER,\
            prod_week INTERGER,\
            first_serial INTERGER,\
            last_serial INTERGER,\
            first_imei1 INTERGER,\
            last_imei1 INTERGER,\
            first_imei2 INTERGER,\
            last_imei2 INTERGER,\
            first_wifi INTERGER,\
            last_wifi INTERGER,\
            first_bt INTERGER,\
            last_bt INTERGER,\
            date TEXT,\
            created_by INTERGER\
        )""")
        self.database.commit()

    def add_user(self, user_obj, password, level=2):
        # print("Adding user {}".format(user_obj.login))
        cmd = """INSERT INTO users (first_name, last_name, login, password, level, active) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(
            user_obj.first_name, user_obj.last_name, user_obj.login, password, level, True
        )
        self.exec_cmd(cmd)
        user_obj.id = self.cursor.lastrowid
        return user_obj.id

    def is_valid_user(self, login, password):
        cmd = 'SELECT * FROM users where login="{}" and password="{}" and active="True"'.format(login, password)
        self.exec_cmd(cmd)
        return self.cursor.fetchone()
    
    def get_user_id(self, login):
        cmd = 'SELECT * FROM users where login="{}"'.format(login)
        self.exec_cmd(cmd)
        return self.cursor.fetchone()
    
    def get_device_by_id(self, dev_id):
        cmd = 'SELECT * FROM devices where id="{}"'.format(dev_id)
        self.exec_cmd(cmd)
        return self.cursor.fetchone()

    def get_all_generations_from_db(self):
        pass

    def add_new_generation_to_db(self, generation):
        '''
        Add the generation' object' data to the SQL database (so the program knows what have been done before)
        '''
        pass

    def add_supplier(self, supplier_obj, user_obj):
        # print("Adding supplier {}".format(supplier_obj.name))
        cmd = "INSERT INTO suppliers (name, code, mac_min, mac_max, created_by) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
            supplier_obj.name.upper(),
            supplier_obj.code,
            supplier_obj.mac_min,
            supplier_obj.mac_max,
            user_obj.id
        )
        self.exec_cmd(cmd)
        return self.cursor.lastrowid

    def add_device(self, device_obj, supplier_obj, user_obj):
        '''
        Use this method to add a device to the database.
        in : Device (object) : This object contains all the data of a device
        out : last row id (int) : This is the ID (key) of the last inserted device (when successful) 
        '''
        # print("Adding device {}".format(device_obj.name))
        cmd = "INSERT INTO devices (name, code, type, tac_number, sim_nb, wifi, bt, supplier, created_by) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            device_obj.name,
            device_obj.code,
            device_obj.device_type,
            device_obj.base_tac_number,
            device_obj.sim_number,
            device_obj.wifi,
            device_obj.bt,
            supplier_obj.id,
            user_obj.id
        )
        self.exec_cmd(cmd)
        return self.cursor.lastrowid

    def add_generation(self, generation_obj, user_obj):
        # print("Adding a generation for {} - {} - {}".format(generation_obj.supplier.id, generation_obj.device.id, generation_obj.qty))
        cmd = "INSERT INTO updates (\
        device_id, po_number, quantity, color, prod_year, prod_week,\
        first_serial, last_serial, first_imei1, last_imei1, first_imei2, last_imei2,\
        first_wifi, last_wifi, first_bt, last_bt, date, created_by)\
        VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
            generation_obj.device.id,
            generation_obj.po_number,
            generation_obj.qty,
            generation_obj.color,
            generation_obj.prod_year,
            generation_obj.prod_week,
            generation_obj.generated_values[0].serial,
            generation_obj.generated_values[-1].serial,
            generation_obj.generated_values[0].imei_1,
            generation_obj.generated_values[-1].imei_1,
            generation_obj.generated_values[0].imei_2,
            generation_obj.generated_values[-1].imei_2,
            generation_obj.generated_values[0].wifi,
            generation_obj.generated_values[-1].wifi,
            generation_obj.generated_values[0].bt,
            generation_obj.generated_values[-1].bt,
            time.strftime("%d/%m/%Y"),
            user_obj.id
        )
        self.exec_cmd(cmd)

    def read_suppliers(self):
        cmd = """SELECT * FROM suppliers;"""
        self.exec_cmd(cmd)
        db_supplier = self.cursor.fetchall()
        return db_supplier

    def read_devices(self):
        cmd = """SELECT * FROM devices;"""
        self.exec_cmd(cmd)
        db_devices = self.cursor.fetchall()
        return db_devices

    def read_generations_summary(self):
        # Could be written with device_id as a parameter
        cmd = """SELECT * FROM updates;"""
        # cmd = """SELECT * FROM updates where device_id={item};"""
        self.exec_cmd(cmd)
        db_generations = self.cursor.fetchall()
        return db_generations

    def __del__(self):
        '''
        Make sure everything is closed so we can access DB later
        '''
        self.cursor.close()
        self.database.close()
