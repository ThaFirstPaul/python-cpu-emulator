import time
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

if __name__ == "__main__":
    
    inss = dict({'NULL': '000000', 'LDA': '000001', 'SVA': '000010', 'ADD': '000011', 'SUB': '000100', 'SET': '000101', 'JMP': '001000', 'JPE': '001001', 'OTA': '001010', 'INA': '001100', 'HAL': '111111'})
    nons = ("000000", "001010", "001100","111111")
    meanings = dict({'000000': 'Does nothing', '000001': 'Load mem[addr] to regA', '000010': 'Stores regA to mem[addr]', '000011': 'Add mem[addr] to regA', '000100': 'Subtract mem[addr] from regA', '000101': 'Load [num] to regA', '001000': 'Set program counter to value', '001001': 'Set program counter to value if z_flag = 0', '001010': 'Display regA to Display','001100': ' Store input from selected device to RegA', '111111': 'Halts the computer'})
    undo_history = []
    valid_value = False
    last_valid_value = False
    
    def callback(*args):
        global last_valid_value, valid_value
        last_valid_value = valid_value
        valid_value = False
        
        c = v_in.get()
        info.config(text="Info: ")
        if len(c) < 3:
            v_out.set("Not enough characters!")
        instruc = c[:3].upper()
        if not (instruc in inss.keys()):
            v_out.set("Not a valid instuction!")
            
            return
        instruc_b = inss.get(instruc)
        info.config(text="Info: " + meanings.get(instruc_b))
        if instruc_b in nons:
            v_out.set(instruc_b + "0000000000")
            return
        try:
            if opt.get() == "DEC": valu = int(c[3:].strip())
            elif opt.get() == "HEX": valu = int(c[3:].strip(), 16)
            elif opt.get() == "BIN": valu = int(c[3:].strip(), 2)
        except ValueError:
            v_out.set("Not a Number!")
            return
        if valu > 1023:
            v_out.set("Address overflow!")
            return
        last_valid_value = True
        valu = format(valu, '010b')
        v_out.set(instruc_b + valu)


    

    def ins(*args):
        if last_valid_value:
            memlist.insert(END, v_out.get())

    def setin(*args):
        v_in.set(alllist.get(ACTIVE)[0:3]+ " ")
        e.focus_set()
        e.icursor(END)


    def toclip(*args):
        root.clipboard_clear()
        root.clipboard_append(memlist.get(ACTIVE))

    def showmenu(e ,*args):
        menu.post(e.x_root, e.y_root)

    def dele(*args):
        memlist.delete(ACTIVE)

    def delall(*args):
        memlist.delete(0, END)
    
    root = Tk()
    root.geometry("340x720")

    v_in = StringVar()
    v_out = StringVar()
    opt = StringVar()
    opt.set("DEC")

    menu = Menu(root, tearoff=0)
    menu.add_command(label="Delete", command=dele)
    menu.add_command(label="Clear", command=delall)

    info = Label(root, text="Info")
    info.pack(fill="x", padx=10, pady=5)
    entlabel = Entry(root, textvariable=v_out, state="readonly")
    entlabel.pack(padx=10, pady=5)
    
    
    e = Entry(root,textvariable=v_in)
    e.pack(fill="x", padx=10, pady=5)

    optlabel = Label(root, text="Value Type:", borderwidth=2, relief="groove")
    optlabel.pack(padx=10, pady=5)
    w = OptionMenu(root, opt, "DEC", "HEX", "BIN")
    w.pack(padx=10, pady=5)
    
    memlabel = Label(root, text="Recent", borderwidth=2, relief="groove")
    memlabel.pack(padx=10, pady=5)
    memlist = Listbox(root, height =16, width =40, font="Courier")
    memlist.pack(fill="x", padx=10, pady=5)

    alllabel = Label(root, text="All", borderwidth=2, relief="groove")
    alllabel.pack(padx=10, pady=5)
    alllist = Listbox(root, height =16, width =40, font="Courier")
    alllist.pack(fill="x", padx=10, pady=5)

    for i in inss:
        alllist.insert(END, "{}: {}".format(i, meanings[inss[i]]))
    
    v_in.trace_add("write", callback)
    opt.trace_add("write", callback)

    e.bind("<Return>", ins)
    memlist.bind("<Double-Button-1>", toclip)
    memlist.bind("<Button-2>",showmenu)
    memlist.bind("<BackSpace>", dele)

    alllist.bind("<Double-Button-1>",setin)

    root.mainloop()

