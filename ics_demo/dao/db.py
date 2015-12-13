from sqlobject import *
from ics_demo.dao.orm.demo import Carrot, Rabbit, Corps
from ics_demo.dao import CarrotDAO, RabbitDAO, CorpsDAO
from ics_demo.helpers import uuidgen

def createTables(tables):
    for table in tables:
        table.createTable(ifNotExists=True)

def cleanTables(tables):
    for table in tables[::-1]:
        table.dropTable(ifExists=True)

global rabbit_dao
global carrot_dao
global corps_dao
global demo_tables

demo_tables = [Rabbit, Carrot, Corps] # order by dependency
rabbit_dao = RabbitDAO()
carrot_dao = CarrotDAO()
corps_dao = CorpsDAO()

def init_demo():
    cleanTables(demo_tables)
    createTables(demo_tables)
    # init test data
    bunny_kun1 = Rabbit(uuid=uuidgen(), name="BunnyKun1")
    bunny_kun2 = Rabbit(uuid=uuidgen(), name="BunnyKun2")
    #carrot_kun = Carrot(name="CarrotKun")
    carrot_kun1 = Carrot(uuid=uuidgen(), name="CarrotKun1", rabbit=bunny_kun1)
    carrot_kun2 = Carrot(uuid=uuidgen(), name="CarrotKun2", rabbit=bunny_kun2)
    carrot_kun3 = Carrot(uuid=uuidgen(), name="CarrotKun3", rabbit=bunny_kun2)
    corps = Corps(uuid=uuidgen(), name="BunnyArmy")
    corps.addRabbit(bunny_kun1)
    corps.addRabbit(bunny_kun2)

def init_db():
    #sqlhub.processConnection = connectionForURI('sqlite:/:memory:')
    #sqlhub.processConnection = connectionForURI('sqlite:///root/zzltestsqlitedb')
    sqlhub.processConnection = connectionForURI('mysql://root:root@localhost:3306/zzl?debug=t')
    init_demo()

