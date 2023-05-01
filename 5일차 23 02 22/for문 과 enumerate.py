Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i, coffee in enumerate(['americano','caffe latte', 'espresso']):
    i, coffee

    
(0, 'americano')
(1, 'caffe latte')
(2, 'espresso')

a1['americano','caffe lette','es[resso','green tea')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a1=['americano','caffe lette','es[resso','green tea')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a1=['americano','caffe lette','es[resso','green tea']
a2[1500,2500,1600,2200]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a2[1500,2500,1600,2200]
NameError: name 'a2' is not defined. Did you mean: 'a1'?
a2=[1500,2500,1600,2200]
z=zip(a1,a2)
for coffee,price in z:
    coffee,price
... 
...     
('americano', 1500)
('caffe lette', 2500)
('es[resso', 1600)
('green tea', 2200)
>>> for coffee,price in z:
...     coffee,price
... 
...     
>>> a1=['americano','caffe latte','espresso']
>>> a2=[1500,2500,1600]
>>> z=zip(a1,a2)
>>> z*,
SyntaxError: incomplete input
>>> *z,
(('americano', 1500), ('caffe latte', 2500), ('espresso', 1600))
>>> *z,
()
>>> z=zip(a1,a2)
>>> a2=[*z]
>>> a2
[('americano', 1500), ('caffe latte', 2500), ('espresso', 1600)]
>>> 
>>> zip(*a2)
<zip object at 0x000002184AD05940>
>>> a3=zip(*a2)
>>> a4=[*a3]
>>> a4
[('americano', 'caffe latte', 'espresso'), (1500, 2500, 1600)]
>>> LL1,LL2=a4
>>> LL1
('americano', 'caffe latte', 'espresso')
>>> LL2
(1500, 2500, 1600)
>>> list(LL1)
['americano', 'caffe latte', 'espresso']
>>> list(LL2)
[1500, 2500, 1600]
