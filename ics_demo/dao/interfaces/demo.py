from ics_demo.dao.interfaces.base import BaseDAO
from ics_demo.dao.orm.demo import Carrot, Rabbit, Corps

from ics_demo.helpers import uuidgen

class RabbitDAO(BaseDAO):
    def get_all(self):
        return self.get_all_by_class(Rabbit)

    def get_one(self, identifier):
        return self.get_one_by_class(Rabbit, identifier)

    def get_keys(self):
        return self.get_keys_by_class(Rabbit)

    def save(self, post_dict):
        name = post_dict['name']
        return Rabbit(uuid=uuidgen(), name=name)

class CarrotDAO(BaseDAO):
    def get_all(self):
        return self.get_all_by_class(Carrot)

    def get_one(self, identifier):
        return self.get_one_by_class(Carrot, identifier)

    def get_keys(self):
        return self.get_keys_by_class(Carrot)

class CorpsDAO(BaseDAO):
    def get_all(self):
        return self.get_all_by_class(Corps)

    def get_one(self, identifier):
        return self.get_one_by_class(Corps, identifier)

    def get_keys(self):
        return self.get_keys_by_class(Corps)
