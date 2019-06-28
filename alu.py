class alu():
    def __init__(self, name, bus, regA, regB, z_flag, c_flag):
        self.bus = bus
        self.mode = "0000"
        self.regA = regA
        self.regB = regB
        self.zflag = z_flag
        self.cflag = c_flag
        self.state = "00000000"
        
        # mode    logic           description
        # 0000    addition        adds regA and regB
        # 0001    subtraction     subtracts regB from regA
        # 0010
        # 0011

        print("ALU \"{}\" created.".format(name))

    def get(self):
        if self.mode == "0000":
            num_ = int(self.regA.state, 2) + int(self.regB.state, 2)
            if num_ > 255:
                self.cflag.on


        
        self.bus.state = format(num , '008b')

    def setmode(self):
        self.state= self.bus.state
