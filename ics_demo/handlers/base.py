import tornado.web
from sqlobject import *

from ics_demo.helpers.convert import sqlist2list, sqlobj2dict, json2dict
from ics_demo.helpers.exc import NotFoundError, CannotParsedError
from mapping import dao_mapping

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("ICS Demo")

    def get_from_dao(self, dao, identifier=None):
        try:
            if not identifier:
                data = dao.get_all()
            else:
                data = dao.get_one(identifier)
        except NotFoundError, exp:
                exp.handle()
        return data

    def parse_user_data(self, post_data):
        try:
            post_dict = json2dict(post_data)
        except CannotParsedError, exp:
            exp.handle()
        return post_dict

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
                        CannotParsedError().handle()
            else:
                result[key] = val
        return result

    def parse_and_check_user_data(self, post_data):
        post_dict = self.parse_user_data(post_data)
        return self.deref_user_data(post_dict)
