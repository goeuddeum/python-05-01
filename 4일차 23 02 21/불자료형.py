Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=True
b=False
type(a)
<class 'bool'>
type(b)
<class 'bool'>
1 ==1
True
2>1
True
1<2
True
2<1
False
a  =[1,2,3,4]
while a:
    a.pop()

    
4
3
2
1
>>> if []:
...     print("참")
... else:
...     print("거짓")
... 
...     
거짓
>>> if [1,2,3]:
...     print("참")
... else:
...     print("거짓")
... 
...     
참
>>> bool(None)
False
>>> bool(0)
False
>>> bool({})
False
>>> bool(())
False
>>> bool([])
False
>>> bool("")
False
>>> bool('
...      
SyntaxError: incomplete input
>>> bool('')
...      
False
>>> bool('python')
...      
True
