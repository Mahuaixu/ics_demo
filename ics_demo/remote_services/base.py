from ics_demo.helpers.remotes import remote_cmd_list, remote_cmd_oneline, remote_cmd_json, remote_cmd_quiet

class Service(object):
    def __init__(self, proxy):
        self.conn = proxy.conn

    def remote_cmd_list(self, cmd_str):
        return remote_cmd_list(self.conn, cmd_str)

    def remote_cmd_oneline(self, cmd_str):
        return remote_cmd_oneline(self.conn, cmd_str)

    def remote_cmd_json(self, cmd_str):
        return remote_cmd_json(self.conn, cmd_str)

    def remote_cmd_quiet(self, cmd_str):
        return remote_cmd_quiet(self.conn, cmd_str)
