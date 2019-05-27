Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=4
>>> a='hello'
>>> b="world"
>>> print(a+b)
helloworld
>>> a=a.upper()
>>> a.upper()
'HELLO'
>>> a=a.upper()
>>> b.upper()
'WORLD'
>>> len[b]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    len[b]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len(b)
5
>>> a(4)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a(4)
TypeError: 'str' object is not callable
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a[5]
IndexError: string index out of range
>>> a[7]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[7]
IndexError: string index out of range
>>> 
