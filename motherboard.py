import time
class motherboard():
    def __init__(self, bus, clockwait, regA, regB, alu, regi, pcntr, icntr, z_flag, c_flag, mem, display=None, inp=None, running=True):

        self.bus = bus
        self.clockwait = clockwait
        self.regA = regA
        self.regB = regB
        self.alu = alu
        self.c_flag = c_flag
        self.z_flag = z_flag
        self.mem = mem
        self.disp = display
        self.inp = inp

        self.pc = pcntr ##program counter
        self.ic = icntr ##instruction counter
        self.ir = regi ## instruction register
        self.running = running

        self.debug = 1
        

        print("Motherboard created")
        

    def start(self):
        while True:
            if self.running:
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
            struc = self.ir.state[0:6]   # Program
            addr = self.ir.state[6:16]   # 10bit address

            if struc == "000000":
                self.ic.state = 7

            elif struc == "000001":
                if self.ic.state == 3:
                    self.bus.state = addr.zfill(16)
                    self.mem.set_ap()
                elif self.ic.state == 4:
                    self.mem.get()
                    self.regA.set()
                    
                    self.ic.state = 7

            elif struc == "000010":
                if self.ic.state == 3:
                    self.bus.state = addr.zfill(16)
                    self.mem.set_ap()
                elif self.ic.state == 4:
                    self.regA.get()
                    self.mem.set()
                
                    self.ic.state = 7


            elif struc == "000011":
                if self.ic.state == 3:
                    self.bus.state = addr.zfill(16)
                    self.mem.set_ap()
                    self.alu.mode ="0000"
                elif self.ic.state == 4:
                    self.mem.get()
                    self.alu.process()
                    
                    self.ic.state = 7
                    
            elif struc == "000100":
                if self.ic.state == 3:
                    self.bus.state = addr.zfill(16)
                    self.mem.set_ap()
                    self.alu.mode ="0001"
                elif self.ic.state == 4:
                    self.mem.get()
                    self.alu.process()
                    
                    self.ic.state = 7
                    
            elif struc == "000101":
                if self.ic.state == 3:
                    self.bus.state = addr.zfill(16)
                    self.regA.set()
                    
                    self.ic.state = 7
                
            elif struc == "001000":
                if self.ic.state == 3:
                    self.bus.state = addr.zfill(16)
                    self.pc.set()
                    
                    self.ic.state = 7

            elif struc == "001001":
                if self.ic.state == 3:
                    self.bus.state = addr.zfill(16)
                    if self.z_flag.state == 1:
                        self.pc.set()
                    
                    self.ic.state = 7
                    
            elif struc == "001010":
                if self.ic.state == 3:
                    self.regA.get()
                    self.disp.set()
                elif self.ic.state == 4:
                    self.mem.get()
                    
                    self.ic.state = 7
            
            elif struc == "001100":
                if self.ic.state == 3:
                    self.inp.get()
                    self.inp.set("0000000000000000")
                    self.regA.set()
                    
                    self.ic.state = 7
                    
            elif struc == "111111":
                if self.ic.state == 3:
                    self.running = False

