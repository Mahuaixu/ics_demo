import json

import tornado

from ics_demo.handlers import BaseHandler
from ics_demo.helpers.exc import NotFoundError
from ics_demo.dao import RabbitDAO, CarrotDAO, CorpsDAO

class DemoBaseHandler(BaseHandler):
    def get(self):
        self.write("A story of Rabbit")

class DemoRabbitHandler(DemoBaseHandler):
    def get(self, rabbit_id=None):
        self.write(json.dumps({'rabbit': self.get_from_dao(RabbitDAO, rabbit_id)}))

class DemoCarrotHandler(DemoBaseHandler):
    def get(self, carrot_id=None):
        self.write(json.dumps({'carrot': self.get_from_dao(CarrotDAO, carrot_id)}))

class DemoCorpsHandler(DemoBaseHandler):
    def get(self, corps_id=None):
        self.write(json.dumps({'corps': self.get_from_dao(CorpsDAO, corps_id)}))
