'''
Created on 18 mars 2018

@author: Djer
'''


def singleton(cls):
    instance = None

    def ctor(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return ctor


def untextify_mac(mac_address):
    return int(mac_address.replace(":", "").replace("-", ""), 16)


def i2mac(value, mac_seperator=":"):
    '''
    Turns a int value to a XX-XX-XX-XX-XX MAC address
    '''
    if value:
        return textify_mac("{:012X}".format(value), mac_seperator=mac_seperator)
    else:
        return "None"


def textify_mac(digistring, blocksize=2, mac_seperator=":"):
    '''
    Formats a mac address (a int written as a String)
    '''
    if digistring and digistring != "None":
        toto = [digistring[i:i + blocksize] for i in range(0, len(digistring), blocksize)]
        return mac_seperator.join(toto)
    else:
        return "-"


def to_bool(value):
    if value in ["True", "true", "t", "T"]:
        return True
    else:
        return False
