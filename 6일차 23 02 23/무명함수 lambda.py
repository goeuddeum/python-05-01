Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
f=lambda a,b:a*b
f(10,20)
200
f2=lambda a:a**2
f2(3)
9
f3=lambda a:a>2
f3(2)
False
f=lambda a, b=: a*b
SyntaxError: invalid syntax
f=lambda a, b: a*b
f(10,20)
200
m=map(lambda a: a**2,[1,2,3,4])
m
<map object at 0x000001C212C76EC0>
m=8M
SyntaxError: invalid decimal literal
M=8m
SyntaxError: invalid decimal literal
M=*M
SyntaxError: can't use starred expression here
M=[*M}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['

M=[*M]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    M=[*M]
NameError: name 'M' is not defined. Did you mean: 'm'?
m=[*m]
m
[1, 4, 9, 16]
f=lambda a:a**2
l=[1,2,3,4]
for m in map(f,1):
    m
... 
...     
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    for m in map(f,1):
TypeError: 'int' object is not iterable
>>> for m in map(f,l):
...     m
... 
...     
1
4
9
16
>>> f=filter(lambda a: a>2,[1,2,3,4])
>>> 
>>> f
<filter object at 0x000001C212C761D0>
>>> f=*f]
SyntaxError: unmatched ']'
>>> f=[*f]
>>> f
[3, 4]
>>> f=lambda a:a>2
>>> b=[1,2,3,4]
>>> for f in filter(f,1):
...     f
... 
...     
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for f in filter(f,1):
TypeError: 'int' object is not iterable
>>> for f in filter(f,b):
...     f
... 
...     
3
4
