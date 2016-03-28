from base import Service
from ics_demo.helpers.base import uuidgen


# vsan service: vsan, mon, osd
class OsdService(Service):

    def get_vsan_info(self):
        cmd = 'python shell.py osd show --uuid ceph'
        return self.remote_cmd_list(cmd)