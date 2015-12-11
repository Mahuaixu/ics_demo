from ics_demo.dao import BaseDAO
from ics_demo.dao.orm.demo import Carrot, Rabbit, Corps

class RabbitDAO(BaseDAO):
    def get_all(self):
        return self.get_all_by_class(Rabbit)

    def get_one(self, identifier):
        return self.get_one_by_class(Rabbit, identifier)

class CarrotDAO(BaseDAO):
    def get_all(self):
        return self.get_all_by_class(Carrot)

    def get_one(self, identifier):
        return self.get_one_by_class(Carrot, identifier)

class CorpsDAO(BaseDAO):
    def get_all(self):
        return self.get_all_by_class(Corps)

    def get_one(self, identifier):
        return self.get_one_by_class(Corps, identifier)
