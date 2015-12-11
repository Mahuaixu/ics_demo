import tornado 

class IcsError(Exception):
    """
    Unknown ics error
    """

    def __str__(self):
        doc = self.__doc__.strip()
        return ': '.join([doc] + [str(a) for a in self.args])

class NotFoundError(IcsError):
    """
    No data found
    """
    def handle(self):
        raise tornado.web.HTTPError(404, self.__doc__.strip())

class CannotParsedError(IcsError):
    """
    Data cannot be parsed
    """
    def handle(self):
        raise tornado.web.HTTPError(500, self.__doc__.strip())

