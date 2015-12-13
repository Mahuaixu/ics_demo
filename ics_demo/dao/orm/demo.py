from sqlobject import *
from ics_demo.dao.orm.base import IcsSQLObject

"""
    Carrot n <-----> 1 Rabbit
    Corps  n <-----> n Rabbit
"""

class Carrot(IcsSQLObject):
    """Who is eating me???"""
    name = StringCol()
    rabbit = ForeignKey('Rabbit')

class Rabbit(IcsSQLObject):
    """
    A Rabbit has(related to) a lot of Carrots.
    """
    name = StringCol()
    carrots = MultipleJoin('Carrot')
    corps = RelatedJoin('Corps')

class Corps(IcsSQLObject):
    """
    A Corps is compound by some Rabbits,
    A Rabbit can attend multiple Corps'.
    """
    name = StringCol()
    rabbits = RelatedJoin('Rabbit')
