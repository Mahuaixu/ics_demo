import tornado.ioloop
import tornado.web
from ics_demo.dao.db import init_db
from ics_demo.handlers import BaseHandler
from ics_demo.handlers import DemoHandler

application = tornado.web.Application([
    (r"/", BaseHandler),
    (r"/demo", DemoHandler),
])

if __name__ == "__main__":
    init_db()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
