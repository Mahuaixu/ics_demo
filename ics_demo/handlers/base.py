import tornado.web
from sqlobject import *

from ics_demo.helpers.convert import sqlist2list, sqlobj2dict

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("ICS Demo")
