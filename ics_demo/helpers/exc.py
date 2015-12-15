import tornado.web

class IcsError(tornado.web.HTTPError):
    """
    Unknown ics error
    """
    def __init__(self, status_code):
        super(tornado.web.HTTPError, self).__init__(status_code, log_message=self.message, reason=self.message)

    def __str__(self):
        return self.message

class NotFoundError(IcsError):
    """
    No data found
    """
    def __init__(self, which_type, which_item):
        self.message = self.__doc__.strip() + ': ['+ str(which_type) + '] of ' + str(which_item)
        super(IcsError, self).__init__(404)

class CannotParsedError(IcsError):
    """
    Data cannot be parsed
    """
    def __init__(self, to_what, from_what):
        self.message = self.__doc__.strip() + ' to ['+ str(to_what) + '] of ' + str(from_what)
        super(IcsError, self).__init__(500)

class DuplicatedError(IcsError):
    """
    Data duplicated
    """
    def __init__(self, dup_type, data):
        self.message = self.__doc__.strip() + ' type ['+ str(dup_type) + '] duplicated: ' + str(data)
        super(IcsError, self).__init__(500)

class FailedExecError(IcsError):
    """
    Failed Executed
    """
    def __init__(self, cmd, reason):
        self.message = self.__doc__.strip() + ' ['+ str(cmd) + '] reason: ' + str(reason)
        super(IcsError, self).__init__(500)

class AlreadyExistsError(IcsError):
    """
    Already Exists
    """
    def __init__(self, what_exists, where):
        self.message = self.__doc__.strip() + ' ['+ str(what_exists) + '] on: ' + str(where)
        super(IcsError, self).__init__(500)

class InconsistentError(IcsError):
    """
    Data Inconsistent
    """
    def __init__(self, l_type, r_type, l_data='', r_data=''):
        self.message = self.__doc__.strip() + ' between [%s]: %s , [%s]: %s' % (l_type, r_type, l_data, r_data)
        super(IcsError, self).__init__(500)
