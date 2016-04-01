from ics_demo.remote_services.base import Service
from ics_demo.helpers.base import uuidgen


base_mon_cmd = 'ics-storage vsandatastore mon'


class MonService(Service):

    def mon_create(self, uuid, name):
        cmd = 'ics-storage vsandatastore mon create --uuid %s --name %s' % (uuid,  name)
        return self.remote_cmd_list(cmd)

    def mon_add(self, uuid, name, address):
        cmd = 'ics-storage vsandatastore mon add --uuid %s --name %s --address' % (uuid,  name, address)
        return self.remote_cmd_list(cmd)

    def mon_destroy(self, uuid, name):
        cmd = 'ics-storage vsandatastore mon destroy --uuid %s --name' % (uuid, name)
        return self.remote_cmd_list(cmd)

    def mon_purge(self, uuid, name):
        cmd = 'ics-storage vsandatastore mon purge --uuid %s --name' % (uuid, name)
        return self.remote_cmd_list(cmd)

    def mon_status(self, uuid, name):
        cmd = 'ics-storage vsandatastore mon status --uuid %s --name' % (uuid, name)
        return self.remote_cmd_list(cmd)

    def mon_list(self, uuid, name):
        cmd = 'ics-storage vsandatastore mon show --uuid %s --name' % (uuid, name)
        return self.remote_cmd_list(cmd)

    def mon_service(self, enable):
        cmd = 'ics-storage vsandatastore mon service --enable %s' % enable
        return self.remote_cmd_list(cmd)

    def mon_start(self):
        cmd = 'ics-storage vsandatastore mon start'
        return self.remote_cmd_list(cmd)

    def mon_restart(self):
        cmd = 'ics-storage vsandatastore mon restart'
        return self.remote_cmd_list(cmd)

    def mon_stop(self):
        cmd = 'ics-storage vsandatastore mon stop'
        return self.remote_cmd_list(cmd)



