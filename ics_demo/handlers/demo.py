import json

import tornado

from ics_demo.handlers import BaseHandler
from ics_demo.helpers.exc import CannotParsedError
from ics_demo.dao import RabbitDAO, CarrotDAO, CorpsDAO
from ics_demo.dao.orm.demo import Carrot, Rabbit, Corps

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
                2. check whether can be parsed and convert it to dict
                        a generic operation. throw it to BaseHandler
                3. prepare data
                    3.1 derefernce ObjectRef from dao
                        a generic operation. throw it to BaseHandler
                    3.2 fill user posted data to object
                        dealing with it in this handler
                    3.3 fill other data rpc eagering
                4. do rpc
                5. data persistent
                6. show posted Object
        """
        # give ref mapping to parse reference
        ref_mapping = {'carrotRef' : Carrot}

        self.set_header("Content-Type", "text/plain")
        post_data = self.get_argument("rabbit")
        post_dict = self.parse_and_check_user_data(RabbitDAO, post_data, ref_mapping)
        rabbit = self.save_to_dao(RabbitDAO, post_dict)
        self.write(json.dumps({'rabbit': self.get_from_dao(RabbitDAO, rabbit.get_identifier())}))

class DemoCarrotHandler(DemoBaseHandler):
    def get(self, carrot_id=None):
        self.write(json.dumps({'carrot': self.get_from_dao(CarrotDAO, carrot_id)}))

class DemoCorpsHandler(DemoBaseHandler):
    def get(self, corps_id=None):
        self.write(json.dumps({'corps': self.get_from_dao(CorpsDAO, corps_id)}))
