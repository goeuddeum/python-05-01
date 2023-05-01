Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s1 = set([1,2,3])

s1
{1, 2, 3}
s2=set("HELLO")
S2
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    S2
NameError: name 'S2' is not defined. Did you mean: 's2'?
S2
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    S2
NameError: name 'S2' is not defined. Did you mean: 's2'?
s2
{'O', 'H', 'E', 'L'}
{*[1,2,3]}
{1, 2, 3}
[*[1,2,3]]
[1, 2, 3]
(*[1,2,3],)
(1, 2, 3)
*[1,2,3],
(1, 2, 3)
1
1
(1)
1
s1=set([1,2,3])
l1=list(s1)
l1
[1, 2, 3]
l1[0]
1
t1=tuple(s1)
t1
(1, 2, 3)
t1[0]
1
s1&s2
set()
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
s17s2([4,5,6])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s17s2([4,5,6])
NameError: name 's17s2' is not defined
s1&s2([4,5,6])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s1&s2([4,5,6])
TypeError: 'set' object is not callable
>>> s1&s2
{4, 5, 6}
>>> s1&s2
{4, 5, 6}
>>> s1.intersection(s2)
{4, 5, 6}
>>> s1:s2
>>> 
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> s1-s2
{1, 2, 3}
>>> s2-s1
{8, 9, 7}
>>> s1.difference(s2)
{1, 2, 3}
>>> s2.difference
<built-in method difference of set object at 0x0000021207C742E0>
>>> s2.differences1)
SyntaxError: unmatched ')'
>>> s2.difference(s1)
{8, 9, 7}
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> {*[1,2,3],*[4,5,6]}
{1, 2, 3, 4, 5, 6}
>>> (*[1,2,3],*[4,5,6])
(1, 2, 3, 4, 5, 6)
>>> 
>>> (*[1,2,3],)
(1, 2, 3)
>>> s1=set([1,2,3])
>>> s1.add(4)
>>> s1
{1, 2, 3, 4}
>>> s1=set([1,2,3])
>>> s1.update([4,5,6])
>>> s1
{1, 2, 3, 4, 5, 6}
>>> s1=set([1,2,3])
>>> s1.remove(2)
>>> s1
{1, 3}
