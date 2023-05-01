Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
shopping={}
shopping['apple']=2
shopping['pear']=2
shopping['hanrabong']=5
shopping['pine apple']=2
shopping
{'apple': 2, 'pear': 2, 'hanrabong': 5, 'pine apple': 2}
shopping['apple']
2
shopping['hanrabong']
5
shopping['banana']
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    shopping['banana']
KeyError: 'banana'
shopping.keys()
dict_keys(['apple', 'pear', 'hanrabong', 'pine apple'])
shopping.values()
dict_values([2, 2, 5, 2])
shopping.items()
dict_items([('apple', 2), ('pear', 2), ('hanrabong', 5), ('pine apple', 2)])
list(shopping.keys())
['apple', 'pear', 'hanrabong', 'pine apple']
list(shopping.values())
[2, 2, 5, 2]
list(shopping,items())
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(shopping,items())
NameError: name 'items' is not defined. Did you mean: 'iter'?
list(shopping.items())
[('apple', 2), ('pear', 2), ('hanrabong', 5), ('pine apple', 2)]
[*shopping.keys()]
['apple', 'pear', 'hanrabong', 'pine apple']
[*shopping.values()]
[2, 2, 5, 2]
[*shopping.items()]
[('apple', 2), ('pear', 2), ('hanrabong', 5), ('pine apple', 2)]
for key in shopping.keys():
    key

    
'apple'
'pear'
'hanrabong'
'pine apple'
for value in shopping.values():
    value

    
2
2
5
2
for item in shopping.items():
    item

    
('apple', 2)
('pear', 2)
('hanrabong', 5)
('pine apple', 2)
shopping={'apple':3, 'pear':2 'hanrabong':5, 'pine apple':2}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
shopping={'apple':3, 'pear':2, 'hanrabong':5, 'pine apple':2}
basket=[]
for fruit, how_many in shopping.items():
    fruit,how_many
    plastic_bag[]
    
SyntaxError: incomplete input
for fruit, how_many in shopping.items():
    fruit,how_many
    plastic_bag=[]
    for _ in range(how_many):
        plastic_bag.append(fruit)
        basket.append(plastic_bag)

        
('apple', 3)
('pear', 2)
('hanrabong', 5)
('pine apple', 2)
basket
[['apple', 'apple', 'apple'], ['apple', 'apple', 'apple'], ['apple', 'apple', 'apple'], ['pear', 'pear'], ['pear', 'pear'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['pine apple', 'pine apple'], ['pine apple', 'pine apple']]
>>> shopping={'apples':3,'pear':2,'hanrabong':5,'pine apple':2}
>>> basket[]
SyntaxError: incomplete input
>>> basket=[]
>>> for fruit, how_many in shopping.items():
...     fruit, how_many
...     basket.append([fruit]*how_many)
... 
...     
('apples', 3)
('pear', 2)
('hanrabong', 5)
('pine apple', 2)
>>> basket
[['apples', 'apples', 'apples'], ['pear', 'pear'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['pine apple', 'pine apple']]
>>> shopping={'apples':3,'pear':2,'hanrabong':5,'pine apple':2}
>>> basket=[[fruit]*how_many for fruit,how_many in shopping.items()]
>>> basket
[['apples', 'apples', 'apples'], ['pear', 'pear'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['pine apple', 'pine apple']]
>>> shopping={'apples':3,'pear':2,'hanrabong':5,'pine apple':2}
>>> basket=[]
>>> while shopping:
...     fruit,how_many = shopping.popitem()
...     fruit,how_many
...     basket.append([fruit]*how_many)
... 
...     
('pine apple', 2)
('hanrabong', 5)
('pear', 2)
('apples', 3)
>>> shopping
{}
>>> basket
[['pine apple', 'pine apple'], ['hanrabong', 'hanrabong', 'hanrabong', 'hanrabong', 'hanrabong'], ['pear', 'pear'], ['apples', 'apples', 'apples']]
