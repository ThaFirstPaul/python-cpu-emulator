class digitmodule():
    def __init__(self, bus, name):
        self.name = name
        self.bus = bus
        self.state = "0000"
        self.displaystate = "0"
        
        print("Display module \"{}\" created.".format(self.name))

    def getdisplay(self):
        self.bus.state = self.state

    def set(self):
        self.state = self.bus
        if int(self.bus.state, 2) < 10:
            self.displaystate = str(int(self.bus.state, 2))
        else:
            ls = ["a","b","c","d","e","f"]
            self.displaystate = ls[int(self.bus.state, 2)-10]
        print("Digit display \"{}\" updated to: {}".format(self.name, self.displaystate))

