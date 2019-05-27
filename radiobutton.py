from tkinter import *
a=Tk()
def mm():
    a=v.get()
    if (a==1):
        a1=Tk()
        a1.title("Infosys")
        l1=Label(a1,text="Welcome to infosys",font=('arial',20,'italic'))
        l1.pack()
    elif(a==2):
         a1=Tk()
         a1.title('Wipro')
         l1=Label(a1,text="Welcome to Wipro",fonr=('roman',20,'bold'))
         l1.pack()
a.title("What You Look")

v=IntVar()
v.set(3)
label=Label(a,text='What IT Company your looking for',padx=25,justify=LEFT).pack(anchor=W)
radiobutton1=Radiobutton(a,text='Infosys',padx=25,variable=v,value=1).pack(anchor=W)
radiobutton2=Radiobutton(a,text='Wipro',padx=25,variable=v,value=2).pack(anchor=W)
radiobutton3=Radiobutton(a,text='TCS',padx=25,variable=v,value=3).pack(anchor=W)
radiobutton4=Radiobutton(a,text='CTS',padx=25,variable=v,value=4).pack(anchor=W)
a.mainloop()
