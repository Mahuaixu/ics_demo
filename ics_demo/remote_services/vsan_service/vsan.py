from ics_demo.remote_services.base import Service
from ics_demo.helpers.base import uuidgen

base_vsan_cmd = 'ics-storage vsandatastore vsan'


# vsan service: vsan, mon, osd
class VsanService(Service):

    def vsan_info(self):
        cmd = 'python shell.py vsan show --uuid ceph'
        return self.remote_cmd_list(cmd)

    def vsan_status(self, uuid):
        cmd = 'ics-storage vsandatastore vsan status --uuid %s' % uuid
        return self.remote_cmd_list(cmd)

    def vsan_show(self, uuid):
        cmd = 'ics-storage vsandatastore vsan show --uuid %s' % uuid
        return self.remote_cmd_list(cmd)

    def vsan_image_create(self, uuid, volume, size):
        cmd = 'ics-storage vsandatastore vsan imagecreate --uuid %s --volume %s --size %s' % (uuid, volume, size)
        return self.remote_cmd_list(cmd)

    def vsan_iamge_map(self, uuid, volume):
        cmd = 'ics-storage vsandatastore vsan imagemap --uuid %s --volume %s' % (uuid, volume)
        return self.remote_cmd_list(cmd)

    def vsan_iamge_unmap(self, uuid, volume):
        cmd = 'ics-storage vsandatastore vsan imageunmap --uuid %s --volume %s' % (uuid, volume)
        return self.remote_cmd_list(cmd)

    def vsan_iamge_delete(self, uuid, volume):
        cmd = 'ics-storage vsandatastore vsan imagedelete --uuid %s --volume %s' % (uuid, volume)
        return self.remote_cmd_list(cmd)

    def vsan_map_info(self, uuid, volume):
        cmd = 'ics-storage vsandatastore vsan imagemapinfo --uuid %s --volume %s' % (uuid, volume)
        return self.remote_cmd_list(cmd)

    def vsan_image_info(self, uuid, volume):
        cmd = 'ics-storage vsandatastore vsan imageinfo --uuid %s --volume %s' % (uuid, volume)
        return self.remote_cmd_list(cmd)

    def vsan_set(self, uuid, field, value):
        cmd = 'ics-storage vsandatastore vsan set --uuid %s --field %s --value %s' % (uuid, field, value)
        return self.remote_cmd_list(cmd)

    def vsan_balance(self, uuid, flag=None):
        cmd = 'ics-storage vsandatastore vsan balance --uuid %s --flag %s' % (uuid, flag)
        return self.remote_cmd_list(cmd)

    def vsan_start(self, uuid):
        cmd = 'ics-storage vsandatastore vsan start --uuid %s' % uuid
        return self.remote_cmd_list(cmd)

    def vsan_restart(self, uuid):
        cmd = 'ics-storage vsandatastore vsan restart --uuid %s' % uuid
        return self.remote_cmd_list(cmd)

    def vsan_stop(self, uuid):
        cmd = 'ics-storage vsandatastore vsan stop --uuid %s' % uuid
        return self.remote_cmd_list(cmd)



