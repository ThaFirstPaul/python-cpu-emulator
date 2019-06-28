import time
class motherboard():
    def __init__(self, bus, clockwait, regA, regB, regi, pcntr, icntr, fReg, mem, display=None, running=True):

        self.bus = bus
        self.clockwait = clockwait
        self.regA = regA
        self.regB = regB
        self.fReg = fReg
        self.mem = mem
        self.disp = display

        self.pc = pcntr ##program counter
        self.ic = icntr ##instruction counter
        self.ir = regi ## instruction register
        self.running = running

        self.debug = 1
        

        print("Motherboard created")
        

    def start(self):
        while self.running:
            self.step()
            if self.debug:
                print("pc={}  ic={}  bus={}  mem_addr={} mem_data={} regA={} disp={}".format(self.pc.state, self.ic.state, self.bus.state, self.mem.ap, self.mem.mem[self.mem.ap], self.regA.state, self.disp.displaystate), end='\r')
                self.c = input()
            else:
                time.sleep(self.clockwait)

    def step(self):
        if self.ic.state == 7:
            self.ic.state = 1
        else: self.ic.state +=1
        
        self.exc()
        
        
        
    def exc(self):
        if self.ic.state == 1:
            self.pc.get()
            self.mem.set_ap()
        elif self.ic.state == 2:
            self.mem.get()
            self.ir.set()
            self.pc.up()
        else:
            struc = self.ir.state[0:4]
            addr = self.ir.state[4:8]

            

            if struc == "0001":
                if self.ic.state == 3:
                    self.bus.state = addr.zfill(8)
                    self.mem.set_ap()
                elif self.ic.state == 4:
                    self.mem.get()
                    self.regA.set()
                    self.ic.state = 7
                    
            elif struc == "0011":
                if self.ic.state == 3:
                    self.bus.state = self.c.zfill(8)
                    self.regA.set()
                    self.ic.state = 7
                    
                
            elif struc == "1101":
                if self.ic.state == 3:
                    self.bus.state = addr.zfill(8)
                    self.pc.set()
                    self.ic.state = 7
                    
            elif struc == "1110":
                if self.ic.state == 3:
                    self.regA.get()
                    self.disp.set()
                elif self.ic.state == 4:
                    self.mem.get()
                    self.ic.state = 7
            elif struc == "1111":
                if self.ic.state == 3:
                    self.running = False

