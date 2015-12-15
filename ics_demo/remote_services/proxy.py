from remoto import Connection

from ics_demo.dao import host_dao
from ics_demo.helpers.exc import DuplicatedError
from ics_demo.helpers.base import uuidgen
from ics_demo.helpers.import uuidgen

class Proxy(object):
    # global proxys
    proxy_list = []

    def __init__(self, ipaddr, password, user='root'):
    """
        Proxy is composed of (ipaddr, connection, host_uuid)
        1) Create remoto.Connection to host by given ip address
        2) Get host infomation and generate Host object
        3) Hold ipaddr of host in memory for quick checking ip dup
    """
        valid_ipaddr(ipaddr)
        if ipaddr in [proxy.ipaddr for proxy in Proxy.proxy_list]:
            raise
        # inject ssh auth
        ssh_copy_id(ipaddr, user, password)
        self.ipaddr = ipaddr
        self.conn = Connection(ipaddr, logger=logging.getLogger(ipaddr))
        # check whether host has been used
        check_dirty_host(self.conn)

        host_uuid = uuidgen()
        inject_host_uuid(self.conn, host_uuid)

        host_info['hostname'] = remote_hostname(self.conn)
        host = host_dao.save({
            'uuid' : host_uuid,
            'name' : host_info['hostname'],
            'ipaddr': ipaddr,
            'initialized' : 0,
        })
        Proxy.proxy_list[uuid] = self
        
    def get_conn(self):
        return self.conn

    #TODO refresh proxy_list by class method when host ip changed
