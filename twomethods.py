Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import calender
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
>>> import calander
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import calander
ModuleNotFoundError: No module named 'calander'
>>> import calander
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import calander
ModuleNotFoundError: No module named 'calander'
>>> import calendar
>>> print
<built-in function print>
>>> print(calendar,month(2019,8))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(calendar,month(2019,8))
NameError: name 'month' is not defined
>>> import calendar
>>> print(calendar.month(2020,8))
    August 2020
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

>>> from calendar import *
>>> print(month(2020,8))
    August 2020
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

>>> pow(2,3)
8
>>> from math import *
>>> pow(2,4)
16.0
>>> 
