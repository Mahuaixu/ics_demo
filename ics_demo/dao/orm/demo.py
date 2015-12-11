from sqlobject import *

"""
    Carrot n <-----> 1 Rabbit
    Corps  n <-----> n Rabbit
"""

class Carrot(SQLObject):
    """Who is eating me???"""
    name = StringCol()
    rabbit = ForeignKey('Rabbit')

class Rabbit(SQLObject):
    """
    A Rabbit has(related to) a lot of Carrots.
    """
    name = StringCol()
    carrots = MultipleJoin('Carrot')
    corps = RelatedJoin('Corps')

class Corps(SQLObject):
    """
    A Corps is compound by some Rabbits,
    A Rabbit can attend multiple Corps'.
    """
    name = StringCol()
    rabbits = RelatedJoin('Rabbit')
