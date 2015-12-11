import json
from ics_demo.handlers import BaseHandler
from ics_demo.dao.orm.demo import Rabbit
from ics_demo.helpers.convert import sqlist2list

class DemoHandler(BaseHandler):
    def get(self):
        rabbits = Rabbit.select()
        result = json.dumps({'rabbit': sqlist2list(rabbits)})
        self.write(result)
        
