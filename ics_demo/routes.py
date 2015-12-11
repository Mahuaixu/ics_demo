from ics_demo.handlers import BaseHandler
from ics_demo.handlers import DemoBaseHandler, DemoRabbitHandler, DemoCarrotHandler, DemoCorpsHandler

urls = [
    (r"/", BaseHandler),
    (r"/demo", DemoBaseHandler),
    (r"/demo/rabbit", DemoRabbitHandler),
    (r"/demo/rabbit/([0-9]+)", DemoRabbitHandler),
    (r"/demo/carrot", DemoCarrotHandler),
    (r"/demo/carrot/([0-9]+)", DemoCarrotHandler),
    (r"/demo/corps", DemoCorpsHandler),
    (r"/demo/corps/([0-9]+)", DemoCorpsHandler),

]
