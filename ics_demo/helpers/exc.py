import tornado 

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
        message = self.__doc__.strip() + ': ['+ str(to_what) + '] of ' + str(from_what)
        super(IcsError, self).__init__(500, message)

