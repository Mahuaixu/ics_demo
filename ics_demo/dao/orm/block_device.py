from sqlobject import *
from ics_demo.dao.orm.base import IcsSQLObject
from ics_demo.dao.orm.host import Host


class BlockDevice(IcsSQLObject):
    """Block devices"""
    #id = StringCol()
    name = StringCol()
    used = BoolCol()
    capacity = StringCol()
    absolute_path = StringCol()
    osd = SingleJoin('OSD')
    host = ForeignKey('Host')