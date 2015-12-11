import tornado.web
from sqlobject import *

from ics_demo.helpers.convert import sqlist2list, sqlobj2dict

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("ICS Demo")

    def get_from_dao(self, DAO, identifier=None):
        dao = DAO()
        try:
            if not identifier:
                data = dao.get_all()
            else:
                data = dao.get_one(identifier)
        except NotFoundError, exp:
                exp.handle()
        return data
