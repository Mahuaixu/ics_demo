
class Ear(object):
    def __init__(self, name):
        self.name = name

class Rabbit(object):
    def __init__(self, name):
        self.name = name
        self.ears = [Ear('left'), Ear('right')]
