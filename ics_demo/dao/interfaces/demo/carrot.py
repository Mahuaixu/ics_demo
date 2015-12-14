from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.demo import Carrot

from ics_demo.helpers import uuidgen

def get_all():
    return base.get_all_by_class(Carrot)

def get_one(identifier):
    return base.get_one_by_class(Carrot, identifier)

def get_obj(identifier):
    return base.get_obj_by_class(Carrot, identifier)

def get_keys():
    return base.get_keys_by_class(Carrot)

def save(post_dict):
    name = post_dict['name']
    rabbit = post_dict['rabbit']
    return Carrot(uuid=uuidgen(), name=name, rabbit=rabbit)
