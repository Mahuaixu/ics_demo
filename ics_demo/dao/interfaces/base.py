from sqlobject import *

from ics_demo.helpers.exc import NotFoundError
from ics_demo.helpers.convert import sqlist2list, sqlobj2dict
from ics_demo.dao.interfaces.mapping import ref_mapping

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

class BaseDAO(object):
    def _get_all_from_orm(self, klass):
        objs = klass.select()
        return sqlist2list(objs, blacklist=['id'])

    def _get_one_from_orm(self, klass, identifier):
        try:
            obj = klass.selectBy(uuid=identifier).getOne()
        except SQLObjectNotFound:
            raise NotFoundError()
        return sqlobj2dict(obj, blacklist=['id'])

    def get_all_by_class(self, klass):
        return map(id_to_ref, self._get_all_from_orm(klass))

    def get_one_by_class(self, klass, identifier):
        return id_to_ref(self._get_one_from_orm(klass, identifier))

    def get_keys_by_class(self, klass):
        return klass.sqlmeta.getColumns().keys()
