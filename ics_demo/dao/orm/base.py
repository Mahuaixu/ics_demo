from sqlobject import *

class IcsSQLObject(SQLObject):
    uuid = StringCol(unique=True, varchar=True, length=36)

    def get_identifier(self):
        return self.uuid
