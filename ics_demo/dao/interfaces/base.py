from sqlobject import *

from ics_demo.helpers.exc import NotFoundError
from ics_demo.helpers.convert import sqlist2list, sqlobj2dict

class BaseDAO(object):
    def _get_all_from_orm(self, klass):
        objs = klass.select()
        return sqlist2list(objs)

    def _get_one_from_orm(self, klass, identifier):
        try:
            obj = klass.get(identifier)
        except SQLObjectNotFound:
            raise NotFoundError()
        return sqlobj2dict(obj)

    def _get_one_from_livestatus(self, klass, identifier):
        pass

    def _combine_obj(self, persist, live):
        return persist

    def _get_id(self, persist):
        return persist

    def get_all_by_class(self, klass):
        result = []
        for persist in self._get_all_from_orm(klass):
            live = self._get_one_from_livestatus(klass, self._get_id(persist))
            result.append(self._combine_obj(persist, live))
        return result

    def get_one_by_class(self, klass, identifier):
        persist = self._get_one_from_orm(klass, identifier)
        live = self._get_one_from_livestatus(klass, identifier)
        return self._combine_obj(persist, live)

    def get_keys_by_class(self, klass):
        return klass.sqlmeta.getColumns().keys()
