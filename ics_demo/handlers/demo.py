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
        rabbit_dao = RabbitDAO()
        try:
            if not rabbit_id:
                rabbit = rabbit_dao.get_all()
            else:
                rabbit = rabbit_dao.get_one(rabbit_id)
        except NotFoundError, exp:
            exp.handle()
        self.write(json.dumps({'rabbit': rabbit}))
