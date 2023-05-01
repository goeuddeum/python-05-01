>>> class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.bank="SC은행"
        num1 = random.randint(0,999)
        num2=random.randint(0,99)
        num3=random.randint(0,999999)
        num1=str(num1).zfill(3) # 1 > '1' > '001'
        num2=str(num2).zfill(2) # 1 > '1' > '01'
        num3=str(num3).zfill(6) # 1 > '1' > '000001'
        self.account_number = num1+'-'+num2+'-'+num3 #001-01-000001
        
>>> kim=Account("김민수",100)
>>> print(kim.name)
김민수
>>> print(kim.balance)
100
>>> print(kim.bank)
SC은행
>>> print(kim.account_number)
768-69-065347

>>> import random
>>> import string
>>> string.digits
'0123456789'
>>> random.choices(string.digits,k=3)
['0', '5', '6']
>>> random.choices(string.digits,k=2)
['7', '9']
>>> random.choices(string.digits,k=6)
['0', '3', '9', '1', '3', '7']
>>> first=''.join(random.choices(string.digits,k=3))
>>> mid=''.join(random.choices(string.digits,k=2))
>>> last=''.join(random.choices(string.digits,k=6))
>>> acc_num=first+'-'+mid+'-'+last
>>> acc_num
'839-36-915958'
>>> '%d'%2276
'2276'
>>> '%6d'%2276
'  2276'
>>> '%06d'%2276
'002276'
>>> first=random.randint(0,1000)
>>> mid=random.randint(0,100)
>>> last=random.randint(0,1000000)
>>> acc_num='%03d-%02d-%06d'%(first,mid,last)
>>> acc_num
'911-26-383026'
>>> acc_num='{:03}-{:02}-{:06}'.format(first,mid,last)
>>> acc_num
'911-26-383026'
>>> acc_num=f'{first:03}-{mid:02}-{last:06}'
>>> acc_num
'911-26-383026'