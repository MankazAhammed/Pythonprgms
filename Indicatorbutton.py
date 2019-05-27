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
companies=[('Infosys',1),('Wipro',2),('TCS',3)]
Label(a,text="Choose a Company",padx=25,justify=LEFT).pack(anchor=W)
for txt,val in companies:
    Radiobutton(text=txt,padx=25,indicatoron=0,width=25,variable=v,command=mm,value=val).pack(anchor=W)
    
a.mainloop()
