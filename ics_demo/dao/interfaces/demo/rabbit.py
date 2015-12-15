from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.demo import Rabbit

from ics_demo.helpers import uuidgen

def get_all():
    return base.class_get_all_to_dict(Rabbit)

def get_one(uuid):
    return base.class_get_one_by_uuid_to_dict(Rabbit, uuid)

def get_obj(uuid):
    return base.class_get_one_by_uuid_to_obj(Rabbit, uuid)

def get_obj_by_ID(ID):
    return base.class_get_one_by_ID_to_obj(Rabbit, ID)

def get_keys():
    return base.class_get_keys(Rabbit)

def save(post_dict):
    name = post_dict['name']
    return Rabbit(uuid=uuidgen(), name=name)
