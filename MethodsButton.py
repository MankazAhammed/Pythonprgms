from tkinter import *
a=Tk()
def One():
    b=d.get()
    myLabel1=Label(text=d,fg='blue',bg='yellow',font=10).pack()
def Dead():
    e=c.get()
    myLabel1=Label(text=c,fg='black',bg='red',font=10).pack()
d=StringVar()
c=StringVar()
a.title("Xoxo")
a.geometry("500x500+100+100")
myLabel1=Label(text="Who are you!",fg='blue',bg='yellow',font=10).pack()
text1=Entry(textvariable=d).pack()
myButton1=Button(text='Submit',fg='black',bg='blue',command=One,font=10).pack()
text2=Entry(textvariable=c).pack()
myButton2=Button(text='Win Now',fg='blue',bg='green',command=Dead,font=10).pack()

a.mainloop()
