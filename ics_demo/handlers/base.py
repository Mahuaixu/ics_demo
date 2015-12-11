import tornado.web
from sqlobject import *

from ics_demo.helpers.convert import sqlist2list, sqlobj2dict

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("ICS Demo")

    def get_all(self, cls):
        objs = cls.select()
        return sqlist2list(objs)

    def get_one(self, cls, identifier):
        obj = cls.get(identifier)
        return sqlobj2dict(obj)

    def get_all_or_one(self, cls, identifier):
        try:
            if not identifier:
                return self.get_all(cls)
            else:
                return self.get_one(cls, identifier)
        except SQLObjectNotFound:
            raise tornado.web.HTTPError(404)
