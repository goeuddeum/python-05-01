>>> def print_coin():
    print("비트코인")

>>> print_coin()
비트코인

>>> for i in range(100):
    print_coin
    
>>> def print_coin():
    for i in range(100):
        print("비트코인")
        
>>> def message():
    print("A")
    print("B")
    
>>> message()
A
B
>>> print("C")
C
>>> message()
A
B

>>> print("A")
A
>>> def message():
    print("B")
    
>>> print("C")
C
>>> message()
B

>>> def message1():
    print("A")
    
>>> def message2():
    print("B")
    message1()
    
>>> message2()
B
A

>>> def message1():
    print("A")
    
>>> def message2():
    print("B")
    
>>> def message3():
    for i in range(3):
        message2()
        
        print("C")
    message1()
    
>>> message3()
B
C
B
C
B
C
A
>>> def 함수(문자열):
    print(문자열)
    
>>> 함수("안녕")
안녕
>>> 함수("Hi")
Hi


>>> def 함수(a,b):
    print(a+b)
    
>>> 함수(3,4)
7
>>> 함수(7,8)
15

>>> f=print(":D")
>>> def print_with_smile (string) :
    print (string +":D")
>>> print_with_smile("안녕하세요")
안녕하세요:D
>>> def print_upper_price(price):
    print(price*1.3)
    
>>> def print_sum(a.b):
    print(a+b)
>>> def print_sum(a,b):
    print( a + b )
>>> def print_arithmetic_operation(a,b):
    print(a,"+",b,"=",a+b)
    print(a,"-",b,"=",a-b)
    print(a,"*",b,"=",a*b)
    print(a,"/",b,"=",a/b)
    
>>> def print_max(a,b,c):
    max_val=0
    if a>max_val:
        max_val=a
    if b>max_val:
        max_val=b
    if c>max_val:
        max_val=c
    print(max_val)
    
>>> max(1,2,3)
3

>>> def print_reverse(string):
    print(string[::-1])
>>> print_reverse("nohtyp")
python

>>> def print_score(score_list):
    print(sum(score_list)/len(score_list))
>>> print_score([1,2,3])
2.0

>>> def print_even(my_list):
    for v in my_list:
        if v % 2 == 0:
            print(v)
            
>>> print_even([1,3,2,10,12,11,15])
2
10
12

>>> def print_keys(dic):
    for keys in dic.keys():
        print(keys)
        
>>> print_keys({"이름":"김말똥","나이":30,"성별":0})
이름
나이
성별
