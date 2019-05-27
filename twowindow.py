from tkinter import *
a=Tk()
s=Tk()
def hello():
    myLabel1=Label(text="Hell",fg='black',bg='red',font=10).pack()

def Dele():
    myLabel2=Label(text="heaven",fg='black',bg='green',font=10).pack()
d=StringVar()
a.title("First")
s.title("Second")
myLabel2=Label(a,text='Welcome',fg='black',bg='blue',font=10).pack()
myButton1=Button(a,text='Click',fg='yellow',bg='green',command=hello,font=10).pack()
myButton2=Button(s,text='Dont click',fg='yellow',bg='green',command=dele,font=10).pack()
text=Entry(a,textvariable=d).pack()
a.mainloop()
s.mainloop()
