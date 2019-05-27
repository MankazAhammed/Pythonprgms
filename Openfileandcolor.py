from tkinter import *
a=Tk()
def mcolor():
    color=colorchooser.askcolor()
    label=Label(text="Your choosen color",bg=color[1]).pack()
def mfileopen():
    file1=filedialog.askopenfile()
    label=Label(text=file).pack()

button=Button(text="Choose Color",width=30,command=mcolor).pack()
button=Button(text="Open File",width=30,command=mfileopen).pack()

a.mainloop()
