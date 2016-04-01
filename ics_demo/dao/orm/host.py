from sqlobject import *
from ics_demo.dao.orm.base import IcsSQLObject

class Host(IcsSQLObject):
    name = StringCol()
    ipaddr = StringCol()
    initialized = BoolCol()
    mon = SingleJoin('Mon')
    block_device = MultipleJoin('BlockDevice')
    datastore = RelatedJoin('VsanStore')