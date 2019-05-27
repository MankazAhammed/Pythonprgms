Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> age={'john':40,'peter':50,'bob':44}
>>> age
{'john': 40, 'peter': 50, 'bob': 44}
>>> age['john']
40
>>> age['william']=20
>>> age
{'john': 40, 'peter': 50, 'bob': 44, 'william': 20}
>>> dict1={'john':"married",'peter':92,39243:23}
>>> dict1
{'john': 'married', 'peter': 92, 39243: 23}
>>> a=[1,2,3,4,5]
>>> b=[6,7,8,9]
>>> dict2={'a','b'}
>>> dict2
{'b', 'a'}
>>> dict2={'a':[1,2,3,4,5],'b'=[6,7,8,9]}
SyntaxError: invalid syntax
>>> dict2={'a':[1,2,3,4,5],'b':[6,7,8,9]}
>>> dict2
{'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9]}
>>> print(age['bob'])
44
>>> del age['bob']
>>> age
{'john': 40, 'peter': 50, 'william': 20}
>>> age.
