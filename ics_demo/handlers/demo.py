import json

import tornado
from sqlobject import *

from ics_demo.handlers import BaseHandler
from ics_demo.dao.orm.demo import Rabbit

class DemoBaseHandler(BaseHandler):
    def get(self):
        self.write("A story of Rabbit")

class DemoRabbitHandler(DemoBaseHandler):
    def get(self, rabbit_id=None):
        try:
            if not rabbit_id:
                rabbit = self.get_all(Rabbit)
            else:
                rabbit = self.get_one(Rabbit, rabbit_id)
        except SQLObjectNotFound:
            raise tornado.web.HTTPError(404)
        self.write(json.dumps({'rabbit': rabbit}))
