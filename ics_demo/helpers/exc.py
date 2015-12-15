import tornado.web

class IcsError(tornado.web.HTTPError):
    """
    Unknown ics error
    """
    def __init__(self, status_code, msg):
        super(tornado.web.HTTPError, self).__init__(status_code, log_message=msg, reason=msg)

    def __str__(self):
        return self.log_message

class NotFoundError(IcsError):
    """
    No data found
    """
    def __init__(self, which_type, which_item):
        msg = self.__doc__.strip() + ': ['+ str(which_type) + '] of ' + str(which_item)
        super(IcsError, self).__init__(404, msg)

class CannotParsedError(IcsError):
    """
    Data cannot be parsed
    """
    def __init__(self, to_what, from_what):
        msg = self.__doc__.strip() + ' to ['+ str(to_what) + '] of ' + str(from_what)
        super(IcsError, self).__init__(500, msg)

class DuplicatedError(IcsError):
    """
    Data duplicated
    """
    def __init__(self, dup_type, data):
        msg = self.__doc__.strip() + ' type ['+ str(dup_type) + '] duplicated: ' + str(data)
        super(IcsError, self).__init__(500, msg)

class FailedExecError(IcsError):
    """
    Failed Executed
    """
    def __init__(self, cmd, reason):
        msg = self.__doc__.strip() + ' ['+ str(cmd) + '] reason: ' + str(reason)
        super(IcsError, self).__init__(500, msg)

class AlreadyExistsError(IcsError):
    """
    Already Exists
    """
    def __init__(self, what_exists, where):
        msg = self.__doc__.strip() + ' ['+ str(what_exists) + '] on: ' + str(where)
        super(IcsError, self).__init__(500, msg)

class InconsistentError(IcsError):
    """
    Data Inconsistent
    """
    def __init__(self, l_type, r_type, l_data='', r_data=''):
        msg = self.__doc__.strip() + ' between [%s]: %s , [%s]: %s' % (l_type, r_type, l_data, r_data)
        super(IcsError, self).__init__(500, msg)
