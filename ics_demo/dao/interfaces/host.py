from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.host import Host

from ics_demo.helpers import uuidgen

def get_all():
    return base.get_all_by_class(Host)

def get_one(identifier):
    return base.get_one_by_class(Host, identifier)

def get_obj(identifier):
    return base.get_obj_by_class(Host, identifier)

def get_keys():
    return base.get_keys_by_class(Host)

def save(properties_dict):
    name = properties_dict['name']
    ipaddr = properties_dict['ipaddr']
    initialized = properties_dict['initialized']
    return Host(uuid=uuidgen(), name=name, ipaddr=ipaddr, initialized=initialized)
