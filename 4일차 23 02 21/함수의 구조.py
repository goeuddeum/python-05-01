Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def add(a,b):
    return a+b

def add(a,b)
SyntaxError: incomplete input
reuturn a+b
SyntaxError: invalid syntax
a=3
b=4
c=add(a,b)
print(c)
7

def add(a,b):
    returtn a+ b
    
SyntaxError: invalid syntax
def add(a,b):
    returtn a + b
    
SyntaxError: invalid syntax
print(add(3,4))
7
def say():
    input('say something: ')
    return word

say()
say something: hi!
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    say()
  File "<pyshell#18>", line 3, in say
    return word
NameError: name 'word' is not defined. Did you mean: 'ord'?
def say():
    input('say something: ')
    return word

say()
say something: hi
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    say()
  File "<pyshell#21>", line 3, in say
    return word
NameError: name 'word' is not defined. Did you mean: 'ord'?
def get_order():
    order=input('what do tou want? coffee or tea?')
    return order

get_order()
what do tou want? coffee or tea? coffee
' coffee'
def add(a,b):
    print("%d, %d의 합은 %d입니다." (a,b, a+b))

    

add(3<4)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    add(3<4)
TypeError: add() missing 1 required positional argument: 'b'
>>> def add(a,b):
...     print("%d, %d의 합은 %d입니다." (a,b, a+b))
... 
...     
>>> add(3,4)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    add(3,4)
  File "<pyshell#34>", line 2, in add
    print("%d, %d의 합은 %d입니다." (a,b, a+b))
TypeError: 'str' object is not callable
>>> def add(a,b):
...     print("%d, %d의 합은 %d입니다." (a, b, a+b))
... 
...     
>>> add(3,4)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    add(3,4)
  File "<pyshell#37>", line 2, in add
    print("%d, %d의 합은 %d입니다." (a, b, a+b))
TypeError: 'str' object is not callable
>>> def add(a,b):
...     print("%d, %d의 합은 %d입니다." % (a, b, a+b))
... 
...     
>>> add(3,4)
3, 4의 합은 7입니다.
>>> a= add(3,4)
3, 4의 합은 7입니다.
>>> def add(a,b):
...     return a+b
... 
>>> result = add(a=3,b=7)
>>> print(result)
10
>>> result=add(b=5,a=3)
>>> print(result)
8
