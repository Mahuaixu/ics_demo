from ics_demo.handlers import BaseHandler
from ics_demo.handlers import DemoHandler

urls = [
    (r"/", BaseHandler),
    (r"/demo", DemoHandler),
]
