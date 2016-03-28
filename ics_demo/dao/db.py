from sqlobject import *
from ics_demo.dao.orm.demo import Carrot, Rabbit, Corps
from ics_demo.dao.orm.host import Host
from ics_demo.dao.orm.vsan import Mon, Osd, DataStore, DataStoreHost, BlockDevice
from ics_demo.helpers import uuidgen

def createTables(tables):
    for table in tables:
        table.createTable(ifNotExists=True)

def cleanTables(tables):
    for table in tables[::-1]:
        table.dropTable(ifExists=True)

demo_tables = [Rabbit, Carrot, Corps] # order by dependency
vsan_tables = [Mon, Osd, DataStore]                # order by dependency
base_tables = [Host, BlockDevice, DataStoreHost]   # order by dependency

def init_demo():
    cleanTables(demo_tables)
    createTables(demo_tables)
    # init test data
    bunny_kun1 = Rabbit(uuid="11111111-1111-1111-1111-111111111111", name="BunnyKun1")
    bunny_kun2 = Rabbit(uuid="22222222-2222-2222-2222-222222222222", name="BunnyKun2")
    carrot_kun1 = Carrot(uuid="11111111-1111-1111-1111-111111111111", name="CarrotKun1", rabbit=bunny_kun1)
    carrot_kun2 = Carrot(uuid="22222222-2222-2222-2222-222222222222", name="CarrotKun2", rabbit=bunny_kun2)
    carrot_kun3 = Carrot(uuid="33333333-3333-3333-3333-333333333333", name="CarrotKun3", rabbit=bunny_kun2)
    corps = Corps(uuid="11111111-1111-1111-1111-111111111111", name="BunnyArmy")
    corps.addRabbit(bunny_kun1)
    corps.addRabbit(bunny_kun2)


def init_base():
    cleanTables(base_tables)
    createTables(base_tables)

    host0 = DataStoreHost(name="host0", ipaddr="192.168.126.0", initialized=True)
    blk0 = BlockDevice(id="0", name="xxxx", used=False, capacity="10240", absolute_path="/dev/sdb")
    host0.addBlock(blk0)
    host1 = DataStoreHost(name="host1", ipaddr="192.168.126.1", initialized=True)
    blk1 = BlockDevice(id="1", name="yyyy", used=False, capacity="10240", absolute_path="/dev/sdb")
    host1.addBlock(blk1)
    host2 = DataStoreHost(name="host2", ipaddr="192.168.126.2", initialized=True)
    blk2 = BlockDevice(id="2", name="zzzz", used=False, capacity="10240", absolute_path="/dev/sdb")
    host2.addBlock(blk2)
def init_vsan_store():
    cleanTables(vsan_tables)
    createTables(vsan_tables)
def init_db():
    #sqlhub.processConnection = connectionForURI('sqlite:/:memory:')
    #sqlhub.processConnection = connectionForURI('sqlite:///root/zzltestsqlitedb')
    sqlhub.processConnection = connectionForURI('mysql://root:root@localhost:3306/zzl?debug=t')
    init_base()
    init_vsan_store()
    init_demo()
