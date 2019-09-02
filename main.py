import math
from alu import alu as alog
from register import register
from motherboard import motherboard
from ram import ram
from digitmodule import digitmodule
from flag import flag
from counter import counter

class bus_:
    def __init__(self):
        self.state="00000000"
        print("Bus initialised!")

class inp_:
    def __init__(self, bus):
        self.state="0000000000000000"
        self.bus = bus
        print("Input initialised!")

    def get(self):
        print(self.state)
        self.bus.state = self.state

    def set(self, to):
        self.state = to
        
if __name__ == "__main__":
    bus = bus_()
    regA = register("A", bus)
    regi = register("Instruction", bus)
    pcntr = counter("pcntr", bus, 15)
    icntr = counter("icntr", bus, 4)
    mem = ram(bus)
    disp = digitmodule(bus, "disp")
    z_flag = flag()
    c_flag = flag()
    alu = alog("ALU", bus, regA, None, z_flag, c_flag)
    inp = inp_(bus)

    mb = motherboard(bus, 1.5, regA, None, alu, regi, pcntr, icntr, z_flag, c_flag, mem, disp, inp)

    mem.mem[0] = "00110000"
    mem.mem[1] = "11100000"
    mem.mem[2] = "11010000"
    
    mem.mem[8] = "00000001"
    mb.start(auto=True)

##          get = put data on bus
##          set = set data from bus
##  format(number, '<fill zeros>b')
##  int(binary, 2)
##
##  LDA <addr>  0001    Load mem[addr] to regA
##  ADD <addr>  0010    Add mem[addr] to regA
##  INP         0011    Stores an inputted value in regA  
##  JMP <value> 1101    Set program counter to value
##  OUT         1110    Display regA to Display
##  HALT        1111    Halt the clock
##

