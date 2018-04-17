'''
Created on 22 nov. 2017

@author: Djer
'''

import os
import json


class CSVHandler(object):

    def __init__(self):
        self.path = None
        self.read_data = None

    def get_file_path(self):
        return self.path

    def parse(self, filepath):  
        """ take a CSV filepath as input,
        Parse it,
        then returns a dict with all the values read
        """
        self.path = filepath

        data = {}

        if not os.path.exists(self.path):
            return

        with open(self.path, "r") as fic:
            previous_results = fic.readlines()

        previous_results.pop(0)
        for line in previous_results:
            items = line.strip().replace("-", "").replace('"', "").replace('=', "").split(";")
            parsed_line_data = {"previous_run": {}}

            if items == ['']:
                # Avoid empty lines
                continue

            parsed_line_data["type"] = items[0]
            parsed_line_data["po_number"] = items[1]
            parsed_line_data["supplier"] = items[2]
            parsed_line_data["model"] = items[3]
            parsed_line_data["prod_date"] = items[4]
            parsed_line_data["color"] = items[5]
            parsed_line_data["qty"] = items[6]
            parsed_line_data["first_sn"] = items[7][8:]
            parsed_line_data["last_sn"] = items[8][8:]

            if items[9] in ["-", "", "None"]:
                parsed_line_data["first_imei1"] = None
            else:
                parsed_line_data["first_imei1"] = items[9][8:-1]

            if items[10] in ["-", "", "None"]:
                parsed_line_data["last_imei1"] = None
            else:
                parsed_line_data["last_imei1"] = items[10][8:-1]

            if items[11] in ["-", "", "None"]:
                parsed_line_data["first_imei2"] = None
            else:
                parsed_line_data["first_imei2"] = items[11][8:-1]

            if items[12] in ["-", "", "None"]:
                parsed_line_data["last_imei2"] = None
            else:
                parsed_line_data["last_imei2"] = items[12][8:-1]

            if items[13] in ["-", "", "None"]:
                parsed_line_data["first_mac_wifi"] = None
            else:
                parsed_line_data["first_mac_wifi"] = items[13]

            if items[14] in ["-", "", "None"]:
                print(items[3])
                parsed_line_data["last_mac_wifi"] = None
            else:
                print("---->" + items[3])
                parsed_line_data["last_mac_wifi"] = items[14]

            if items[15] in ["-", "", "None"]:
                parsed_line_data["first_bt_mac"] = None
            else:
                parsed_line_data["first_bt_mac"] = items[15]

            if items[16] in ["-", "", "None"]:
                parsed_line_data["last_bt_mac"] = None
            else:
                parsed_line_data["last_bt_mac"] = items[16]

            # Stores all the runs and the last sn given for this device
            parsed_line_data["previous_run"][items[4]] = items[8][8:]

            data[items[3]] = parsed_line_data
        return data

    def write_result(self, filepath, run_result):
        self.log_info("Preparing to update Summary...")

        if not os.path.exists(filepath):
            with open(filepath, "w") as fic:
                fic.write("Type;PO number; Supplier; Model; Prod Date; Color; Qty; First SN; Last SN; First IMEI1; Last IMEI1; First IMEI2; Last IMEI2; First WIFI MAC; Last WIFI MAC; First BT MAC; Last BT MAC\n")

        with open(filepath, "a") as fic:
            fic.write(run_result.serialize())

        print("Summary succesfully updated")


class JSONHandler(object):

    def __init__(self):
        self.path = None
        self.data = {}

    def get_file_path(self):
        return self.path

    def load_from_path(self, filepath):
        self.log_info("Loading database...")
        if os.path.isfile(self.config_db_path):
            with open(self.config_db_path, "r") as fic:
                self.data = json.load(fic)
                print("Loading finished.")
                return self.data
        else:
            raise ValueError("No database in file yet. Please create one in the database windows.")

    def write_data(self, data):
        with open(self.path, "w") as fic:
            fic.write(data)

        self.data = data

