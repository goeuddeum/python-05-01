Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[1, 2, 3]
a.append[4]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a.append[4]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.append(4)

a=[1, 2, 3]
a.append(4)

a
[1, 2, 3, 4]
a.ppend([5. 6])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a.ppend([5, 6])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.ppend([5, 6])
AttributeError: 'list' object has no attribute 'ppend'. Did you mean: 'append'?
a
[1, 2, 3, 4]
a.append([5, 6])
a
[1, 2, 3, 4, [5, 6]]
a=[1, 4 ,3, 2]
a.sort()
a
[1, 2, 3, 4]
a=[ 'a', 'c', 'b']
a.sort()
a
['a', 'b', 'c']
a=['a', 'c', 'b']
a.reverse()
a
['b', 'c', 'a']
a=[1,2,3]
a.index(3)
2
a.index(0)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.index(0)
ValueError: 0 is not in list
a.index(1)
0
a=['a', 'b', 'c']
ar=a[::=1]
SyntaxError: invalid syntax
ar=a[::-1]
ar
['c', 'b', 'a']
a.sort()
a
['a', 'b', 'c']
a.reverse()
a
['c', 'b', 'a']
import random
random.shuffle(a)
a
['a', 'c', 'b']
a=[1, 2, 3]
a.insert(0, 4)
a
[4, 1, 2, 3]
a=[1, 2, 3, 1, 2, 3]
a.remove(3)
a
[1, 2, 1, 2, 3]
a.remove(3)
a
[1, 2, 1, 2]
a=[1, 2, 3]
a.pop()
3
a
[1, 2]
a=[1, 2, 3]
a.pop(1)
2
>>> a
[1, 3]
>>> a= 1, 2, 3, 1]
SyntaxError: unmatched ']'
>>> a= [1, 2, 3, 1]
>>> a.count(1)
2
>>> a= [1, 2, 3]
>>> a.extend([4, 5])
>>> a
[1, 2, 3, 4, 5]
>>> b=[6, 7]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6, 7]
>>> backpack=['book','note','tavlet','pencil case']
>>> if 'note book' in backpack:
...     where=backpack.index('note book')
...     where
...     notebook = backpack,pop(where)
...     notebook
... 
...     
>>> 1
1
>>> 'notebook'
'notebook'
>>> backpack
['book', 'note', 'tavlet', 'pencil case']
>>> backpack.insert('note book')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    backpack.insert('note book')
TypeError: insert expected 2 arguments, got 1
>>> backpack.extend('note book')
>>> backpack
['book', 'note', 'tavlet', 'pencil case', 'n', 'o', 't', 'e', ' ', 'b', 'o', 'o', 'k']
