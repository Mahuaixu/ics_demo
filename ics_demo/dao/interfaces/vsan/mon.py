from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.vsan import Mon

from ics_demo.helpers import uuidgen


def get_all():
    return base.class_get_all_to_dict(Mon)


def get_one(uuid):
    return base.class_get_one_by_uuid_to_dict(Mon, uuid)


def get_obj(uuid):
    return base.class_get_one_by_uuid_to_obj(Mon, uuid)


def get_obj_by_ID(ID):
    return base.class_get_one_by_ID_to_obj(Mon, ID)


def get_keys():
    return base.class_get_keys(Mon)


def save(post_dict):
    record_id = post_dict['id']
    name = post_dict['name']
    host_id = post_dict['host_id']
    return Mon(id=record_id, uuid=uuidgen(), name=name, host_id=host_id)
