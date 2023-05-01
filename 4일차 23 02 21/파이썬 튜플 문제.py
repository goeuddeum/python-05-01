Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
my_variable
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    my_variable
NameError: name 'my_variable' is not defined
(my_variavle)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    (my_variavle)
NameError: name 'my_variavle' is not defined
my_variable=()
print(my_variable)
()
print(type(my_variable))
<class 'tuple'>

movie_rank=("닥터스트레인지","스플릿","럭키")
print(type(movie_rank))
<class 'tuple'>

a=(1,)
print(type(a))
<class 'tuple'>

t = (1,2,3)
t=1,2,3,4
type(t)
<class 'tuple'>

t=('a','b','c')
a=A
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a=A
NameError: name 'A' is not defined. Did you mean: 'a'?
t[0]="A"
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t[0]="A"
TypeError: 'tuple' object does not support item assignment
t=('a','b','c')
t[0]='A'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t[0]='A'
TypeError: 'tuple' object does not support item assignment
t=('A,'B','C')
   
SyntaxError: unterminated string literal (detected at line 1)
t=('A','B','C')
   
t
   
('A', 'B', 'C')
interest=('삼성전자','LG전자','SK Hynix')
   
>>> data=tiple(interest)
...    
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    data=tiple(interest)
NameError: name 'tiple' is not defined. Did you mean: 'tuple'?
>>> data=tuple(interest)
...    
>>> print(data)
...    
('삼성전자', 'LG전자', 'SK Hynix')
>>> 
>>> temp = ('apple', 'banana', 'cake')
...    
>>> a,b,c = temp
...    
>>> print(a,b,c)
...    
apple banana cake
>>> 
>>> a=(2,n+2)
...    
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a=(2,n+2)
NameError: name 'n' is not defined
>>> a=(n+2)
...    
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a=(n+2)
NameError: name 'n' is not defined
>>> data=tuple(range(2,100,2))
...    
>>> print(data)
...    
(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98)
