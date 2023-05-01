Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def t_func():
...     return 1,2,3
... 
>>> a=t_func()
>>> a
(1, 2, 3)
>>> a,b,c=t_func()
>>> a
1
>>> b
2
>>> c
3
>>> a,b*=t_func()
SyntaxError: 'tuple' is an illegal expression for augmented assignment
>>> b
2
>>> a,*b=t_func()
>>> b
[2, 3]
