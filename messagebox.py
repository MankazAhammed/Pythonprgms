from tkinter import *
a=Tk()
def hello():
    c=b.get()
    myLabel3=Label(text="WAHOO",fg='blue',bg='yellow',font=("Arial",12,"B")).pack()
def dele():
    myLabel1=Label(text="Yahoo",fg='blue',bg='yellow',font=("roman",12,"i")).pack()
def newfi():
    myLabel1=Label(text="Clicked",font=10).pack()
def sfil():
    messagebox.showinfo(title="Save",message="Are You Sure You Want to Save")
def mquit():
    m=messagebox.askyesno(title="Quit",message="Are You Sure To Quit")
    if m==1:
        a.destroy()
b=StringVar()
a.title("Infosys")
a.geometry("500x500+100+10")
myLabel1=Label(a,text="Registration",fg='blue',bg='yellow').pack()
myButton1=Button(a,text="Submit",fg='black',bg='blue',command=hello,font=10).pack()
myButton2=Button(a,text="Cancel",fg='black',bg='blue',command=dele,font=10).pack()
text=Entry(textvariable=b).pack()
mymenu=Menu()
listone=Menu()
listone.add_command(label="New File",command=newfi)
listone.add_command(label="Open File")
listone.add_command(label="Save File",command=sfil)
listone.add_command(label="Quit",command=mquit)
listtwo=Menu()
listtwo.add_command(label="Undo")
listtwo.add_command(label="redo")
mymenu.add_cascade(label="File",menu=listone)
mymenu.add_cascade(label="Edit",menu=listtwo)
mymenu.add_cascade(label="Format")
mymenu.add_cascade(label="Run")
a.config(menu=mymenu)
a.mainloop()
