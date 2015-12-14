from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.demo import Rabbit

from ics_demo.helpers import uuidgen

def get_all():
    return base.get_all_by_class(Rabbit)

def get_one(identifier):
    return base.get_one_by_class(Rabbit, identifier)

def get_obj(identifier):
    return base.get_obj_by_class(Rabbit, identifier)

def get_keys():
    return base.get_keys_by_class(Rabbit)

def save(post_dict):
    name = post_dict['name']
    return Rabbit(uuid=uuidgen(), name=name)
