'''
Created on 5 avr. 2018

@author: Djer
'''

from PyQt5.QtCore import (QThread, pyqtSignal)

from luhn import append as luhn_append

from src.lsng.database.models import GenerationData


class NoMoreMACAdressAvailable(Exception):
    pass


class NoMoreIMEIAdressAvailable(Exception):
    pass


class NoMoreSerialAvailable(Exception):
    pass


class GenerationHandler(QThread):
    '''
    This class is a threaded-class that is designed to handle the computation of serial, IMEIs and MACs generations.
    This is a thread to be able to be able to follow the progress and to not block the main HMI 
    '''

    event_trace = pyqtSignal(str)
    event_errors = pyqtSignal(str)
    session_progression = pyqtSignal(int)
    session_finished = pyqtSignal()

    def __init__(self, parent):
        super(GenerationHandler, self).__init__(parent)
        # This is a list of GenerationData objects
        self.generated_values = []
        # Attributes
        self.supplier = None
        self.device = None
        self.po_number = None
        self.color = None
        self.prod_week = None
        self.prod_year = None
        self.qty = None

    def load_values(self, supplier, device, po_number, color, prod_week, prod_year, run_qty):
        self.supplier = supplier
        self.device = device
        self.po_number = po_number
        self.color = color
        self.prod_week = prod_week
        self.prod_year = prod_year
        self.qty = run_qty
        self.last_mac = 0
        self.last_imei = 0
        self.last_serial = 0

        if not self.supplier.check_enough_mac_adress(self.qty):
            raise NoMoreMACAdressAvailable

        if not self.device.check_enough_imeis_adress(self.qty):
            raise NoMoreIMEIAdressAvailable

    def run(self):
        '''
        Main function of class.
        Called when calling GenerationHandler.start() in main thread
        '''
        serial_base = int("{:02}{:02}{:02}{:02}{:05}".format(self.prod_year, self.prod_week, self.supplier.code, self.device.code, 0))
        self.last_serial = self.device.get_previous_generation_for_date(self.prod_year, self.prod_week)
        self.last_imei = self.device.get_last_imei()

        # If retrieving data from database was unsuccessful... we reset the settings ! (means we didn't had any input before)
        if self.last_serial is None:
            self.last_serial = 0
        if self.last_imei is None:
            self.last_imei = 0

        # Prerequisite are OK, so here we go !
        for idx in range(self.qty):
            self.session_progression.emit(idx)
            current_generation = GenerationData()
            #SIM = SIM_BASE + Last_Gen + current_order_position
            current_generation.serial = serial_base + self.last_serial + idx + 1
            if len(str(current_generation.serial)) != 13:
                self.event_errors.emit("Wrong SERIAL SIZE ! Found {} char instead of 13. Please contact admin.".format(len(str(current_generation.serial))))
                return

            # IMEIs calculation
            if self.device.sim_number == 1:
                current_generation.imei_1 = int(luhn_append(str(self.device.get_base_tac() + self.last_imei + idx + 1)))
                if len(str(current_generation.imei_1)) != 15:
                    self.event_errors.emit("Wrong IMEI SIZE ! Found {} char instead of 16.  Please contact admin.".format(len(str(current_generation.imei_1))))
                    return
            elif self.device.sim_number == 2:
                current_generation.imei_1 = int(luhn_append(str(self.device.get_base_tac() + self.last_imei + idx + 1)))
                current_generation.imei_2 = int(luhn_append(str(self.device.get_base_tac() + self.last_imei + idx + self.qty + 1)))
                if len(str(current_generation.imei_1)) != 15:
                    self.event_errors.emit("Wrong IMEI SIZE ! Found {} char instead of 16.  Please contact admin.".format(len(str(current_generation.imei_1))))
                    return

            # MACs calculation
            if self.device.wifi and self.device.bt:
                current_generation.wifi = self.supplier.mac_last + idx + 1
                current_generation.bt = self.supplier.mac_last + self.qty + idx + 1
            elif self.device.wifi and not self.device.bt:
                current_generation.wifi = self.supplier.mac_last + idx + 1
            elif not self.device.wifi and self.device.bt:
                current_generation.bt = self.supplier.mac_last + idx + 1

            self.event_trace.emit(str(current_generation))
            self.generated_values.append(current_generation)
        # Safely returns control to Qt
        self.session_progression.emit(self.qty)
        self.session_finished.emit()

    def get_results(self):
        ret_dict = {}
        ret_dict["supplier"] = self.supplier
        ret_dict["device"] = self.device
        ret_dict["po_number"] = self.po_number
        ret_dict["color"] = self.color
        ret_dict["prod_week"] = self.prod_week
        ret_dict["prod_year"] = self.prod_year
        ret_dict["qty"] = self.qty
        ret_dict["values"] = self.generated_values
        return ret_dict

    def __repr__(self, *args, **kwargs):
        return str(self.generated_values)
