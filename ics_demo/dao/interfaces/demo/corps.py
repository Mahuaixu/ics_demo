from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.demo import Carrot, Rabbit, Corps

from ics_demo.helpers import uuidgen

def get_all():
    return base.class_get_all_to_dict(Corps)

def get_one(uuid):
    return base.class_get_one_by_uuid_to_dict(Corps, uuid)

def get_obj(uuid):
    return base.class_get_one_by_uuid_to_obj(Corps, uuid)

def get_obj_by_ID(ID):
    return base.class_get_one_by_ID_to_obj(Corps, ID)

def get_keys():
    return base.class_get_keys(Corps)
