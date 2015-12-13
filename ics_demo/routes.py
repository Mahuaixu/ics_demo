from ics_demo.handlers import BaseHandler
from ics_demo.handlers import DemoBaseHandler, DemoRabbitHandler, DemoCarrotHandler, DemoCorpsHandler

uuid_regex = "([0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})"

urls = [
    (r"/", BaseHandler),
    (r"/demo", DemoBaseHandler),
    (r"/demo/rabbit", DemoRabbitHandler),
    (r"/demo/rabbit/" + uuid_regex, DemoRabbitHandler),
    (r"/demo/carrot", DemoCarrotHandler),
    (r"/demo/carrot/" + uuid_regex, DemoCarrotHandler),
    (r"/demo/corps", DemoCorpsHandler),
    (r"/demo/corps/" + uuid_regex, DemoCorpsHandler),

]
