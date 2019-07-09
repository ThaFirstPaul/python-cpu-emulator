import math

class counter():
    def __init__(self, name, bus, upto):
        self.bus = bus
        self.mx = int(math.log2(math.sqrt(upto+1)))
        self.state = 0
        self.upto = upto
        self.name = name

        print("Counter '{}' created.".format(name))

    def get(self):
        self.bus.state = format(self.state, '016b')

    def set(self):
        self.state = int(self.bus.state, 2)
        
    def up(self):
        if self.state == self.upto:
            self.state = 0
        else:
            self.state += 1
