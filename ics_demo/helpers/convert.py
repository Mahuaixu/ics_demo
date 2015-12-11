import jsonpickle

def sqlobj2dict(sqlobj):
    #FIXME: dealing Datetime()
    return sqlobj.sqlmeta.asDict()

def sqlobj2json(sqlobj):
    return jsonpickle.encode(sqlobj2dict(sqlobj), unpicklable=True)

def sqlist2list(sqlist):
    return [sqlobj2dict(sqlobj) for sqlobj in sqlist]

def sqlist2json(sqlist):
    return jsonpickle.encode(sqlist2list(sqlist), unpicklable=True)
