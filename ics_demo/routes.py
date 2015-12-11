from ics_demo.handlers import BaseHandler
from ics_demo.handlers import DemoBaseHandler, DemoRabbitHandler

urls = [
    (r"/", BaseHandler),
    (r"/demo", DemoBaseHandler),
    (r"/demo/rabbit", DemoRabbitHandler),
]
