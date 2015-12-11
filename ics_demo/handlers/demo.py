import json

from ics_demo.handlers import BaseHandler
from ics_demo.dao.orm.demo import Rabbit
from ics_demo.helpers.convert import sqlist2list

class DemoBaseHandler(BaseHandler):
    def get(self):
        self.write("A story of Rabbit")

class DemoRabbitHandler(DemoBaseHandler):
    def get(self):
        rabbits = Rabbit.select()
        result = json.dumps({'rabbit': sqlist2list(rabbits)})
        self.write(result)
