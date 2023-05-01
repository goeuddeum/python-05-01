Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dic ={'name':'pey','phone':'0119993323','birth':'1118'}
a={1:'hi'}
a = {'a':[1,2,3]}
a={1:'a'}
a[2]=b
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[2]=b
NameError: name 'b' is not defined
a[2]= 'b'
a
{1: 'a', 2: 'b'}
a['name']='pey
SyntaxError: incomplete input
a['name']='pey'
a
{1: 'a', 2: 'b', 'name': 'pey'}
a[3]=[1,2,3]
a
{1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

del a[1]
a
{2: 'b', 'name': 'pey', 3: [1, 2, 3]}
grade ={'pey':10, 'julliet':99}
grade['pey']
10
grade['julliet']
99
a = {'name': 'pey','phone':'0119993323','birth':'1118'}
a.keys()
dict_keys(['name', 'phone', 'birth'])
for k in a,keys():
    print(k)

    
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for k in a,keys():
NameError: name 'keys' is not defined
name
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    name
NameError: name 'name' is not defined
for k in a.keys():
    print(k)
    name
    phone
    birth

    
name
Traceback (most recent call last):
  File "<pyshell#28>", line 3, in <module>
    name
NameError: name 'name' is not defined
list(a.keys())
['name', 'phone', 'birth']
a.values()
dict_values(['pey', '0119993323', '1118'])
a.items()
dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
a.clear()
a
{}
a={'name':'pey','phone':'0119993323','birth':'1118'}
a.get('name')
'pey'
a.get('phone')
'0119993323'
fridge={'apple':2,'banana':5,'orange':10}
for fruit,howmany in fridge.items():
    fruit,howmany

    
('apple', 2)
('banana', 5)
('orange', 10)
for item in fridge.items():
    item

    
('apple', 2)
('banana', 5)
('orange', 10)
for item in fridge.keys():
    item

    
'apple'
'banana'
'orange'
for item in fridge.values():
    item

    
2
5
10
for item in fridge:
...     item
... 
...     
'apple'
'banana'
'orange'
>>> [*fridge]
['apple', 'banana', 'orange']
>>> fridge.keys()
dict_keys(['apple', 'banana', 'orange'])
>>> type(fridge.keys())
<class 'dict_keys'>
>>> [*fridge.keys()]
['apple', 'banana', 'orange']
>>> fridge.values()
dict_values([2, 5, 10])
>>> type(fridge.values())
<class 'dict_values'>
>>> [*frudge.values()]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    [*frudge.values()]
NameError: name 'frudge' is not defined. Did you mean: 'fridge'?
>>> [*fridge.values()]
[2, 5, 10]
>>> type(fridge.items())
<class 'dict_items'>
>>> [*frudge.iteums()]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    [*frudge.iteums()]
NameError: name 'frudge' is not defined. Did you mean: 'fridge'?
>>> [*frudge.items()]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    [*frudge.items()]
NameError: name 'frudge' is not defined. Did you mean: 'fridge'?
>>> [*fridge.items()]
[('apple', 2), ('banana', 5), ('orange', 10)]
