Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ㅁ=1
a=1
b='pythone'
c=[1,2,3]
a=[1,2,3]
id(a)
2027744646144
b=a
id(b)
2027744646144
c=[1,2,3]
id(c)
2027744814080
>>> a=3
>>> b
[1, 2, 3]
>>> b=3
>>> id(3)
140734623052648
>>> id(a)
140734623052648
>>> id(b)
140734623052648
>>> a,b=('python','Life')
>>> (a,b)='python','Life'
>>> [a,b]=['pthone''Life']
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    [a,b]=['pthone''Life']
ValueError: not enough values to unpack (expected 2, got 1)
>>> [a,b] = ['pthone''Life']
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    [a,b] = ['pthone''Life']
ValueError: not enough values to unpack (expected 2, got 1)
>>> a=3
>>> b=5
>>> a,b=b,a
>>> a
5
>>> b
3
>>> [a,b]=['python', 'Life']
>>> a=b='python;
SyntaxError: incomplete input
>>> a=b='python'
>>> a=[1,2,3]
>>> b=[1,2,3]
>>> a is b
False
>>> b is a
False
