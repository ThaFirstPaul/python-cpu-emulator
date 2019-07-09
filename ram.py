class ram():
    def __init__(self, bus):
        self.bus = bus
        self.mem = []
        for i in range(0,1024):
            self.mem.append("0000000000000000")
        self.ap = 0

        print("Random Access Memory created.")

    def get(self):
        self.bus.state = self.mem[self.ap]

    def set(self):
        s = self.mem[self.ap]
        self.mem[self.ap] = self.bus.state

    def set_ap(self):
        self.ap = int(self.bus.state, 2)

    def get_ap(self):
        self.bus.state = format(self.ap, '016b')
