import tornado.web
from sqlobject import *

from ics_demo.helpers.convert import sqlist2list, sqlobj2dict, json2dict

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("ICS Demo")

    def get_from_dao(self, DAO, identifier=None):
        dao = DAO()
        try:
            if not identifier:
                data = dao.get_all()
            else:
                data = dao.get_one(identifier)
        except NotFoundError, exp:
                exp.handle()
        return data

    def deref_dict(self, post_dict, ref_mapping):
        #TODO
        return post_dict

    def parse_user_data(self, post_data, ref_mapping):
        try:
            post_dict = json2dict(post_data)
        except CannotParsedError, exp:
            exp.handle()
        post_dict = self.deref_dict(post_dict, ref_mapping)
        return post_dict

    def check_user_data(self, DAO, post_dict):
        """user posted data keys must in orm"""
        dao = DAO()
        for key in post_dict.keys():
            if key.endswith('Ref') and len(key) > 3:
                key = key[:-3]
            if key not in dao.get_keys():
                CannotParsedError().handle()

    def parse_and_check_user_data(self, DAO, post_data, ref_mapping):
        post_dict = self.parse_user_data(post_data, ref_mapping)
        self.check_user_data(DAO, post_dict)
        return post_dict

    def save_to_dao(self, DAO, post_dict):
        dao = DAO()
        return dao.save(post_dict)
