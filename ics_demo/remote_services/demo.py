from base import Service
from ics_demo.helpers.base import uuidgen

class RabbitService(Service):

    def it_is_my_warren(self, name):
        cmd = 'mktemp -d /tmp/%s-XXXX' % name
        return self.remote_cmd_oneline(cmd)

    def put_carrot_bucket_in_my_warren(self, warren):
        cmd = 'mktemp -d %s/carrots-XXXX' % warren
        return self.remote_cmd_oneline(cmd)

    def put_a_carrot(self, bucket):
        cmd = 'mktemp %s/XXXX' % bucket
        self.remote_cmd_quiet(cmd)

    def my_carrots(self, bucket):
        cmd = 'ls %s' % bucket
        return self.remote_cmd_list(cmd)
