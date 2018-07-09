'''
Created on 22 nov. 2017

@author: Djer
'''
# Global imports
import enum
from netaddr import EUI, AddrFormatError
from luhn import append as luhn_append

# Local imports
from src.lsng.helpers import singleton, to_bool, i2mac, untextify_mac
from enum import Enum


class DeviceType(Enum):
    FEAT_PHONE = 0
    SMARTPHONE = 1
    TABLET = 2
    OTHER = 3


class User(object):

    def __init__(self, db_id, first_name, last_name, login, level):
        self.id = db_id
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        # password is ignored
        self.level = level

    def __str__(self):
        return '{} {} {} {} {}'.format(
            self.id,
            self.first_name,
            self.last_name,
            self.login,
            self.level
        )


class MACAdress(object):
    # Code helper to increase code readability

    def __init__(self, value):
        if isinstance(value, EUI):
            # If MAC adress is already an EUI class, turns it into an integer
            self.value = int(value)
        else:
            # Otherwise store it directly
            self.value = int(EUI(value))

    def __eq__(self, other):
        # For '==' operations
        return other == self.value

    def __add__(self, other):
        if isinstance(other, MACAdress):
            return self.value + other.value
        return self.value + other

    def __sub__(self, other):
        if isinstance(other, MACAdress):
            return self.value - other.value
        return self.value - other

    def __str__(self, *args, **kwargs):
        # Displays the xx-xx-xx-xx-xx format
        return str(EUI(self.value))

    def __repr__(self):
        return self.value


class GenerationRunBasic(object):

    def __init__(self, supplier, device, po_number, color, prod_week, prod_year, run_qty):
        # This is a list of GenerationData objects
        self.generated_values = []
        # Attributes
        self.supplier = supplier
        self.device = device
        self.po_number = po_number
        self.color = color
        self.prod_week = prod_week
        self.prod_year = prod_year
        self.qty = run_qty

    def __repr__(self, *args, **kwargs):
        return str(self.generated_values)


class GenerationData(object):

    def __init__(self):
        self.serial = None
        self.imei_1 = None
        self.imei_2 = None
        self.bt = None
        self.wifi = None

    def __repr__(self, *args, **kwargs):
        return "{} - {} - {} - {} - {}".format(self.serial, self.imei_1, self.imei_2, i2mac(self.wifi), i2mac(self.bt))


@singleton
class Database(object):

    def __init__(self):
        self.suppliers = {}

    def add_supplier(self, supplier_name, supplier_code, mac_min, mac_max, db_id=None):
        if not self.suppliers.get(supplier_name):
            # Supplier not already created
            supplier = Supplier(supplier_name, supplier_code, mac_min, mac_max, db_id)
            self.suppliers[supplier_name] = supplier
            return supplier

        return self.suppliers[supplier_name]

    def get_supplier(self, supplier_name):
        return self.suppliers.get(supplier_name)

    def get_suppliers(self):
        return self.suppliers

    def get_supplier_by_id(self, id_to_find):
        for supplier in self.suppliers.values():
            if supplier.id == id_to_find:
                return supplier
        return None

    def get_device(self, device_name):
        for supplier in self.suppliers.values():
            for device in supplier.devices.values():
                if device.name == device_name:
                    return device
        return None

    def get_device_by_id(self, id_to_find):
        for supplier in self.suppliers.values():
            for device in supplier.devices.values():
                if device.id == id_to_find:
                    return device
        return None

    def __repr__(self):
        return str(self.suppliers)


class Supplier(object):

    def __init__(self, name, code, mac_min, mac_max, db_id=None):
        self.id = 0  # From database
        self.name = name
        self.code = code
        self.mac_min = untextify_mac(mac_min) if mac_min else 0
        self.mac_max = untextify_mac(mac_max) if mac_max else 200000
        self.mac_last = self.mac_min
        self.id = db_id
        self.devices = {}

    def get_device(self, device_name):
        return self.devices.get(device_name)

    @property
    def mac_max(self):
        return self._mac_max

    @mac_max.setter
    def mac_max(self, value):
        if value == self.mac_min:
            raise ValueError("Max MAC adress can't equal to Min MAC")
        else:
            self._mac_max = value

    def get_devices(self):
        return self.models

    def update_mac_max(self, value):
        if value:
            self.mac_max = self.mac_max + value
            return self.mac_max
        raise ValueError("Please enter a value bigger than 0")

    def add_device(self, device_name, device_code, base_imei_tac_number, sim_number, wifi_connectivity, bt_connectivity, device_type=DeviceType.SMARTPHONE, db_id=None):
        if not self.devices.get(device_name):
            device = Device(device_name, int(device_code), int(base_imei_tac_number), int(sim_number), to_bool(wifi_connectivity), to_bool(bt_connectivity), int(device_type), db_id)
            self.devices[device_name] = device
            return device
        return self.devices[device_name]

    def add_generation(self, data_tuple):
        mac_last = self.mac_min
        if data_tuple[15] and str(data_tuple[15]).isdigit():
            mac_last = int(data_tuple[15])
        elif data_tuple[13] and str(data_tuple[13]).isdigit():
            mac_last = int(data_tuple[13])
        else:
            mac_last = 0

        if self.mac_min <= mac_last <= self.mac_max and mac_last > self.mac_last:
            self.mac_last = mac_last

    def get_mac_address_left(self):
        return self.mac_max - self.mac_last

    def check_enough_mac_adress(self, quantity, device):
        # Returns true if remaining MAC adress number is bigger than requested quantity
        if device.wifi and device.bt :
            # Si WIFI et BT alors on a besoin du double d'addresses
            return (self.get_mac_address_left() - (2 * quantity)) >= 0
        else:
            return (self.get_mac_address_left() - quantity) >= 0

    def __repr__(self, *args, **kwargs):
        return str(self.devices)


class Device(object):

    def __init__(self, name, code, base_tac_number, sim_number, wifi, bt, device_type=DeviceType.SMARTPHONE, db_id=None):
        self.id = 0  # From database
        self.name = name
        self.code = code
        self.base_tac_number = base_tac_number
        self.device_type = device_type
        self.sim_number = sim_number
        self.wifi = wifi
        self.bt = bt
        self.base_serial = 0
        self.last_serial = 0
        self.last_imei = 0
        self.id = int(db_id) if db_id else None
        self.previous_generation = {}

    def check_enough_imeis_adress(self, size=0):
        # Returns True if num_imei + qty < 1000000; otherwise returns False
        if self.sim_number == 1 :
            return (self.last_imei + size) < 1000000
        elif self.sim_number == 2:
            return (self.last_imei + (2 * size)) < 1000000
        else:
            return True

    def get_imei_left(self):
        return 1000000 - self.get_last_imei()

    def get_base_tac(self):
        return int(str(self.base_tac_number) + "000000")

    def set_device_type(self, dev_type):
        if dev_type == "Smartphone":
            self.device_type = DeviceType.SMARTPHONE
        elif dev_type == "Tablet":
            self.device_type = DeviceType.TABLET
        elif dev_type == "Feature Phone":
            self.device_type = DeviceType.FEAT_PHONE
        else:
            print("Unknown device type: {}".format(dev_type))

    def add_generation(self, data_tuple):
        '''
            Add previous generation informations
        '''
        year = data_tuple[4]
        week = data_tuple[5]
        self.previous_generation.setdefault("last_serial", {})
        self.previous_generation["last_serial"].setdefault(year, {})
        self.previous_generation["last_serial"][year].setdefault(week, 0)

        # Check that SN are increasing in values
        if int(str(data_tuple[7])[8:]) > self.previous_generation["last_serial"][year][week]:
            self.previous_generation["last_serial"][year][week] = int(str(data_tuple[7])[8:])

        if data_tuple[11] and self.sim_number > 0:
            # Check that IMEIs are increasing in values
            if int(str(data_tuple[11])[8:-1]) > self.previous_generation.get("last_imei", 0):
                self.previous_generation["last_imei"] = int(str(data_tuple[11])[8:-1])
        else:
            self.previous_generation["last_imei"] = None

    def get_previous_generation_for_date(self, year, week):
        if self.previous_generation.get("last_serial", {}).get(year):
            return self.previous_generation["last_serial"][year].get(week)
        return None

    def get_last_imei(self):
        value = self.previous_generation.get("last_imei", 0)
        if value:
            return value
        else:
            return 0

    def __repr__(self, *args, **kwargs):
        return "Name:{0}, Code:{1:02}, Base TAC:{2}, type:{3}, SIM:{4}, Wifi:{5}, BT:{6}, last_serial:{7:04}".format(self.name, self.code, self.base_tac_number, self.device_type, self.sim_number, self.wifi, self.bt, self.last_serial)


if __name__ == '__main__':
    db = Database()
    a = db.add_supplier("yolo", 42, 0xDC783406D3A1, 0xDC7834088888, 0xDC783407B374)
    b = a.add_device("toto", 7, 35908507)
    print(a)
    print(b)
    print(db)
    run = GenerationRun("yolo", "toto", "001", "Biteuh", 20, 16, 10)
    run.generate()
    print("1736750900001 - 353441082546515 - 353441082628115 - DC7834683FD6 - DC783468535E")
    print(run.get_results())
