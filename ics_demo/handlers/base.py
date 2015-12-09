import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("ICS Demo")
