import json

import tornado

from ics_demo.handlers import BaseHandler
from ics_demo.helpers.exc import NotFoundError
from ics_demo.dao import RabbitDAO

class DemoBaseHandler(BaseHandler):
    def get(self):
        self.write("A story of Rabbit")

class DemoRabbitHandler(DemoBaseHandler):
    def get(self, rabbit_id=None):
        self.write(json.dumps({'rabbit': self.get_from_dao(RabbitDAO, rabbit_id)}))

