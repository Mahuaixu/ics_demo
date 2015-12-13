import tornado.web
from sqlobject import *

from ics_demo.helpers.convert import sqlist2list, sqlobj2dict, json2dict
from ics_demo.helpers.exc import NotFoundError, CannotParsedError

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
        post_dict = self.deref_dict(post_dict, ref_mapping)
        return post_dict

    def check_user_data(self, post_dict, valid_keys):
        """user posted data keys must in orm"""
        for key in valid_keys:
            if key.endswith('Ref') and len(key) > 3:
                key = key[:-3]
            if key not in valid_keys:
                CannotParsedError().handle()

    def parse_and_check_user_data(self, post_data, valid_keys):
        post_dict = self.parse_user_data(post_data)
        self.check_user_data(post_dict, valid_keys)
        return post_dict
