Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
>>> time.asctime
<built-in function asctime>
>>> time.asctime()
'Wed May 15 15:54:31 2019'
>>> time.time()
1557915894.587297
>>> lin=time.time()
>>> mes=time.time()
>>> lout=time.time()
>>> lin1=time.localtime(lin)
>>> mes=time.localtime(mes)
>>> lout1=time.localtime(lout)
>>> login=time.asctime(lin1)
>>> message=time.asctime(mes)
>>> logout=times.asctime(lout1)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    logout=times.asctime(lout1)
NameError: name 'times' is not defined
>>> logout=time.asctime(lout1)
>>> login
'Wed May 15 15:55:07 2019'
>>> message
'Wed May 15 15:55:21 2019'
>>> logout
'Wed May 15 15:55:50 2019'
>>> 
