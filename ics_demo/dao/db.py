from sqlobject import *
from ics_demo.dao.orm.demo import Carrot, Rabbit, Corps
from ics_demo.dao.orm.host import Host
from ics_demo.dao.orm.block_device import BlockDevice
from ics_demo.dao.orm.vsan import Mon, Osd, VsanStore
from ics_demo.helpers import uuidgen

def createTables(tables):
    for table in tables:
        table.createTable(ifNotExists=True)

def cleanTables(tables):
    for table in tables[::-1]:
        table.dropTable(ifExists=True)

demo_tables = [Rabbit, Carrot, Corps] # order by dependency
vsan_tables = [Mon, Osd, VsanStore]                # order by dependency
base_tables = [Host, BlockDevice]                  # order by dependency

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

    host0 = Host(uuid="11111111-1111-1111-1111-111111111111", name="node0", ipaddr="100.7.33.56", initialized=True)
    blk0 = BlockDevice(uuid="11111111-1111-1111-1111-111111111111", name="ssd1", used=False, capacity="558.9", absolute_path="/dev/sda", host=host0)
    blk1 = BlockDevice(uuid="22222222-2222-2222-2222-222222222222", name="sas1", used=False, capacity="465.8", absolute_path="/dev/sdc", host=host0)
    blk2 = BlockDevice(uuid="33333333-3333-3333-3333-333333333333", name="sas2", used=False, capacity="465.8", absolute_path="/dev/sdd", host=host0)

    host1 = Host(uuid="22222222-1111-1111-1111-111111111111", name="node1", ipaddr="100.7.33.58", initialized=True)
    blk3 = BlockDevice(uuid="22222222-1111-1111-1111-111111111111", name="ssd1", used=False, capacity="558.9", absolute_path="/dev/sda", host=host1)
    blk4 = BlockDevice(uuid="33333333-2222-2222-2222-222222222222", name="sas1", used=False, capacity="465.8", absolute_path="/dev/sdc", host=host1)
    blk5 = BlockDevice(uuid="11111111-3333-3333-3333-333333333333", name="sas2", used=False, capacity="465.8", absolute_path="/dev/sdd", host=host1)

    host2 = Host(uuid="11111111-1111-1111-1111-222222222222", name="node2", ipaddr="100.7.33.60", initialized=True)
    blk6 = BlockDevice(uuid="11111111-1111-1111-1111-222222222222", name="ssd1", used=False, capacity="558.9", absolute_path="/dev/sda", host=host2)
    blk7 = BlockDevice(uuid="22222222-2222-2222-2222-333333333333", name="sas1", used=False, capacity="465.8", absolute_path="/dev/sdc", host=host2)
    blk8 = BlockDevice(uuid="33333333-3333-3333-3333-222222222222", name="sas2", used=False, capacity="465.8", absolute_path="/dev/sdd", host=host2)

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
