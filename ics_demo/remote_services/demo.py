from base import Service
from ics_demo.helpers.base import uuidgen

class RabbitService(Service):

    def it_is_my_warren(self, name):
        cmd = 'mkdir -p /tmp/%s' % name
        self.remote_cmd_quiet(cmd)

    def put_carrot_bucket_in_my_warren(self, rabbit):
        cmd = 'mkdir /tmp/%s/carrots' % rabbit.name
        self.remote_cmd_quiet(cmd)

    def put_a_carrot(self, rabbit):
        cmd = 'touch /tmp/%s/carrots/%s' % (rabbit.name, uuidgen())
        self.remote_cmd_quiet(cmd)

    def my_carrots(self, rabbit):
        cmd = 'ls /tmp/%s/carrots/' % rabbit.name
        return self.remote_cmd_list(cmd)
