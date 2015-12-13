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
        """
            Instructions:
            In GET:
                1. fetch data from dao,
                    BaseHandler provide method get_from_dao to do some generic operation
                2. display data and convert it to json
                    using json.dumps enough and fill type
        """
        self.write(json.dumps({'rabbit': self.get_from_dao(RabbitDAO, rabbit_id)}))

    def post(self):
        """
            Instructions:
            In POST:
                1. get data user posted
                2. check whether can be parsed
                        a generic operation. throw it to Helpers
                3. prepare data
                    3.1 derefernce ObjectRef from dao
                        a generic operation. throw it to BaseHandler
                    3.2 fill user posted data to object
                        dealing with it in this handler
                    3.3 fill data rpc eagering
                4. do rpc
                5. data persistent
        """
        self.set_header("Content-Type", "text/plain")
        post_data = self.get_argument("rabbit")

class DemoCarrotHandler(DemoBaseHandler):
    def get(self, carrot_id=None):
        self.write(json.dumps({'carrot': self.get_from_dao(CarrotDAO, carrot_id)}))

class DemoCorpsHandler(DemoBaseHandler):
    def get(self, corps_id=None):
        self.write(json.dumps({'corps': self.get_from_dao(CorpsDAO, corps_id)}))
