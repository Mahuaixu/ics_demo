from sqlobject import *

class IcsSQLObject(SQLObject):

    def get_identifier(self):
        return self.id
