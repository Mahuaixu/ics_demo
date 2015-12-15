import uuid
import socket

def uuidgen():
    return str(uuid.uuid4())

def valid_ipaddr(ipaddr):
    try:
        socket.inet_aton(ipaddr)
    except:
        raise CannotParsedError('ip address', ipaddr)
