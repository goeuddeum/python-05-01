Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=(1,2,3,4)
>>> d-{'a':1, 'b':2,'c':3,'d':4}
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    d-{'a':1, 'b':2,'c':3,'d':4}
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> d={'a':1, 'b':2,'c':3,'d':4}
>>> t
(1, 2, 3, 4)
>>> d
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> s
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s={1,2,2,3,3,3,4,4,4,4,}
>>> s
{1, 2, 3, 4}
>>> type(t)
<class 'tuple'>
>>> type(d)
<class 'dict'>
>>> type(s)
<class 'set'>
>>> for i in t:
...     i
... 
...     
1
2
3
4
>>> for i in d:
...     i
... 
...     
'a'
'b'
'c'
'd'
for i in s:
    i

    
1
2
3
4
t=(i for i in range(10))
d={('key'+str(i)):i for i in range(10)}
d
{'key0': 0, 'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5, 'key6': 6, 'key7': 7, 'key8': 8, 'key9': 9}
t=(i for i in tange(10))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    t=(i for i in tange(10))
NameError: name 'tange' is not defined. Did you mean: 'range'?
t=(i for i in range(10))
d ={('key'+str(o)):i for i in range(10)}
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d ={('key'+str(o)):i for i in range(10)}
  File "<pyshell#25>", line 1, in <dictcomp>
    d ={('key'+str(o)):i for i in range(10)}
NameError: name 'o' is not defined
d ={('key'+str(i)):i for i in range(10)}
s ={i for i in range(10)}
t
<generator object <genexpr> at 0x0000020504257920>
s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
d
{'key0': 0, 'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5, 'key6': 6, 'key7': 7, 'key8': 8, 'key9': 9}
type(t)
<class 'generator'>
type(d)
<class 'dict'>
type(s)
<class 'set'>

for i in t:
    i

    
0
1
2
3
4
5
6
7
8
9
for i in d:
    i

    
'key0'
'key1'
'key2'
'key3'
'key4'
'key5'
'key6'
'key7'
'key8'
'key9'
for i in t:
    i

    
for i in d:
    i

    
'key0'
'key1'
'key2'
'key3'
'key4'
'key5'
'key6'
'key7'
'key8'
'key9'
a=(1,2,3,4)
a
(1, 2, 3, 4)
type(1)
<class 'int'>
type(a)
<class 'tuple'>
b=(1)
type(b)
<class 'int'>
c-(1,)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    c-(1,)
NameError: name 'c' is not defined
c-=(1,)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    c-=(1,)
NameError: name 'c' is not defined
c =( 1,)
type(c)
<class 'tuple'>
d,e=5,6
5
5
6
6
d,e=(5,6)
d
5
e
6
(d,e)=5,6
d
5
e
6
(d,e)=(5,6)
d
5
e
6
d,e=5,6,7
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d,e=5,6,7
ValueError: too many values to unpack (expected 2)
d, e =5,6,7
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d, e =5,6,7
ValueError: too many values to unpack (expected 2)
d,*r=5,67
r,,,,,,,,,,,,,,,,,,,,
SyntaxError: invalid syntax





























4
d,*e=5,6,7
e
[6, 7]
d,*e,f= 5,6
e
[]
d,*,f==5
SyntaxError: invalid syntax
d,*e,f=5
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    d,*e,f=5
TypeError: cannot unpack non-iterable int object

*e,f=5,6
e
[5]
*e=5,
SyntaxError: starred assignment target must be in a list or tuple
*e=5
SyntaxError: starred assignment target must be in a list or tuple

def t_fune()
SyntaxError: incomplete input
def t_func():
    reutrn 1,2,3
    
SyntaxError: invalid syntax
def t_func():
    reutrn 1, 2, 3
    
SyntaxError: invalid syntax
def t_func():
    return 1, 2, 3
a=f_func()
SyntaxError: invalid syntax
def t_func():
    return 1, 2, 3

a+f_func()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a+f_func()
NameError: name 'f_func' is not defined. Did you mean: 't_func'?
a=f_func()
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a=f_func()
NameError: name 'f_func' is not defined. Did you mean: 't_func'?
a=t_func()
a
(1, 2, 3)
a,b,c=t_func()
a
1
b
2
c
3
a,*b=t_func()
b
[2, 3]
a,b,*c=1,2,3,4,5,6
c
[3, 4, 5, 6]
def f(a,b,*c):
    a
    b
    c

    
f(1,2,3,4,5,6)

def f(a,b,*c):
    a
    b
    c

    
f(1,2,3,4,5,6)


a
1
f(a)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    f(a)
TypeError: f() missing 1 required positional argument: 'b'
f(a,)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    f(a,)
TypeError: f() missing 1 required positional argument: 'b'
f(1,2,3,4,5,6) # a,b,*c=1,2,3,4,5,6
def g(*args):
    args

    
g(1,2,3,4,5,6,7)
g(1)
g(1,2)
