import logging
from remoto import Connection

from .registers import registered_services

from ics_demo.dao import host_dao
from ics_demo.helpers.exc import DuplicatedError, AlreadyExistsError, NotFoundError, InconsistentError
from ics_demo.helpers.base import uuidgen, valid_ipaddr
from ics_demo.helpers.remotes import ssh_copy_id, check_dirty_host, inject_uuid_to_host, remote_hostname, get_uuid_on_host, remove_uuid_on_host

class Proxy(object):
    # global proxys
    proxy_list = []

    def __init__(self, ipaddr, create=False, password='', user='root', clean=False):
        """
            Proxy is composed of (connection, Host instance)
            1) Create remoto.Connection to host by given ip address
            2) if create: Get host infomation and generate Host instance
            3) if connect: Get Host instance from DAO layer
        """
        valid_ipaddr(ipaddr)
        if ipaddr in [proxy.host.ipaddr for proxy in Proxy.proxy_list]:
            raise AlreadyExistsError('proxy host', ipaddr)

        if create:
            # inject ssh auth
            if not password:
                raise NotFoundError('given password', ipaddr)
            ssh_copy_id(ipaddr, user, password)

        self.conn = Connection(ipaddr, logger=logging.getLogger(ipaddr))
        # Clean env for test
        if clean and create:
            remove_uuid_on_host(self.conn)

        # Create relation to Host
        if create:
            # check whether host has been used
            check_dirty_host(self.conn)
            host_uuid = uuidgen()
            inject_uuid_to_host(self.conn, host_uuid)

            hostname = remote_hostname(self.conn)
            host = host_dao.save({
                'uuid' : host_uuid,
                'name' : hostname,
                'ipaddr': ipaddr,
                'initialized' : 0,
            })
        else:
            host = host_dao.get_obj_by_ipaddr(ipaddr)
            uuid_on_host = get_uuid_on_host(self.conn)
            if host.uuid != uuid_on_host:
                raise InconsistentError('uuid on host', 'uuid in DB', uuid_on_host, host.uuid)

        self.host = host
        self.uuid = host.uuid

        # Register services
        self.services = {}
        for name, service in registered_services.iteritems():
            self.services[name] = service(self)

        Proxy.proxy_list.append(self)

    def get_service(self, srv_name):
        if srv_name not in self.services.keys():
            raise NotFoundError('proxy service', srv_name)
        return self.services[srv_name]
        
    def get_conn(self):
        return self.conn

    #TODO refresh proxy_list by class method when host ip changed


def init_proxy():
    Proxy('127.0.0.1', password='root', create=True, clean=True)
