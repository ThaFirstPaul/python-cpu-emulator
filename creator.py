import time, csv
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

if __name__ == "__main__":
    
    #inss = dict({'NUL': '000000', 'LDA': '000001', 'SVA': '000010', 'ADD': '000011', 'SUB': '000100', 'SET': '000101', 'JMP': '001000', 'JPE': '001001', 'OTA': '001010', 'INA': '001100', 'HOL': '111110', 'HAL': '111111'})
    inss = dict()
    meanings = dict()
    nons = []
    ins_dict= []
    
    try:
        with open('Mnemonics.csv') as csv_file:
            mnemonics = csv.reader(csv_file, delimiter=';')
            line_count = 0
            print(mnemonics)
            
            for row in mnemonics:
                if line_count == 0: line_count = 1; continue
                if row[1] == '': continue
                inss[row[1][0:3]] = row[0]
                meanings[row[0]] = row[3]
                if row[2] == '': nons.append(row[0])

    except FileNotFoundError:
        messagebox.showerror("Creator","Error! 'Mnemonics.csv' not found, is it in the same directory?\n\nWill now load Creator with default Instruction Set.")
        inss = dict({'NUL': '000000', 'LDA': '000001', 'SVA': '000010', 'ADD': '000011', 'SUB': '000100', 'SET': '000101', 'JMP': '001000', 'JPE': '001001', 'OTA': '001010', 'INA': '001100', 'HOL': '111110', 'HAL': '111111'})
        meanings = dict({'000000': 'Does nothing', '000001': 'Load mem[addr] to regA', '000010': 'Stores regA to mem[addr]', '000011': 'Add mem[addr] to regA', '000100': 'Subtract mem[addr] from regA', '000101': 'Load [num] to regA', '001000': 'Set program counter to value', '001001': 'Set program counter to value if z_flag = 0', '001010': 'Display regA to Display','001100': ' Store input from selected device to RegA', '111110': 'Pauses the computer for [num] milliseconds', '111111': 'Halts the computer'})
        nons = ["000000", "001010", "001100", "111111"]
	
    undo_history = []
    valid_value = False
    
    def callback(*args):
        global valid_value
        valid_value = False
        c = v_in.get()
        info.config(text="Info: ")
        try:
            int(c,2)
            if len(c) > 16:
                v_out.set("Too many characters!")
                return
            v_out.set(format(int(c,2), '016b'))
            valid_value = True
            return
        except ValueError: pass
        if len(c) < 3:
            v_out.set("Not enough characters!")
        instruc = c[:3].upper()
        if not (instruc in inss.keys()):
            v_out.set("Not a valid instuction!")
            return
        instruc_b = inss.get(instruc)
        info.config(text="Info: " + meanings.get(instruc_b))
        if instruc_b in nons:
            valid_value = True
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
        valid_value = True
        valu = format(valu, '010b')
        v_out.set(instruc_b + valu)

    def ins(*args):
        if valid_value:
            memlist.insert(END, v_out.get())

    def toshow(*args):
        for i, j in inss.items():
            if j == memlist.get(ACTIVE)[0:6]:
                instr = i
                break
        else:
            instr = memlist.get(ACTIVE)[0:6]

        if opt.get() == "DEC": valu = int(memlist.get(ACTIVE)[6:], 2)
        elif opt.get() == "HEX": valu = "{0:x}".format(int(memlist.get(ACTIVE)[6:], 2))
        elif opt.get() == "BIN": valu = memlist.get(ACTIVE)[6:]
        
        v_in.set(instr + str(valu))
        callback()

    def setin(*args):
        v_in.set(alllist.get(ACTIVE)[0:3]+ " ")
        e.focus_set()
        e.icursor(END)

    def move(movetoindex):
        memlist.t
        tkinter.Listbox.index

    def moveup(*args):
        move(memlist.index - 1)

    def movedown(*args):
        move(memlist.index + 1)

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
    menu.add_command(label="Copy", command=toclip)
    menu.add_command(label="Move up", command=moveup)
    menu.add_command(label="Move down", command=movedown)

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
    
    mem_frame = Frame(root)
    mem_frame.pack(side="top")
    memlabel = Label(mem_frame, text="Recent", borderwidth=2, relief="groove")
    memlabel.pack(padx=10, pady=5, side="left")
    savebutton = Button(mem_frame, text="Write", state=DISABLED)
    savebutton.pack(padx=10, pady=5, side="left")
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
    memlist.bind("<1>", toshow)
    memlist.bind("<Double-Button-1>", toshow)
    memlist.bind("<2>", toclip)
    memlist.bind("<3>",showmenu)
    memlist.bind("<BackSpace>", dele)
    
    alllist.bind("<Double-Button-1>",setin)

    write = messagebox.askokcancel("Creator","Would you like to open with write enabled?")
    if write:
        try:
            import writer
            print(writer.__name__)
            write_handler = writer.writer('hdd.txt')
            messagebox.showinfo("Creator","Success! Creator loaded with write enabled.")
            for stri in write_handler.getraw():
                memlist.insert(END, stri)
            def save(*args):
                 if memlist.size() > 0:
                     write_handler.write(memlist.get(0,END))
                
            savebutton.config(state="normal", command=save)
        except FileNotFoundError as e:
            write = False
            print('Error: ' + e.args[0])
            messagebox.showerror("Creator","Error! 'hdd.txt' not found, is it in the same directory?\n\nWill now load Creator without write enabled.")
        except ModuleNotFoundError:
            write = False
            messagebox.showerror("Creator","Error! Could not load write module, is it in the same directory?\n\nWill now load Creator without write enabled.")

    root.mainloop()

