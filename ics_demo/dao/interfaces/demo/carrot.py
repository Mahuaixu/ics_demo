from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.demo import Carrot

from ics_demo.helpers import uuidgen

def get_all():
    return base.class_get_all_to_dict(Carrot)

def get_one(uuid):
    return base.class_get_one_by_uuid_to_dict(Carrot, uuid)

def get_obj(uuid):
    return base.class_get_one_by_uuid_to_obj(Carrot, uuid)

def get_obj_by_ID(ID):
    return base.class_get_one_by_ID_to_obj(Carrot, ID)

def get_keys():
    return base.class_get_keys(Carrot)

def save(post_dict):
    name = post_dict['name']
    rabbit = post_dict['rabbit']
    return Carrot(uuid=uuidgen(), name=name, rabbit=rabbit)
