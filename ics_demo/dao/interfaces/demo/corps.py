from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.demo import Carrot, Rabbit, Corps

from ics_demo.helpers import uuidgen

def get_all():
    return base.get_all_by_class(Corps)

def get_one(identifier):
    return base.get_one_by_class(Corps, identifier)

def get_obj(identifier):
    return base.get_obj_by_class(Corps, identifier)

def get_keys():
    return base.get_keys_by_class(Corps)
