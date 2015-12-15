from sqlobject import *

from ics_demo.helpers.exc import NotFoundError
from ics_demo.helpers.convert import sqlist2list, sqlobj2dict
from ics_demo.dao.interfaces.mapping import ref_mapping

# private helper functions

# convert xxxID:id to xxxRef:identifier
def id_to_ref(output_dict):
    result = {}
    for key, val in output_dict.iteritems():
        if key.endswith("ID"):
            ref_key = key[:-2]
            klass = ref_mapping.get(ref_key, None)
            if ref_key in ref_mapping.keys():
               result[ref_key + 'Ref'] = klass.get(val).get_identifier()
        else:
            result[key] = val
    return result

def _get_all_from_orm(klass):
    objs = klass.select()
    return sqlist2list(objs, blacklist=['id'])

def _get_one_by_uuid_from_orm(klass, uuid):
    try:
        obj = klass.selectBy(uuid=uuid).getOne()
    except SQLObjectNotFound:
        raise NotFoundError(str(klass.__name__), uuid)
    return sqlobj2dict(obj, blacklist=['id'])

# public functions
def class_get_all_to_dict(klass):
    return map(id_to_ref, _get_all_from_orm(klass))

def class_get_one_by_uuid_to_dict(klass, uuid):
    return id_to_ref(_get_one_by_uuid_from_orm(klass, uuid))

def class_get_one_by_uuid_to_obj(klass, uuid):
    try:
        return klass.selectBy(uuid=uuid).getOne()
    except SQLObjectNotFound:
        raise NotFoundError(str(klass.__name__), uuid)

def class_get_one_by_ID_to_obj(klass, ID):
    try:
        return klass.get(ID)
    except SQLObjectNotFound:
        raise NotFoundError(str(klass.__name__), ID)

def class_get_keys(klass):
    return klass.sqlmeta.getColumns().keys()
