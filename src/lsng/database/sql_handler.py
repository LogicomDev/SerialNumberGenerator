# -*- coding: utf-8 -*-

# Global imports
import sqlite3
import time
import os

# Local imports
from src.lsng.helpers import singleton, untextify_mac
from src.lsng.database.models import User, Database, GenerationData, GenerationRunBasic

DATABASE_NAME = "logicom_database.db"


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

    def __init__(self, database_path=DATABASE_NAME):
        '''
        Init the Database and cursor so we can deal with SQL database
        '''
        self.logfile = "query_log.txt"
        self.database = sqlite3.connect(database_path)
        self.cursor = self.database.cursor()
        if not self.check_table_presence():
            self.create_table()

    def check_table_presence(self):
        return True

    def exec_cmd(self, cmd):
        if not os.path.exists(self.logfile):
            with open(self.logfile, "w") as fic:
                fic.write("")
            
        with open(self.logfile, "a") as fic:
            fic.write(cmd.replace("\t","").replace("\n","") + "\n")
        self.cursor.execute(cmd)
        self.database.commit()

    def create_table(self):
        '''
        Create required tables if not present in database
        '''
        # Create the Users table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            first_name TEXT,
            last_name TEXT,
            login TEXT,
            password TEXT,
            Level INTERGER,
            Active BOOLEAN
        )""")
        self.database.commit()

        # Create the Suppliers table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS suppliers(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT,
            code INTERGER,
            mac_min INTERGER,
            mac_max INTERGER,
            created_by INTERGER          
        )""")
        self.database.commit()

        # Create the Devices table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS devices(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT,
            code INTERGER,
            type INTERGER,
            tac_number INTERGER,
            sim_nb INTERGER,
            wifi BOOLEAN,
            bt BOOLEAN,
            supplier INTERGER,
            created_by INTERGER
        )""")
        self.database.commit()

        # Create the Updates table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS updates(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            device_id INTERGER,
            po_number TEXT,
            quantity INTERGER,
            color TEXT,
            prod_year INTERGER,
            prod_week INTERGER,
            first_serial INTERGER,
            last_serial INTERGER,
            first_imei1 INTERGER,
            last_imei1 INTERGER,
            first_imei2 INTERGER,
            last_imei2 INTERGER,
            first_wifi INTERGER,
            last_wifi INTERGER,
            first_bt INTERGER,
            last_bt INTERGER,
            date TEXT,
            created_by INTERGER
        )""")
        self.database.commit()

    def add_user(self, user_obj, password, level=2):
        #print("Adding user {}".format(user_obj.login))
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
        #print("Adding supplier {}".format(supplier_obj.name))
        cmd = """INSERT INTO suppliers (name, code, mac_min, mac_max, created_by) VALUES ('{}', '{}', '{}', '{}', '{}')""".format(
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
        #print("Adding device {}".format(device_obj.name))
        cmd = """INSERT INTO devices (name, code, type, tac_number, sim_nb, wifi, bt, supplier, created_by) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
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
        #print("Adding a generation for {} - {} - {}".format(generation_obj.supplier.id, generation_obj.device.id, generation_obj.qty))
        cmd = """INSERT INTO updates (
        device_id, po_number, quantity, color, prod_year, prod_week,
        first_serial, last_serial, first_imei1, last_imei1, first_imei2, last_imei2,
        first_wifi, last_wifi, first_bt, last_bt, date, created_by)
        VALUES ('{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
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
        cmd = """SELECT * FROM updates;"""
        self.exec_cmd(cmd)
        db_generations = self.cursor.fetchall()
        return db_generations

    def __del__(self):
        '''
        Make sure everything is closed so we can access DB later
        '''
        self.cursor.close()
        self.database.close()


def test_create_db_from_previous_file_formats():
    user_obj = None
    
    if os.path.exists(DATABASE_NAME):
        os.remove(DATABASE_NAME)
    if os.path.exists("query_log.txt"):
        os.remove("query_log.txt")

    handler = SQLHandler()
    handler.create_table()

    with open("user_list.txt", "r") as fic:
        users = fic.readlines()
    for user in users:
        user_data = user.replace('/t', '').replace('"', '').split(";")
        user_tmp_obj = User(0, user_data[0], user_data[1], user_data[2], user_data[4])
        if user_obj is None:
            user_obj = user_tmp_obj
        handler.add_user(user_tmp_obj, user_data[3])

    db = Database()

    load_json()
    load_summary()

    start = time.time()
    print("Starting Supplier/devices importation")
    for supplier_name, supplier_data in load_json().items():
        supp_obj = db.add_supplier(
            supplier_name,
            supplier_data.get("supplier_id"),
            supplier_data.get("mac_min"),
            supplier_data.get("mac_max")
        )
        supp_obj.id = handler.add_supplier(supp_obj, user_obj)
        for device_name, device_data in supplier_data.get("models", {}).items():
            dev_obj = supp_obj.add_device( # device_name, device_code, base_imei_tac_number, sim_number, wifi_connectivity, bt_connectivity
                device_name,
                device_data.get("model_id"),
                device_data.get("base_imei"),
                0,
                False,
                False
            )
            
            if device_data.get("model_type") is None and "TAB" in device_name:
                dev_obj.set_device_type("Tablet")
            else:
                if device_data.get("model_type") == "Feature Phone":
                    dev_obj.set_device_type("Feature Phone")
                else:
                    dev_obj.set_device_type("Smartphone")

            if device_data.get("connectivity") == "BT ONLY":
                dev_obj.bt = True
                dev_obj.wifi = False
            elif device_data.get("connectivity") == "WIFI ONLY":
                dev_obj.bt = False
                dev_obj.wifi = True
            elif device_data.get("connectivity") == "WIFI + BT":
                dev_obj.bt = True
                dev_obj.wifi = True
            
            if device_data.get("bluetooth"):
                dev_obj.bt = True
            
            if device_data.get("sim_nb") == "2 SIM":
                dev_obj.sim_number = 2
            elif device_data.get("sim_nb") == "2 SIM":
                dev_obj.sim_number = 1

            dev_obj.id = handler.add_device(dev_obj, supp_obj, user_obj)
    print("Importation of Supplier/devices database took %ds" % (time.time() - start))

    start = time.time()
    print("Starting Updates importation")
    for update in load_summary():
        data = update.replace("=", "").replace('"', '').replace("\n", "").split(";")
        summary_run = GenerationRunBasic(Database().get_supplier(data[2]),
                                        Database().get_supplier(data[2]).get_device(data[3]),
                                        data[1],
                                        data[5],
                                        data[4][-2:],
                                        data[4][2:4],
                                        data[6])
        # ---
        first_gen = GenerationData()
        first_gen.serial = data[7]
        first_gen.imei_1 = data[9] if len(data[9]) > 12 else ""
        first_gen.imei_2 = data[11] if len(data[11]) > 12 else ""
        first_gen.wifi = untextify_mac(data[13]) if data[13] != "-" else ""
        first_gen.bt = untextify_mac(data[15]) if data[15] != "-" else ""
        # ---
        last_gen = GenerationData()
        last_gen.serial = data[8] if data[8] != data[7] else data[7] + data[6]
        last_gen.imei_1 = data[10] if len(data[10]) > 12 else ""
        last_gen.imei_2 = data[12] if len(data[12]) > 12 else ""
        last_gen.wifi = untextify_mac(data[14]) if data[14] != "-" else ""
        last_gen.bt = untextify_mac(data[16]) if data[16] != "-" else ""   
        summary_run.generated_values = [first_gen, last_gen]
        handler.add_generation(summary_run, user_obj)

    print("Importation of Updates database took %ds" % (time.time() - start))


def test_reading_from_sql():
    user_obj = User("admin", "admin", "admin", "admin", 0)

    handler = SQLHandler()
    handler.create_table()
    db = Database()

    start = time.time()
    suppliers = handler.read_suppliers()
    for supplier in suppliers:
        db_sup = db.add_supplier(supplier[1], supplier[2], supplier[3], supplier[4], supplier[0])
    print("Reading supplier database took %ds" % (time.time() - start))

    start = time.time()
    devices = handler.read_devices()
    for device in devices:
        db_sup = db.get_supplier_by_id(device[8])
        db_sup.add_device(device[1], device[2], device[4], device[3], device[5], device[6], device[7], device[0])
    print("Reading devices database took %ds" % (time.time() - start))

    start = time.time()
    generations = handler.read_generations_summary()
    for generation in generations:
        print(db.get_device_by_id(generation[1]))
        # TODO: Add the generation results to the object (so the last imei/macs are up to date)
        # To do so, create a dict with prod/week and update it's value foreach time we encounter it
    print("Reading updates database took %ds" % (time.time() - start))
    print(db)   

if __name__ == '__main__':
    test_create_db_from_previous_file_formats()
    # test_reading_from_sql()
