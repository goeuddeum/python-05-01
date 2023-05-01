Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= 'hello world'
>>> b=78
>>> c=1.23456
>>> 
>>> f'[a]
SyntaxError: incomplete input
>>> f'{a}
SyntaxError: incomplete input
>>> a='hello world'
>>> b=78
>>> c=1.23456
>>> 
>>> f'{a}'
'hello world'
>>> f'{b}'
'78'
>>> f"{c}'
SyntaxError: incomplete input
>>> f'{c}'
'1.23456'
>>> a=78
>>> b=.23456
>>> 
>>> f'{a} {a:x}'
'78 4e'
>>> f'{b:.0f}'
'0'
>>> f'{b:2f}'
'0.234560'
>>> f'{b;.4f}'
SyntaxError: incomplete input
>>> f'{b:.4f}'
'0.2346'
