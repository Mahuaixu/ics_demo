import tornado.web

class IcsError(tornado.web.HTTPError):
    """
    Unknown ics error
    """
    def __init__(self, status_code, message):
        super(tornado.web.HTTPError, self).__init__(status_code, log_message=message, reason=message)

    def __str__(self):
        doc = self.__doc__.strip()
        return ': '.join([doc] + [str(a) for a in self.args])

class NotFoundError(IcsError):
    """
    No data found
    """
    def __init__(self, what, who):
        message = self.__doc__.strip() + ': ['+ str(what) + '] of ' + str(who)
        super(IcsError, self).__init__(404, message)

class CannotParsedError(IcsError):
    """
    Data cannot be parsed
    """
    def __init__(self, to_what, from_what):
        message = self.__doc__.strip() + ' to ['+ str(to_what) + '] of ' + str(from_what)
        super(IcsError, self).__init__(500, message)

class DuplicatedError(IcsError):
    """
    Data duplicated
    """
    def __init__(self, dup_type, data):
        message = self.__doc__.strip() + ' type ['+ str(dup_type) + '] duplicated: ' + str(data)
        super(IcsError, self).__init__(500, message)

class FailedExecError(IcsError):
    """
    Failed Executed
    """
    def __init__(self, cmd, reason):
        message = self.__doc__.strip() + ' ['+ str(cmd) + '] reason: ' + str(reason)
        super(IcsError, self).__init__(500, message)

class AlreadyExistsError(IcsError):
    """
    Already Exists
    """
    def __init__(self, what_exists, where):
        message = self.__doc__.strip() + ' ['+ str(what_exists) + '] on: ' + str(where)
        super(IcsError, self).__init__(500, message)
