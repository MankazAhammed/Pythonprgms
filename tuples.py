Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup1=(1,2,3,4,5)
>>> tup2=('john',60,43)
>>> tup2
('john', 60, 43)
>>> tup1
(1, 2, 3, 4, 5)
>>> tup1[3]
4
>>> l=tup1
>>> l
(1, 2, 3, 4, 5)
>>> tup1
(1, 2, 3, 4, 5)
>>> tup1.count()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tup1.count()
TypeError: count() takes exactly one argument (0 given)
>>> tup1.index()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tup1.index()
TypeError: index() takes at least 1 argument (0 given)
>>> tup1.index(2)
1
>>> 
