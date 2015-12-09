from ics_demo.handlers import BaseHandler
from ics_demo.pojo.demo import Rabbit

class DemoHandler(BaseHandler):
    def get(self):
        rabbit = Rabbit("BunnyKun")
        self.json_write(rabbit)
        
