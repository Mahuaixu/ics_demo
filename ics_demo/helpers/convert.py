import json, jsonpickle
import traceback

from exc import CannotParsedError

def sqlobj2dict(sqlobj, blacklist=None):
    #FIXME: dealing Datetime()
    blacklist = list(blacklist or [])
    # result = {}
    # for key,val in sqlobj.sqlmeta.asDict().iteritems():
    #     if key not in blacklist:
    #         result[key] = val
    # return result
    return dict((key, val) for key, val in sqlobj.sqlmeta.asDict().iteritems() if key not in blacklist)

def sqlobj2json(sqlobj, blacklist=None):
    return jsonpickle.encode(sqlobj2dict(sqlobj, blacklist), unpicklable=True)

def sqlist2list(sqlist, blacklist=None):
    return [sqlobj2dict(sqlobj, blacklist) for sqlobj in sqlist]

def sqlist2json(sqlist, blacklist=None):
    return jsonpickle.encode(sqlist2list(sqlist, blacklist), unpicklable=True)

def check_json_fmt(json_str):
    try:
        json.loads(json_str)
    except ValueError:
        raise CannotParsedError("json", json_str)

def json2dict(json_str):
    try:
        decoded = json.loads(json_str)
        if type(decoded) != type({}):
            raise ValueError
    except ValueError:
        raise CannotParsedError("json", json_str)
    return decoded

def error2json(msg):
    return json.dumps({'status' : 'error', 'message' : msg})

def excinfo2str(exc_info):
    return ''.join(line for line in traceback.format_exception(*exc_info))
