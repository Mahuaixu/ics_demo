from sqlobject import *

from ics_demo.helpers.exc import NotFoundError
from ics_demo.helpers.convert import sqlist2list, sqlobj2dict

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
        return self._get_all_from_orm(klass)

    def get_one_by_class(self, klass, identifier):
        return self._get_one_from_orm(klass, identifier)

    def get_keys_by_class(self, klass):
        return klass.sqlmeta.getColumns().keys()
