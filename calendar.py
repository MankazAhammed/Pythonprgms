Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import calender
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
>>> import calendar
>>> calendar.isleap(2020)
True
>>> calendar.month(2020,8)
'    August 2020\nMo Tu We Th Fr Sa Su\n                1  2\n 3  4  5  6  7  8  9\n10 11 12 13 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30\n31\n'
>>> print(calendar.month(2020,8))
    August 2020
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

>>> calendar.calendar(2020,2,1,10)
'                                      2020\n\n      January                       February                       March\nMo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                          1  2                             1\n 6  7  8  9 10 11 12           3  4  5  6  7  8  9           2  3  4  5  6  7  8\n13 14 15 16 17 18 19          10 11 12 13 14 15 16           9 10 11 12 13 14 15\n20 21 22 23 24 25 26          17 18 19 20 21 22 23          16 17 18 19 20 21 22\n27 28 29 30 31                24 25 26 27 28 29             23 24 25 26 27 28 29\n                                                            30 31\n\n       April                          May                           June\nMo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                       1  2  3           1  2  3  4  5  6  7\n 6  7  8  9 10 11 12           4  5  6  7  8  9 10           8  9 10 11 12 13 14\n13 14 15 16 17 18 19          11 12 13 14 15 16 17          15 16 17 18 19 20 21\n20 21 22 23 24 25 26          18 19 20 21 22 23 24          22 23 24 25 26 27 28\n27 28 29 30                   25 26 27 28 29 30 31          29 30\n\n        July                         August                      September\nMo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su\n       1  2  3  4  5                          1  2              1  2  3  4  5  6\n 6  7  8  9 10 11 12           3  4  5  6  7  8  9           7  8  9 10 11 12 13\n13 14 15 16 17 18 19          10 11 12 13 14 15 16          14 15 16 17 18 19 20\n20 21 22 23 24 25 26          17 18 19 20 21 22 23          21 22 23 24 25 26 27\n27 28 29 30 31                24 25 26 27 28 29 30          28 29 30\n                              31\n\n      October                       November                      December\nMo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su\n          1  2  3  4                             1              1  2  3  4  5  6\n 5  6  7  8  9 10 11           2  3  4  5  6  7  8           7  8  9 10 11 12 13\n12 13 14 15 16 17 18           9 10 11 12 13 14 15          14 15 16 17 18 19 20\n19 20 21 22 23 24 25          16 17 18 19 20 21 22          21 22 23 24 25 26 27\n26 27 28 29 30 31             23 24 25 26 27 28 29          28 29 30 31\n                              30\n'
>>> print(calendar.calendar(2020,2,1,10))
                                      2020

      January                       February                       March
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
       1  2  3  4  5                          1  2                             1
 6  7  8  9 10 11 12           3  4  5  6  7  8  9           2  3  4  5  6  7  8
13 14 15 16 17 18 19          10 11 12 13 14 15 16           9 10 11 12 13 14 15
20 21 22 23 24 25 26          17 18 19 20 21 22 23          16 17 18 19 20 21 22
27 28 29 30 31                24 25 26 27 28 29             23 24 25 26 27 28 29
                                                            30 31

       April                          May                           June
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
       1  2  3  4  5                       1  2  3           1  2  3  4  5  6  7
 6  7  8  9 10 11 12           4  5  6  7  8  9 10           8  9 10 11 12 13 14
13 14 15 16 17 18 19          11 12 13 14 15 16 17          15 16 17 18 19 20 21
20 21 22 23 24 25 26          18 19 20 21 22 23 24          22 23 24 25 26 27 28
27 28 29 30                   25 26 27 28 29 30 31          29 30

        July                         August                      September
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
       1  2  3  4  5                          1  2              1  2  3  4  5  6
 6  7  8  9 10 11 12           3  4  5  6  7  8  9           7  8  9 10 11 12 13
13 14 15 16 17 18 19          10 11 12 13 14 15 16          14 15 16 17 18 19 20
20 21 22 23 24 25 26          17 18 19 20 21 22 23          21 22 23 24 25 26 27
27 28 29 30 31                24 25 26 27 28 29 30          28 29 30
                              31

      October                       November                      December
Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su          Mo Tu We Th Fr Sa Su
          1  2  3  4                             1              1  2  3  4  5  6
 5  6  7  8  9 10 11           2  3  4  5  6  7  8           7  8  9 10 11 12 13
12 13 14 15 16 17 18           9 10 11 12 13 14 15          14 15 16 17 18 19 20
19 20 21 22 23 24 25          16 17 18 19 20 21 22          21 22 23 24 25 26 27
26 27 28 29 30 31             23 24 25 26 27 28 29          28 29 30 31
                              30

>>> 
