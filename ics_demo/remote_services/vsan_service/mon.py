from base import Service
from ics_demo.helpers.base import uuidgen


# vsan service: vsan, mon, osd
class MonService(Service):

    def get_mon_info(self):
        cmd = 'python shell.py mon show'
        return self.remote_cmd_list(cmd)