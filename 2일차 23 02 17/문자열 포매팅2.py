Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "I eat %d apples." %3
'I eat 3 apples.'
>>> "i eat %s apples," % "five"
'i eat five apples,'
>>> number = 3
>>> "I eat %d apples." % number
'I eat 3 apples.'
>>> number = 10
>>> day = "three"
>>> " I  ate %d apples. so I was sick for %s days." % (number, day)
' I  ate 10 apples. so I was sick for three days.'
>>> "I have %s apples" % 3
'I have 3 apples'
>>> "rate is %s" % 3.234
'rate is 3.234'
>>> name=고으뜸
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    name=고으뜸
NameError: name '고으뜸' is not defined
>>> name='고으뜸'
>>> age=26
>>> '나의 이름은 {}입니다. 나이는{}입니다.'.format(name,age)
'나의 이름은 고으뜸입니다. 나이는26입니다.'
>>> '나의 이름은 %s입니다. 나이는%d입니다.'%(name,age)
'나의 이름은 고으뜸입니다. 나이는26입니다.'
>>> '%f'%3.42134234
'3.421342'
>>> '%.8f'%3.42134234
'3.42134234'
>>> '%.2f'%3.42134234
'3.42'
>>> '%.1f'%3.42134234
'3.4'
>>> '%.0f'%3.42134234
'3'
>>> '%d'%3
'3'
'%10d'%3
'         3'
'%.1f'%3.42134234
'3.4'
'{}'.format(3.42134234)
'3.42134234'
'{:.2f}'.format(3.42134234)
'3.42'
f'{3.42134234:.2f}'
'3.42'
'%f.2f'%3.42134234
'3.421342.2f'
'{:.2f}'.format(3.42134234)
'3.42'
'%s'%'hello'
'hello'
'%10s'%'hello'
'     hello'
'%-10s'%'hello'
'hello     '
