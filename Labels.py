Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> a=Tk()
>>> a.title("Hello")
''
>>> a.geometry("500x500+100+100")
''
>>> myLabel1=Label(text="Who are you",fg="red",bg="yellow")
>>> myLabel1.pack()
>>> myLabel2=Label(text="What you need",fg="green",bg="blue").pack()
>>> a.mainloop()
