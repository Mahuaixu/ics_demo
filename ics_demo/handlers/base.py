import json
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("ICS Demo")

    def json_write(self, obj):
        self.write(json.dumps(obj.__dict__, default=lambda o: o.__dict__))
