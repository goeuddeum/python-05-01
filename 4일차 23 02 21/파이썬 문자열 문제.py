Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
letters = 'python'
print(lang[0],lang[2])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(lang[0],lang[2])
NameError: name 'lang' is not defined. Did you mean: 'range'?
print(lang[0], lang[2])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(lang[0], lang[2])
NameError: name 'lang' is not defined. Did you mean: 'range'?
lang='python' print(lang[0], lang[2])
SyntaxError: invalid syntax
print(letters[0])
p
print(letters[0],letters[2])
p t
license_plate = "24가 2210"
print(license_plate[-4:])
2210

strin="홀짝홀짝홀짝"
string="홀짝홀짝홀짝"
print(string[::-2])
짝짝짝
print(string[::2])
홀홀홀
string = "해랑사를너"
print(string[::-1])
너를사랑해

phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)
010 1111 2222
phone_number1.del(" ")
SyntaxError: invalid syntax
phone_number1.replace(" ")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    phone_number1.replace(" ")
TypeError: replace expected at least 2 arguments, got 1
phone_number1 = phone_number.replace("-"," ")
print(phone_number)
010-1111-2222
phone_number ="010-1111-2222"
phone_number1 = phone_number.replace('-','')
print(phone_number1)
01011112222

url="http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])
kr
print(url_split[0])
http://sharebook

lang = 'python'
lang[0] = 'p'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    lang[0] = 'p'
TypeError: 'str' object does not support item assignment
print(lang)
python

string='abcdfe2a354a32a'
string=string.replace('a','A')
print(string)
Abcdfe2A354A32A

string ='abcd'
string.replace('b','B')
'aBcd'
print(string)
abcd

a="3"
b='4
SyntaxError: incomplete input
b="4+
SyntaxError: incomplete input
b+"4"
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    b+"4"
NameError: name 'b' is not defined
b="4"
print(a+b)
34
print("Hi"*3)
HiHiHi
print("-"800)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("-"*800)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
t1='python'
t2='java'
print([t1+t2]*4)
['pythonjava', 'pythonjava', 'pythonjava', 'pythonjava']
t3=t1+''+t2+''
print(t3*4)
pythonjavapythonjavapythonjavapythonjava
name1 = "김민수"
age1 = 10
name2 ="이철희"
age2 = 13

% formmating
SyntaxError: invalid syntax

>>> print("이름 %s 나이 :%d" % (name1,age1))
이름 김민수 나이 :10
>>> print("이름 %s 나이 :%d" % (name2,age2))
이름 이철희 나이 :13
>>> 
>>> print("이름: {} 나이: {}".format(name1,age1))
이름: 김민수 나이: 10
>>> print("이름: {} 나이: {}".format(name2,age2))
이름: 이철희 나이: 13
>>> 
>>> print(f"이름: {name1} 나이: {age1}".)
SyntaxError: incomplete input
>>> print(f"이름: {name1} 나이: {age1}")
이름: 김민수 나이: 10
>>> print(f"이름: {name2} 나이: {age2}")
이름: 이철희 나이: 13
>>> 
>>> 상장주식수 ="5,969,782,550"
>>> 
>>> 컴마제거=상장주식수.replace(",","")
>>> 타입변환 = int(컴마제거)
>>> print(타입변환,type(타입변환))
5969782550 <class 'int'>
>>> 
>>> 분기="2020/04(E) (IFRS연결)"
>>> 분기[:6]
'2020/0'
>>> 분기[:7]
'2020/04'
>>> 
>>> data = " 삼성전자 "
>>> data= data.strip()
>>> print(datal)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    print(datal)
NameError: name 'datal' is not defined. Did you mean: 'data'?
>>> print(data)
삼성전자
