Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> while True:
...     'study python'
...     python_level += 1
...     if python_level>=10:
...         break
... 
...     
'study python'
Traceback (most recent call last):
  File "<pyshell#5>", line 3, in <module>
    python_level += 1
NameError: name 'python_level' is not defined
>>> python_level = 0
>>> while True:
...     'study python'
...     python_level += 1
...     if python_level>=10:
...         break
... 
...     
'study python'
'study python'
'study python'
'study python'
'study python'
'study python'
'study python'
'study python'
'study python'
'study python'
