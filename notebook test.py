from tkinter import *
from tkinter import ttk , BOTH
import main_gui_classed as mainn

root = Tk()
root.title("16-bit Computer")

noteframe = ttk.Notebook(root)


main = mainn.main(noteframe)
writer = Frame(noteframe)
other1 = Frame(noteframe)
other2 = Frame(noteframe)

noteframe.add(main, text="Main")
noteframe.add(writer, text="Writer")
noteframe.add(other1, text="Other1")
noteframe.add(other2, text="Other2")


noteframe.pack(fill=BOTH, expand=True)





txt2 = Text(writer, borderwidth=1, relief="sunken", background="cyan", wrap=WORD)
txt2.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)


canvas = Canvas(other1)
canvas.create_text(10, 10, anchor=W, font="Papyrus", text="'Ello m8")

canvas.create_rectangle(70, 50, 160, 120, outline="#fb0", fill="#fb0")
canvas.create_rectangle(190, 50, 280, 120, outline="#f50", fill="#f50")
canvas.create_rectangle(310, 50, 410, 120, outline="#05f", fill="#05f")
canvas.pack(fill=BOTH, expand=1)


scale = Scale(other2, from_=10, to=1, resolution=-1)

scale.pack(side=LEFT, padx=15)



noteframe.focus_force()

root.mainloop()

