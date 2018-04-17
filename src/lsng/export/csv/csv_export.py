'''
Created on 5 avr. 2018

@author: Djer
'''
import os
from helpers import textify_mac_from_int
from PyQt5.QtCore import (pyqtSignal)

class CSVHandler(object):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        self.basefolder = os.path.join(parent.basefolder,  "..",  "..", "Traceability")
        self.event_trace = pyqtSignal(str)

    def export_generation(self, generation_obj):
        str_generation = []
        if not os.path.isdir(self.basefolder):
            os.mkdir(self.basefolder)
            
        self.basefolder = os.path.join(self.basefolder, "PO{}".format(generation_obj.po_number))
        if not os.path.isdir(self.basefolder):
            os.mkdir(self.basefolder)

        filename = os.path.join(self.basefolder, "PO{}_{}_{}_{}_{}.csv".format(generation_obj.po_number, generation_obj.supplier.name,
                                                                               generation_obj.device.name, generation_obj.color,
                                                                               generation_obj.qty))
        for generated_sn in generation_obj.generated_values:
            str_generation.append("{}; {}; {}; {}; {}".format(generated_sn.serial,
                                                              generated_sn.imei_1, # Here, IMEIs needs to be full (TAC + serial + luhn checksum)
                                                              generated_sn.imei_2,
                                                              textify_mac_from_int(generated_sn.wifi).upper(), # Here, MAC adress needs to be written with dashes
                                                              textify_mac_from_int(generated_sn.bt).upper()
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
