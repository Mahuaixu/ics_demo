from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.vsan import Osd

from ics_demo.helpers import uuidgen

def get_all():
    return base.class_get_all_to_dict(Osd)


def get_one(uuid):
    return base.class_get_one_by_uuid_to_dict(Osd, uuid)


def get_obj(uuid):
    return base.class_get_one_by_uuid_to_obj(Osd, uuid)


def get_obj_by_ID(ID):
    return base.class_get_one_by_ID_to_obj(Osd, ID)


def get_keys():
    return base.class_get_keys(Osd)


def save(post_dict):
    #record_id = post_dict['id']
    name = post_dict['name']
    return Osd(uuid=uuidgen(), name=name)