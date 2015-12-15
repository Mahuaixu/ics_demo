from ics_demo.dao.interfaces import base
from ics_demo.dao.orm.host import Host

from ics_demo.helpers import uuidgen

def get_all():
    return base.class_get_all_to_dict(Host)

def get_one(uuid):
    return base.class_get_one_by_uuid_to_dict(Host, uuid)

def get_obj(uuid):
    return base.class_get_one_by_uuid_to_obj(Host, uuid)

def get_obj_by_ID(ID):
    return base.class_get_one_by_ID_to_obj(Host, ID)

def get_obj_by_ipaddr(ipaddr):
    try:
        return Host.selectBy(ipaddr=ipaddr).getOne()
    except SQLObjectNotFound:
        raise NotFoundError('Host ip address', ipaddr)

def get_keys():
    return base.class_get_keys(Host)

def save(properties_dict):
    name = properties_dict['name']
    ipaddr = properties_dict['ipaddr']
    initialized = properties_dict['initialized']
    return Host(uuid=uuidgen(), name=name, ipaddr=ipaddr, initialized=initialized)

