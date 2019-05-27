from tkinter import *
a=Tk()
def mcol():
    color=colorchooser.askcolor()
    label=Label(text="Color is",bg=color[1]).pack()
button=Button(text="Choosen color",width=30,command=mcol).pack()
a.mainloop()
