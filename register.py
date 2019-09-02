class register():
    def __init__(self, name, bus):
        self.state = "0000000000000000"
        self.name = name
        self.bus = bus

        print("Register '{}' created.".format(self.name))

    def get(self):
        self.bus.state = self.state

    def set(self):
        self.state = self.bus.state

    def reset(self):
        self.state = "0000000000000000"
