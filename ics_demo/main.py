import tornado.ioloop
import tornado.web
from ics_demo.handlers import BaseHandler

application = tornado.web.Application([
    (r"/", BaseHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
