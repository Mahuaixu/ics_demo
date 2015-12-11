import tornado.ioloop
import tornado.web
from ics_demo.dao import init_db
from ics_demo.routes import urls

application = tornado.web.Application(urls)

if __name__ == "__main__":
    init_db()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
