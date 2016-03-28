from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.vsan import VsanStore

from ics_demo.helpers import uuidgen


def get_all():
    return base.class_get_all_to_dict(VsanStore)


def get_one(uuid):
    return base.class_get_one_by_uuid_to_dict(VsanStore, uuid)


def get_obj(uuid):
    return base.class_get_one_by_uuid_to_obj(VsanStore, uuid)


def get_obj_by_ID(ID):
    return base.class_get_one_by_ID_to_obj(VsanStore, ID)


def get_keys():
    return base.class_get_keys(VsanStore)


def save(properties_dict):
    id = properties_dict['id']
    name = properties_dict['name']
    capacity = properties_dict['capacity']
    datastore_type = properties_dict['datastore_type']
    replicas = properties_dict['replicas']
    external = properties_dict['external']
    external_conf = properties_dict['external_conf']
    balance_status = properties_dict['balance_status']
    maintenance_mode = properties_dict['maintenance_mode']
    return VsanStore(uuid=uuidgen(), id=id, name=name,
                     capacity=capacity, datastore_type=datastore_type,
                     replicas=replicas, external=external, external_conf=external_conf,
                     balance_status=balance_status, maintenance_mode=maintenance_mode)