Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[]
>>> b[1,2,3]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    b[1,2,3]
NameError: name 'b' is not defined
>>> b=[1,2,3]
>>> c['Life', 'is', 'too', 'short']
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c['Life', 'is', 'too', 'short']
NameError: name 'c' is not defined
>>> d=[1, 2, 'Life', 'is']
>>> e=[1, 2, ['Life', 'is']]
