>>> def print_max(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
        
>>> 
>>> print_max(1,500,2503910234)
2503910234
>>> print_max(10,10,10)
10
>>> print_max(10,10,9)
9
>>> def print_max(a,b,c):
    if a>=b and a>=c:
        print(a)
    elif a>=b and a<c:
        print(c)
    elif a<b and b>=c:
        print(b)
        
>>> def print_max(a,b,c):
    _max=a
    if b>_max:
        _max=b
    if c>_max:
        _max=c
    print(_max)
    
>>> print_max(10,10,1)
10
>>> print_max(10,12,1)
12
>>> print_max(10,10,10)
10
>>> def print_max(a,b,c):
    _max=a
    L=[b,c]
    for i in L:
        if i>_max:
            _max=i
    print(_max)
    
>>> print_max(10,10,10)
10
>>> print_max(10,10,1)
10
>>> print_max(1,10,10)
10
>>> print_max(1,2,10)
10
>>> import numpy as np
>>> 
>>> L=np.random.randint(1,100,50)
>>> max(L)
99
>>> def print_max(L):
    _max=L[0]
    for i in L[1:]:
        if i>_max:
            
            _max:i
    print(_max)

>>> def print_keys(D):
    for key in D:
        print(key)
        
>>> def print_value_by_key(D,key):
    print(D[key])
    
>>> my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
>>> print_value_by_key  (my_dict, "10/26")
[100, 130, 100, 100]

def print_value_by_key(D,key):
    try:
        print((D[key]))
    except:
        print('키가 없어요')
        
>>> print_value_by_key(my_dict, "10/28")
키가 없어요

>>> def print_5xn(string):
    _cnt=0
    for s in string:
        print(s,end='')
        _cnt+=1
        if _cnt%5==0:
            print()
            
>>> print_5xn("아이엠어보이유알어걸")
아이엠어보
이유알어걸
>>> def print_5xn(string):
    for _cnt,s in enumerate(string):
        print(s,end='')
        if _cnt%5==4:
            print()
>>> def print_mxn(line, num):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1) :
        print(line[x * 5: x * 5 + 5])
        
>>> print_5xn("아이엠어보이유알어걸")
아이엠어보
이유알어걸
>>> print_5xn("아이엠어보이유알어걸스")
아이엠어보
이유알어걸
스

>>> def print_mxn(string,m):
    for _cnt,s in enumerate(string):
        print(s,end='')
        if _cnt%m==(m-1):
            print()
            
>>> print_mxn("아이엠어보이유알어걸",3)
아이엠
어보이
유알어
걸

>>> def calc_monthly_salary(annual_salary):
    print(int(annual_salary/12))
    
>>> def calc_monthly_salary(annual_salary):
    print(f'{(annual_salary/12):.0f}')
    
>>> def calc_monthly_salary(annual_salary):
    print('{:.0f}'.format(annual_salary/12))
    
>>> def calc_monthly_salary(annual_salary):
    print('%0f'%(annual_salary/12))
    
>>> calc_monthly_salary(120000000)
10000000.000000

>>> def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

왼쪽: 100
오른쪽: 200

>>> def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

왼쪽: 200
오른쪽: 100
