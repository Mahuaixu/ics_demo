import tornado.web

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
