from sqlobject import *
from ics_demo.dao.orm.base import IcsSQLObject
#from ics_demo.dao.orm.host import Host
#from ics_demo.dao.orm.host import Host
#from ics_demo.dao.orm.block_device import BlockDevice


"""
Rule:
    n <----> n : RelatedJoin
    @Example
    class User(SQLObject):
        roles = RelatedJoin('Role')
    1 <----> n : MultipleJoin
    @Example
    class Address(SQLObject):
        person = MultipleJoin('Person')
    1 <----> 1 : SingleJoin
"""


class Mon(IcsSQLObject):
    """Vsan monitors"""
    #id = StringCol()  # unused
    name = StringCol()
    host = SingleJoin('Host')
    #datastore = ForeignKey('VsanStore')


class Osd(IcsSQLObject):
    """Vsan osd device"""
    #id = StringCol()
    name = StringCol()
    block_device = SingleJoin('BlockDevice')
#   datastore = ForeignKey('VsanStore')


class VsanStore(IcsSQLObject):
    """Vsan Datastore"""
    #id = StringCol()  # unused
    name = StringCol()
    capacity = StringCol()
    datastore_type = StringCol()
    replicas = StringCol()
    external = StringCol()
    external_conf = StringCol()
    balance_status = StringCol()
    maintenance_mode = StringCol()
#   mon = MultipleJoin('Mon')
#   osd = MultipleJoin('Osd')
    host = RelatedJoin('Host')

