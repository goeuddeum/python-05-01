Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a,b,*c=(0,1,2,3,4,5)
a
0
b
1
c
[2, 3, 4, 5]
scores=[8.8,8.9,8.7,9.2,9.7,9.9,7.8,9.4]
*valid_score,_,_=scores
print(vaild_score)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(vaild_score)
NameError: name 'vaild_score' is not defined. Did you mean: 'valid_score'?
print(valid_score)
[8.8, 8.9, 8.7, 9.2, 9.7, 9.9]
아이스크림={'메로나':'1000','폴라포':'1200','빵빠레':'1800'}
빵빠레
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    빵빠레
NameError: name '빵빠레' is not defined
print(아이스크림)
{'메로나': '1000', '폴라포': '1200', '빵빠레': '1800'}

scores=[8.8,8.9,8.7,9.2,9.7,9.9,7.8,9.4]
a,b,*valid_score=scores
print(valid_score)
[8.7, 9.2, 9.7, 9.9, 7.8, 9.4]
scores=[8.8,8.9,8.7,9.2,9.7,9.9,7.8,9.4]
a,*valid_score,b=scores
print(valid_score)
[8.9, 8.7, 9.2, 9.7, 9.9, 7.8]

ice={'메로나':'1000','폴라포':'1200','빵빠레':'1800'}
ice[죠스바]='1200'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    ice[죠스바]='1200'
NameError: name '죠스바' is not defined
ice['죠스바']='1200'
ice['월드콘']='1500'
print(ice)
{'메로나': '1000', '폴라포': '1200', '빵빠레': '1800', '죠스바': '1200', '월드콘': '1500'}


ice={'메로나':'1000','폴라포':'1200','빵빠레':'1800','죠스바':'1200','월드콘':'1500'}
print(ice[메로나])
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(ice[메로나])
NameError: name '메로나' is not defined
print(ice["메로나"])
1000
print("메로나가격",ice["메로나"])
메로나가격 1000

iice={'메로나':'1000','폴라포':'1200','빵빠레':'1800','죠스바':'1200','월드콘':'1500'}
ice={'메로나':'1000','폴라포':'1200','빵빠레':'1800','죠스바':'1200','월드콘':'1500'}
ice["메로나"]=1300
print(ice["메로나"])
1300

del ice[1]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    del ice[1]
KeyError: 1
del ice["메로나"]
print(ice)
{'폴라포': '1200', '빵빠레': '1800', '죠스바': '1200', '월드콘': '1500'}

inventory={'메로나':'300','20','비비빅':'400','3','죠스바':'250','100'}
SyntaxError: ':' expected after dictionary key
inventory={'메로나':'300,20','비비빅':'400,3','죠스바':'250,100'}
print(inventory)
{'메로나': '300,20', '비비빅': '400,3', '죠스바': '250,100'}

print(inventory["메로나"],"원")
300,20 원
print(inventory["메로나"][0],"원")
3 원
inventory={"메로나":[300,20],"비비빅":[400,3],"죠스바":[250,100]}
print(inventory["메로나"][0],"원")
300 원
print(inventory)
{'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100]}
print([0]inventory["메로나"],"개")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(inventory["메로나"][1],"개")
20 개

inventory[월드콘]=[500,7]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    inventory[월드콘]=[500,7]
NameError: name '월드콘' is not defined
inventory[월드콘]='500,7'
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    inventory[월드콘]='500,7'
NameError: name '월드콘' is not defined
inventory["월드콘"]=[500,7]
print(inventory)
{'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream.keys()
dict_keys(['탱크보이', '폴라포', '빵빠레', '월드콘', '메로나'])

icecream.values()
dict_values([1200, 1200, 1800, 1500, 1000])

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>>> new_product = {'팥빙수':2700, '아맛나':1000}
>>> icecream.updata(new_product)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    icecream.updata(new_product)
AttributeError: 'dict' object has no attribute 'updata'. Did you mean: 'update'?
>>> icecream.update(new_product)
>>> print(icecream)
{'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000, '팥빙수': 2700, '아맛나': 1000}
>>> 
>>> keys = ("apple", "pear", "peach")
>>> vals = (300, 250, 400)
>>> a1=keys
>>> a2=vals
>>> result=zip(a1,a2)
>>> for fruit, price in result:
...     fruit, price
... 
...     
('apple', 300)
('pear', 250)
('peach', 400)
>>> keys = ("apple", "pear", "peach")
>>> vals = (300, 250, 400)
>>> result=dict(zip(keys,vals))
>>> print(result)
{'apple': 300, 'pear': 250, 'peach': 400}
>>> 
>>> date = ['09/05', '09/06', '09/07', '09/08', '09/09']
>>> close_price = [10500, 10300, 10100, 10800, 11000]
>>> close_price=dict(zip(date,close_price))
>>> print(close_table)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print(close_table)
NameError: name 'close_table' is not defined. Did you mean: 'close_price'?
>>> print(close_price)
{'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}
