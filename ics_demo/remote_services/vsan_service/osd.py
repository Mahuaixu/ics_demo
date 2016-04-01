from ics_demo.remote_services.base import Service
from ics_demo.helpers.base import uuidgen

base_osd_cmd = 'ics-storage vsandatastore osd'


class OsdService(Service):

    def osd_create(self, uuid, disk):
        cmd = 'ics-storage vsandatastore osd create --uuid %s --disk %s' % (uuid, disk)
        return self.remote_cmd_list(cmd)

    def osd_delete(self, uuid, disk):
        cmd = 'ics-storage vsandatastore osd delete --uuid %s --disk %s' % (uuid, disk)
        return self.remote_cmd_list(cmd)

    def osd_destroy(self, uuid, disk, osd_id):
        cmd = 'ics-storage vsandatastore osd destroy --uuid %s --disk %s --id %s' % (uuid, disk, osd_id)
        return self.remote_cmd_list(cmd)

    def osd_purge(self, disk):
        cmd = 'ics-storage vsandatastore osd purge --disk %s' % disk
        return self.remote_cmd_list(cmd)

    def osd_list(self, uuid):
        cmd = 'ics-storage vsandatastore osd list --uuid %s' % uuid
        return self.remote_cmd_list(cmd)

    def osd_show(self, uuid):
        cmd = 'ics-storage vsandatastore osd show --uuid %s' % uuid
        return self.remote_cmd_list(cmd)

    def osd_getid(self, disk):
        cmd = 'ics-storage vsandatastore osd getid --disk %s' % disk
        return self.remote_cmd_list(cmd)

    def osd_status(self, uuid):
        cmd = 'ics-storage vsandatastore osd status --uuid %s' % uuid
        return self.remote_cmd_list(cmd)

    def osd_start(self, uuid, id):
        cmd = 'ics-storage vsandatastore osd start --uuid %s --id %s' % (uuid, id)
        return self.remote_cmd_list(cmd)

    def osd_restart(self, uuid):
        cmd = 'ics-storage vsandatastore osd restart --uuid %s --id %s' % (uuid, id)
        return self.remote_cmd_list(cmd)

    def osd_stop(self, uuid):
        cmd = 'ics-storage vsandatastore osd stop --uuid %s --id %s' % (uuid, id)
        return self.remote_cmd_list(cmd)

    def osd_service(self, uuid, enable):
        cmd = 'ics-storage vsandatastore osd service --uuid %s --enable %s' % (uuid, enable)
        return self.remote_cmd_list(cmd)




