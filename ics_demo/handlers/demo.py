import json

import tornado

from ics_demo.handlers import BaseHandler
from ics_demo.dao.orm.demo import Rabbit

class DemoBaseHandler(BaseHandler):
    def get(self):
        self.write("A story of Rabbit")

class DemoRabbitHandler(DemoBaseHandler):
    def get(self, rabbit_id=None):
        rabbit = self.get_all_or_one(Rabbit, rabbit_id)
        self.write(json.dumps({'rabbit': rabbit}))
