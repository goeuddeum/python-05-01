Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a[1, 2, 3, 4, 5]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a[1, 2, 3, 4, 5]
NameError: name 'a' is not defined
>>> a[0:2]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[0:2]
NameError: name 'a' is not defined
>>> a=[1, 2, 3, 4, 5]
>>> a[0:2]
[1, 2]
>>> a="12345"
>>> a[0:2]
'12'
>>> 
>>> a=1, 2, 3, 4, 5]
SyntaxError: unmatched ']'
>>> a=[1, 2, 3, 4, 5]
>>> b=a[:2]
>>> c=a[2:]
>>> c
[3, 4, 5]
