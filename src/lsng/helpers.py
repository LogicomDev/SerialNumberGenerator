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

def i2mac(value):
    '''
    Turns a int value to a XX-XX-XX-XX-XX MAC address
    '''
    if value:
        return textify_mac("{:012X}".format(value))
    else:
        return ""

def textify_mac_from_int(intvalue):
    if intvalue:
        return textify_mac("{:x}".format(intvalue))
    else:
        return "-"

def textify_mac(digistring, blocksize=2):
    if digistring and digistring!="None":
        toto = [digistring[i:i + blocksize] for i in range(0, len(digistring), blocksize)]
        return ":".join(toto)
    else:
        return "-"

def to_bool(value):
    if value in ["True", "true", "t", "T"]:
        return True
    else:
        return False
