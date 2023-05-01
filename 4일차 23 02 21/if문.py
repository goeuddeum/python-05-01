Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
money =True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

    
택시를 타고 가라

pocket =['paper','money','cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

    

money = 2000
if money>=3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

    
걸어 가라
>>> 
>>> money = 2000
>>> card=True
>>> if money >= 3000 or card:
...     print("택시를 타고 가라"
... else:
...     
SyntaxError: '(' was never closed
>>> if money >= 3000 or card:
...     print("택시를 타고 가라")
... else:
...     print("걸어 가라")
... 
...     
택시를 타고 가라
>>> pocket = ['paper', 'cellphone']
>>> card = True
>>> if 'money' in pocket:
...     print("택시를 타고 가라")
... else:
...     if card:
...         print("택시를 타고 가라")
...     else:
...         print("걸어 가라")
... 
...         
택시를 타고 가라
>>> pocket =['paper', 'cellphone']
>>> card = True

>>> if 'money' in pocket:
...     print("택시를 타고 가라")
... elif card:
...     print("택시를 타고 가라")
... else:
...     print("걸어 가라")
... 
...     
택시를 타고 가라
