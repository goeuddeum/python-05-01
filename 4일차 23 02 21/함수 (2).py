Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

        
say_myself("박응용", 27)
나의 이름은 박응용입니다.
나이는 27살입니다.
남자입니다.
say_myself("박응용", 27, True)
나의 이름은 박응용입니다.
나이는 27살입니다.
남자입니다.
>>> say_myself("박응선", 27, False)
나의 이름은 박응선입니다.
나이는 27살입니다.
여자입니다.
>>> say_myself("고으뜸", 26, True)
나의 이름은 고으뜸입니다.
나이는 26살입니다.
남자입니다.
>>> def say_myself(name, man=True, old):
...     print("나의 이름은 %s입니다." % name)
...     print("나이는 %d살입니다." % old)
...     if man:
...         print("남자입니다.")
...     else:
...         print("여자입니다.")
...         
SyntaxError: non-default argument follows default argument
>>> def func(a,b):
...         reutrn
... 
...         
>>> a
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> f=lambda a,b:a+b
>>> f(3,4)
7
>>> a=4
>>> b = 3 if a>3 else 4
>>> if a>3:
...     b=3
... else:
...     b=4
... 
...     
>>> (a>3)?3:4
SyntaxError: invalid syntax
