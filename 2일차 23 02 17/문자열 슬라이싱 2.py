Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='20010331Rainy"
SyntaxError: incomplete input
>>> a=:20010331Rainy"
SyntaxError: invalid decimal literal
>>> a="20010331Rainy"
>>> date=a[:8]
>>> weather = a[8:]
>>> date
'20010331'
>>> weather
'Rainy'
>>> year=a[:4]
>>> day=a[4:8]
>>> year
'2001'
>>> day
'0331'
>>> weather
'Rainy'
>>> a='Pithon"
SyntaxError: incomplete input
>>> a="pithon"
>>> a[1]
'i'
>>> a[1]='y'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a[1]='y'
TypeError: 'str' object does not support item assignment
>>> a="pithon"
>>> a[:1]
'p'
>>> a[2:]
'thon'
>>> a[:1] + 'y' + a[2:]
'python'
