'''
Created on 5 avr. 2018

@author: Djer
'''
import os
from src.lsng.helpers import i2mac
from PyQt5.QtCore import (pyqtSignal)

class CSVHandler(object):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        self.event_trace = pyqtSignal(str)
        self.file_extension = "csv"

    def export_generation(self, filename, generation_obj, seperator):
        str_generation = []
            
        for generated_sn in generation_obj.generated_values:
            str_generation.append("{}; {}; {}; {}; {}".format(generated_sn.serial,
                                                              generated_sn.imei_1, # Here, IMEIs needs to be full (TAC + serial + luhn checksum)
                                                              generated_sn.imei_2,
                                                              i2mac(generated_sn.wifi, seperator).upper(), # Here, MAC adress needs to be written with dashes
                                                              i2mac(generated_sn.bt, seperator).upper()
                                                              )
                                  )

        with open(filename, "w") as fic:
            fic.write("PO NUMBER;{}\n".format(generation_obj.po_number))
            fic.write("SUPPLIER:;{}\n".format(generation_obj.supplier.name))
            fic.write("MODEL:;{}\n".format(generation_obj.device.name))
            fic.write("COLOR:;{}\n".format(generation_obj.color))
            fic.write("QTY:;{}\n".format(generation_obj.qty))
            fic.write("SERIAL NUMBER;IMEI SIM 1;IMEI SIM 2;WIFI MAC ADDRESS;BT ADDRESS\n")
            fic.write("\n".join(str_generation))
            fic.write("\n")
            fic.write("---;END;OF THE;LIST;---")
            
        return os.path.normpath(filename)
