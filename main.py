import math
from register import register
from motherboard import motherboard
from ram import ram
from digitmodule import digitmodule
from flagregister import flagregister

class bus_:
    def __init__(self):
        self.state="00000000"
        print("Bus initialised!")

class counter():
    def __init__(self, bus, upto):
        self.bus = bus
        self.mx = int(math.log2(math.sqrt(upto+1)))
        self.state = 0

        print("Random Access Memory created.")

    def get(self):
        self.bus.state = format(self.state, '008b')

    def set(self):
        self.state = int(self.bus.state, 2)
        
    def up(self):
        self.state += 1
        
if __name__ == "__main__":
    bus = bus_()
    regA = register("A", bus)
    regi = register("Instruction", bus)
    pcntr = counter(bus, 15)
    icntr = counter(bus, 4)
    fReg = flagregister(bus)
    mem = ram(bus)
    disp = digitmodule(bus, "disp")

    mb = motherboard(bus, 1.5, regA, None, regi, pcntr, icntr, fReg, mem, disp)

    mem.mem[0] = "00110000"
    mem.mem[1] = "11100000"
    mem.mem[2] = "11010000"
    
    mem.mem[8] = "00000001"
    mb.start()

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

