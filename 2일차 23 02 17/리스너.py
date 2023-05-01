Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tutle import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from tutle import *
ModuleNotFoundError: No module named 'tutle'
>>> from turtle import *
>>> 
>>> def animate():
...     print('a')
...     ontimer(animate, 1000)
... 
...     
>>> def flick():
...     print('f')
... 
...     
>>> onkey(flick,'space') # key listener
>>> listen()
>>> animate()
a
>>> a
a
a
a
a
a
a
a
a
a

>>> a
a
a
a
a
a
a
a
a
a
a
exitonclick # GUI loop here
<function exitonclick at 0x000001E31E10B560>
a
a
a
a
a
a
a
a
a
a
a
a
a
a
a
clear()
a
a
a
a
bye()
