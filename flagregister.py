class flagregister():
    def __init__(self, bus):
        fReg.state = "0000"
        self.name = name
        self.bus = bus

        print("Flag \"{}\" created.".format(self.name))

    def get(self):
        self.bus.state = self.state.zfill(8)

    def reset(self):
        self.state = "0000"

    def enableFlag(self, flag):
        if flag = 
