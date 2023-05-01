Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end="")
    print('')

    
24681012141618
369121518212427
4812162024283236
51015202530354045
61218243036424854
71421283542495663
81624324048566472
91827364554637281
[i for i in range(2,10]
 
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
[i for i in range(2,10)]
 
[2, 3, 4, 5, 6, 7, 8, 9]
[i*j for i in range(1,10) for i in range(2,10)]
 
[18, 27, 36, 45, 54, 63, 72, 81, 18, 27, 36, 45, 54, 63, 72, 81, 18, 27, 36, 45, 54, 63, 72, 81, 18, 27, 36, 45, 54, 63, 72, 81, 18, 27, 36, 45, 54, 63, 72, 81, 18, 27, 36, 45, 54, 63, 72, 81, 18, 27, 36, 45, 54, 63, 72, 81, 18, 27, 36, 45, 54, 63, 72, 81, 18, 27, 36, 45, 54, 63, 72, 81]
[i*j for j in range(1,10) for i in range(2,10)]
 
[2, 3, 4, 5, 6, 7, 8, 9, 4, 6, 8, 10, 12, 14, 16, 18, 6, 9, 12, 15, 18, 21, 24, 27, 8, 12, 16, 20, 24, 28, 32, 36, 10, 15, 20, 25, 30, 35, 40, 45, 12, 18, 24, 30, 36, 42, 48, 54, 14, 21, 28, 35, 42, 49, 56, 63, 16, 24, 32, 40, 48, 56, 64, 72, 18, 27, 36, 45, 54, 63, 72, 81]
a = [1,2,3,4]
 
result =[]
 
for num in a:
 result.append(num*3)

 
print(result)
 
[3, 6, 9, 12]
a= [1,2,34]
 
result =[num* 3 for num in a]
 
print(result)
 
[3, 6, 102]
a=[1,2,3,4]
 
result=[num*3 for num in a if num % 2 == 0]
 
print(result)
 
[6, 12]
result = [x*y for x in range(2,10)
          for y in range(1,10)
          print(result)
          
SyntaxError: '[' was never closed
result = [x*y for x in range(2,10)
          for y in range(1,10)]
          print(result)
          
SyntaxError: multiple statements found while compiling a single statement
result = [x*y for x in range(2,10)
          for y in range(1,10)]
          
print(result)
          
[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
>>> for i in range(1,5):
...           if i%2==0:
...              i*3
... 
...           
6
12
>>> [i*3 for i in range(1,5) if i i%2==0]
...           
SyntaxError: invalid syntax
>>> [i*3 for i in range(1,5) if i%2==0]
...           
[6, 12]
>>> type((i*3 for i in range(1,5) if i%2==0))
...           
<class 'generator'>
>>> type*(i*3 for i in range(1,5) if i%2==0)
...           
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    type*(i*3 for i in range(1,5) if i%2==0)
TypeError: unsupported operand type(s) for *: 'type' and 'generator'
>>> type*(i*3 for i in range(1,5) if i%2==0)<
...           
SyntaxError: incomplete input
>>> type*(i*3 for i in range(1,5) if i%2==0),
...           
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    type*(i*3 for i in range(1,5) if i%2==0),
TypeError: unsupported operand type(s) for *: 'type' and 'generator'
>>> *(i*3 for i in range(1,5) if i%2==0),
...           
(6, 12)
>>> [*(i*3 for i in range(1,5) if i%2==0)]
...           
[6, 12]
