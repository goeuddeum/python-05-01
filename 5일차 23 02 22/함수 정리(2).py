Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def h (x,y):
    return x + y
x=2
SyntaxError: invalid syntax
def h (x,y):
...     return x + y
... 
>>> x=2
>>> y=2
>>> z= h(x,y)
>>> z
4
>>> def k (a,b):
...     q=a//b
...     r=a%b
...     return q,r
... 
>>> a=19
>>> b=5
>>> q,r=k(a,b)
>>> q
3
>>> r
4
>>> k
<function k at 0x000001EEA7C3C9A0>
>>> type(k)
<class 'function'>
>>> 
>>> def func(a,b)
SyntaxError: incomplete input
>>> def func(a,b):
...     a,b
... 
...     
>>> func(10,20)
>>> func('hello','world')
>>> def func(a,b):
...     a,b
... 
...     
>>> func(10,20)
>>> 
>>> func(b=100,a=3000)
