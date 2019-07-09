class buttontmodule():
    def __init__(self, bus, name):
        self.name = name
        self.bus = bus
        self.state = "0000000000000000"
        
        print("Button \"{}\" created.".format(self.name))

    def get(self):
        self.bus.state = self.state
