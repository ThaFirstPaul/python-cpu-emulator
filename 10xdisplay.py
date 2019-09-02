import tkinter as tk

class digitmodule():
    def __init__(self, bus, name):
        self.name = name
        self.bus = bus
        self.state = "00000000"
        self.displaystate = "0"
        
        print("Display module \"{}\" created.".format(self.name))

    def getdisplay(self):
        self.bus.state = self.state

    def set(self):
        self.displaystate = str(int(self.bus.state, 2))
        
        self.state = self.bus.state

    def reset(self):
        self.state = "00000000"
        self.displaystate = "0"

class addon_screen(tk.Frame): # Externally tkinter-controlled screen
    def __init__(self, parent, size=1000):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        size = size /10

        w = tk.Canvas(self, width=size*10, height=size*10)
        w.pack()
        for i in range(10):
            for j in range(10):
                w.create_rectangle(i*size, j*size, i*size+size, j*size+size, fill='black', activefill='white', outline='')



class screen(): # Externally tkinter-controlled screen
    def __init__(self, name, bus, size=1024):
        self.name = name
        self.pixlrow = 0
        self.pixlcol = 0
        self.bus = bus

        
        self.root = tk.Tk()
        size = size /128

        w = tk.Canvas(self.root, width=size*10, height=size*10)
        w.pack(expand=False)
        for i in range(128):
            for j in range(128):
                w.create_rectangle(i*size, j*size, i*size+size, j*size+size, fill='black', activefill='white', outline='')

    def setpixlrow(self, row):
        self.pixlrow = row

    def setpixlcol(self, col):
        self.pixlcol = col

    def setcol(self):
        self.pixlcol = intself.bus)*32
        
    

if __name__ == '__main__':
    f = screen('alice')
##    while True:
##        f.update()
    
##    root = tk.Tk()
##    MainApplication(root, size= 50).pack(side="top", fill="both", expand=True)
##    root.mainloop()
