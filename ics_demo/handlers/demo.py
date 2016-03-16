import json

import tornado

from ics_demo.handlers import BaseHandler
from ics_demo.helpers.exc import CannotParsedError
from ics_demo.dao import rabbit_dao, carrot_dao, corps_dao
from ics_demo.dao.orm.demo import Carrot, Rabbit, Corps

from ics_demo.remote_services import Proxy

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
        self.write(json.dumps({'rabbit': self.get_from_dao(rabbit_dao, rabbit_id)}))

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
        self.set_header("Content-Type", "text/plain")
        if 'rabbit' not in self.post_data.keys():
            raise CannotParsedError('dict of Rabbit', str(self.post_data))
        else:
            post_dict = self.deref_user_data(self.post_data['rabbit'])
        # do rpc
        warrens = {}
        for proxy in Proxy.proxy_list:
            warren = proxy.RabbitService.it_is_my_warren(post_dict['name'])
            warrens[proxy.uuid] = warren
        # save data
        rabbit = rabbit_dao.save(post_dict)
        # do post rpc
        buckets = {}
        for proxy in Proxy.proxy_list:
            bucket = proxy.RabbitService.put_carrot_bucket_in_my_warren(warren)
            buckets[proxy.host.uuid] = bucket
            proxy.RabbitService.put_a_carrot(bucket)
            proxy.RabbitService.put_a_carrot(bucket)

        carrots = []
        for proxy in Proxy.proxy_list:
            carrots += proxy.RabbitService.my_carrots(buckets[proxy.uuid])

        rabbit_dict = rabbit_dao.get_one(rabbit.uuid)
        rabbit_dict['carrots'] = carrots
        self.write(json.dumps({'rabbit': rabbit_dict}))

class DemoCarrotHandler(DemoBaseHandler):
    def get(self, carrot_id=None):
        self.write(json.dumps({'carrot': self.get_from_dao(carrot_dao, carrot_id)}))

    def post(self):
        self.set_header("Content-Type", "text/plain")
        if 'carrot' not in self.post_data.keys():
            raise CannotParsedError('dict of Carrot', str(self.post_data))
        else:
            post_dict = self.deref_user_data(self.post_data['carrot'])
        carrot = carrot_dao.save(post_dict)
        self.write(json.dumps({'carrot': carrot_dao.get_one(carrot.get_identifier())}))

class DemoCorpsHandler(DemoBaseHandler):
    def get(self, corps_id=None):
        self.write(json.dumps({'corps': self.get_from_dao(corps_dao, corps_id)}))
