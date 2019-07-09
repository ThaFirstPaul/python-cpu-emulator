class flagregister():
    def __init__(self, bus):
        self.state = ("0","0","0","0")
        #             | | |  \_CFlag
        #             | |  \_ZFlag
        #             |  \_
        #              \ 
        self.bus = bus

        print("Flag register created.")

    def get(self):
        self.bus.state = "".join(self.state).zfill(8)

    def reset(self):
        self.state = ("0","0","0","0")

    def enableFlag(self, flag):
        if flag == 0:
            self.state = (self.state[0], self.state[1], self.state[2], "1")
        elif flag == 1:
            self.state = (self.state[0], self.state[1], "1", self.state[3])
            
