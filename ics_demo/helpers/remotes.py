import subprocess 

from remoto.process import check, run

from exc import FailedExecError, AlreadyExistsError
from convert import check_json_fmt

UUID_PATH = '/tmp/uuid'


def remote_cmd_list(conn, cmd_str):
    stdout, stderr, status = check(conn, cmd_str, shell=True)
    if status != 0:
        raise FailedExecError(cmd_str, 'Executed Failed')
    return stdout

def remote_cmd_quiet(conn, cmd_str):
    remote_cmd_list(conn, cmd_str)

def remote_cmd_oneline(conn, cmd_str):
    result, status = remote_cmd_list(conn, cmd_str)
    if len(result) == 0:
        raise FailedExecError(cmd_str, 'Empty Return')
    else:
        return result[0]

def remote_cmd_json(conn, cmd_str):
    result = remote_cmd_oneline(conn, cmd_str)
    try:
        check_json_fmt(result)
    except:
        raise FailedExecError(cmd_str, 'Wrong Output Json Format')

def remote_hostname(conn):
    return remote_cmd_oneline(conn, 'hostname -s')

def check_dirty_host(conn):
    try:
        remote_cmd_quiet(conn, '[ -f %s]' % UUID_PATH)
    except FailedExecError:
        raise AlreadyExistsError('host uuid', UUID_PATH)

def inject_host_uuid(conn, uuid):
    remote_cmd_quiet(conn, 'echo %s > %s' % (uuid, UUID_PATH))

def ssh_copy_id(ipaddr, user, password):
    try:
        cmd = '/usr/bin/sshpass -p %s /usr/bin/ssh-copy-id %s@%s' % (password, user, ipaddr)
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError:
        raise FailedExecError(cmd, 'Failed inject ssh auth')
