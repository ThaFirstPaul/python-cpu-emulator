class alu():
    def __init__(self, name, bus, regA, regB, z_flag, c_flag):
        self.bus = bus
        self.mode = "0000"
        self.regA = regA
        self.regB = regB
        self.zflag = z_flag
        self.cflag = c_flag
        self.state = "0000000000000000"
        
        # mode    logic           description
        # 0000    addition        adds regA and bus >> regA
        # 0001    subtraction     subtracts bus from regA >> regA
        # 0010
        # 0011

        print("ALU '{}' created.".format(name))

    def process(self):
        if self.mode == "0000":
            num_ = int(self.regA.state, 2) + int(self.bus.state, 2)
##            print("adding {} + {}".format(int(self.regA.state, 2), int(self.bus.state, 2)))

        elif self.mode == "0001":
            num_ = int(self.regA.state, 2) - int(self.bus.state, 2)

        if (num_ < 0 or num_ >65535):
            self.cflag.set(1)
            num_ = num_ % 65535
        else: self.cflag.set(0)

        if num_ == 0:
            self.zflag.set(1)
        else: self.zflag.set(0)
        
        self.regA.state = format(num_ , '016b')


    def setmode(self, mode):
        self.mode = mode
            
