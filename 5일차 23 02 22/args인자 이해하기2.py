def func(*args):
    args
    
func(1,2,3,4)
a=[5,6,7,8]
func(*a)
>>> def f(*args):
    args
    
>>> f(1)
(1,)
>>> f(1,2)
(1, 2)
>>> f(1,2,3)
(1, 2, 3)
>>> L=[1,2,3,4]
>>> f(*L)
(1, 2, 3, 4)
>>> def g(**kwargs):
    kwargs
    
>>> g(a=1)
{'a': 1}
>>> g(a=1,b=2)
{'a': 1, 'b': 2}
>>> D={'a':1,'b':2,'c':3}
>>> g(**D)
{'a': 1, 'b': 2, 'c': 3}
>>> D2={'1':2,'2'=3}
  File "<stdin>", line 1
    D2={'1':2,'2'=3}
                ^
SyntaxError: ':' expected after dictionary key
>>> D2={'1':2,'2':3}
>>> g(**D2)
{'1': 2, '2': 3}