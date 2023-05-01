Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> menu{
...     
SyntaxError: incomplete input
>>> menu={
...     'americano' : 1500,
...     'caffe latte':2500,
...     'expresso':1500
... }
>>> total_money=0
>>> def coffee_machine(money, coffee_in):
...     change, coffee_out = money,None
...     if coffee_in in menu.keys():
...         value = menu[coffee_in]
...         if money>=value:
...             change = money - value
...             coffee_out = coffee_in
...     return change, coffee_out
... 
>>> change,coffee = coffee_machine(5000,'americano')
>>> print(change,coffee)
3500 americano
