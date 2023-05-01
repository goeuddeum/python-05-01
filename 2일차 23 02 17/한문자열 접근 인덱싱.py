Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'hello'[0]
'h'
>>> 'hello'[1]
'e'
>>> 'hello'[4]
'o'
>>> 'hello'[5]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    'hello'[5]
IndexError: string index out of range
>>> 'hello'[-0]
'h'
>>> 'hello'[-1]
'o'
>>> 'hello'[-2]
'l'
>>> 'hello'[-5]
'h'
>>> 'hello'[-6]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    'hello'[-6]
IndexError: string index out of range
