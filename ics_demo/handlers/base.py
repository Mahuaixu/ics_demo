import tornado.web
from sqlobject import *

from ics_demo.helpers.convert import sqlist2list, sqlobj2dict, json2dict, error2json, excinfo2str
from ics_demo.helpers.exc import NotFoundError, CannotParsedError
from mapping import dao_mapping

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("ICS Demo")

    def prepare(self):
        if self.request.method == 'POST' and self.request.headers["Content-Type"].startswith("application/json"):
            self.post_data = json2dict(self.request.body)
        else:
            self.post_data = None

    def write_error(self, status_code, **kwargs):
        self.set_header('Content-Type', 'text/plain')
        exc_info = kwargs['exc_info']
        if isinstance(exc_info[1], tornado.web.HTTPError):
            log_message = kwargs['exc_info'][1].log_message
        else:
            log_message = excinfo2str(exc_info)
        self.write(error2json(log_message))
        self.finish()

    def get_from_dao(self, dao, identifier=None):
        if not identifier:
            data = dao.get_all()
        else:
            data = dao.get_one(identifier)
        return data

    def deref_user_data(self, post_dict):
        """user posted data keys must in orm"""
        result = {}
        for key, val in post_dict.iteritems():
            if key.endswith('Ref') and len(key) > 3:
                key = key[:-3]
                if key in dao_mapping.keys():
                    dao = dao_mapping.get(key, None)
                    try:
                        result[key] = dao.get_obj(val)
                    except NotFoundError:
                        raise CannotParsedError(key, post_dict)
            else:
                result[key] = val
        return result
