import time
from tkinter import *
from tkinter import simpledialog

from alu import alu as alog
from register import register
from motherboard import motherboard
from ram import ram
from digitmodule import digitmodule
from flag import flag
from counter import counter

class bus_:
    def __init__(self):
        self.state="0000000000000000"
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
    stepping = False
    debug = True
    
    bus = bus_()
    regA = register("A", bus)
    regi = register("Instruction", bus)
    pcntr = counter("Program Counter" ,bus, 1023)
    icntr = counter("Instrunction Counter", bus, 4)
    z_flag = flag()
    c_flag = flag()
    alu = alog("ALU", bus, regA, None, z_flag, c_flag)
    mem = ram(bus)
    disp = digitmodule(bus, "disp")
    inp = inp_(bus)

    mb = motherboard(bus, 1.5, regA, None, alu, regi, pcntr, icntr, z_flag, c_flag, mem, disp, inp)

    f = open("/Users/paulvonlutzow/Desktop/MyContent/Programming/Python/16bit-singlebus-computer/hdd.txt","r")
    c = f.read().split("\n")
    f.close()
    ii = 0
    for i in c:
        mem.mem[ii] = i.split("\t")[0]
        ii +=1

    
    def step():
        mb.step()
        #update gui
        bus_state.config(text=bus.state)
        memlist.delete(mem.ap)
        memlist.insert(mem.ap, "{}: {}".format(str(mem.ap).zfill(2),mem.mem[mem.ap]))
        
        memlist.selection_clear(0, END)
        memlist.select_set(pcntr.state)

        ap_state.config(text=mem.ap)
        disp_state.config(text=disp.state)
        disp_digit.config(text=disp.displaystate)
        pc_state.config(text="{} : {}".format(pcntr.state,icntr.state))
        rega_state.config(text=regA.state)
        inreg_state.config(text=regi.state)

    def start():
        global stepping
        stepping = True
        clock_status.config(text="Status: Stepping")
        while stepping:
            
            step()
            root.update()
    
#            if (mb.running == False):
#                stepping = False

    def stop(*args):
        global stepping
        stepping = False
        clock_status.config(text="Status: Halted")
    
    def exc(*args):
        c = simpledialog.askstring("Exec", "Execute a command:")
        exec(c)
    
    def ldhdd(*args):
        f = open("/Users/paulvonlutzow/Desktop/MyContent/Programming/Python/16bit-singlebus-computer/hdd.txt","r")
        c = f.read().split("\n")
        f.close()
        ii = 0
        memlist.delete(0,END)
        for i in c:
            mem.mem[ii] = i.split("\t")[0]
            memlist.insert(END, "{}: {}".format(str(ii).zfill(2),i.split("\t")[0]))
            ii +=1


    def editmem(*args):
        index = args[0].widget.index(ACTIVE)
        c = simpledialog.askstring("Edit memory", "Enter the 16-bit value for this mem")
        if c == "0":
            c = "0000000000000000"
        elif c == None or len(c) != 16:
            return
        for i in c:
            if (i == "0" or i == "1") == False:
                return
        memlist.insert(ACTIVE, "{}: {}".format(str(index).zfill(2), c))
        memlist.delete(ACTIVE)
        mem.mem[index] = str(c)

    def setinp(event):
        try:
            sv.set(ord(event.char))
            inp.set(format(ord(event.char), '016b'))
        except:
            pass

    def resetinp(event):
        sv.set(0)
        inp.set("0000000000000000")

    root = Tk()
    root.geometry("860x270")
    
    sv = IntVar()
    sv.set(0)
    
    #memory
    memlabel = Label(root, text="Memory", borderwidth=2, relief="groove")
    memlabel.place(x=24,y=0)
    mem_button = Button(root, text="Reload HDD", command=ldhdd)
    mem_button.place(x=100, y=1)
    memlist = Listbox(root, height =16, width =38, font="Courier")
    memlist.place(x=0, y=24)
    for i in range(0,1024):
        memlist.insert(END, "{}: {}".format(str(i).zfill(2),mem.mem[i]))

    ap_state = Label(root, text="0000000000")
    ap_state.place(x=0, y=250)

    memlist.bind("<Double-Button-1>",editmem)
    memlist.bind("<Button-1>",stop)
    memlist.bind("<Button-2>",set_ip)

    #bus
    bus_label = Label(root, text ="Bus", borderwidth=2, relief="groove")
    bus_label.place(x=320,y=0)
    bus_state = Label(root, text="0000000000000000")
    bus_state.place(x=320,y=24)

    #display
    disp_label = Label(root, text ="Display", borderwidth=2, relief="groove")
    disp_label.place(x=320,y=60)
    disp_state = Label(root, text="0000")
    disp_state.place(x=320,y=84)
    disp_digit = Label(root, text="0")
    disp_digit.place(x=320,y=108)

    #clock buttons
    clock_label = Label(root, text="Clock", borderwidth=2, relief="groove")
    clock_label.place(x=490,y=0)
    clock_status = Label(root, text="Status: Halted")
    clock_status.place(x=470,y=24)
    clock_step = Button(root, text="Step once",command=step)
    clock_step.place(x=470, y=48)
    clock_start = Button(root, text="Start",command=start)
    clock_start.place(x=470, y=72)
    clock_stop = Button(root, text="Stop",command=stop)
    clock_stop.place(x=470, y=96)

    #counters
    pc_label = Label(root, text ="P. : I. Counter", borderwidth=2, relief="groove")
    pc_label.place(x=590,y=0)
    pc_state = Label(root, text="0 : 0")
    pc_state.place(x=590,y=24)
    
    #registers
    rega_label = Label(root, text ="RegA", borderwidth=2, relief="groove")
    rega_label.place(x=590,y=60)
    rega_state = Label(root, text="0000000000000000")
    rega_state.place(x=590,y=84)

    inreg_label = Label(root, text ="I. Register", borderwidth=2, relief="groove")
    inreg_label.place(x=710,y=0)
    inreg_state = Label(root, text="0000000000000000")
    inreg_state.place(x=710,y=24)

    exec_button = Button(root, text="Exec", command=exc)
    exec_button.place(x=470, y=200)

    #input
    inpu_label = Label(root, text ="Input", borderwidth=2, relief="groove")
    inpu_label.place(x=320,y=170)
    inpu_state = Label(root, text="-", textvariable=sv)
    inpu_state.place(x=320,y=194)

    #other
    ips = Label(root, text="IPS: 0")
    ips.place(x=470, y=170)



    root.bind("<Key>",setinp)

    mainloop()
    #root.update()
##          get = put data on bus
##          set = set data from bus
##  format(number, '<fill zeros>b')
##  int(binary, 2)
