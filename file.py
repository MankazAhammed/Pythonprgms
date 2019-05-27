Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=open('c:/text/a.txt','w')
>>> a.write("This is spiderman")
17
>>> a.close()
>>> a=open('c:/text/aa.txt','r')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a=open('c:/text/aa.txt','r')
FileNotFoundError: [Errno 2] No such file or directory: 'c:/text/aa.txt'
>>> a=open('c:/text/a.txt','r')
>>> a.read()
'This is spiderman'
>>> 
