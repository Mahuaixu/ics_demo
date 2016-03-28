from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.vsan import BlockDevice

from ics_demo.helpers import uuidgen


def get_all():
    return base.class_get_all_to_dict(BlockDevice)


def get_one(uuid):
    return base.class_get_one_by_uuid_to_dict(BlockDevice, uuid)


def get_obj(uuid):
    return base.class_get_one_by_uuid_to_obj(BlockDevice, uuid)


def get_obj_by_ID(ID):
    return base.class_get_one_by_ID_to_obj(BlockDevice, ID)


def get_keys():
    return base.class_get_keys(BlockDevice)


def save(post_dict):
    record_id = post_dict['id']
    name = post_dict['name']
    used = post_dict['used']
    capacity = post_dict['capacity']
    absolute_path = post_dict['absolute_path']
    return BlockDevice(id=record_id, uuid=uuidgen(), name=name, used=used, capacity=capacity,absolute_path=absolute_path)
