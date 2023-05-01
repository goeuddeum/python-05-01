>>> f=open('새파일.txt','w')
>>> f.write('hello this is my rifst file')
27
>>> f.close()
>>> f2=open('새파일.txt','r')
>>> line=f2.readline()
>>> line
'hello this is my rifst file'
>>> line
'hello this is my rifst file'
>>> f3=open('새파일.txt','r')
>>> line=f3.readline()
>>> line
'hello shell nice to meet you'
>>> f.close()
>>> f=open('새파일.txt','w')
>>> for i in range(1,100):
    f.write(f'{i} 번째 줄입니다.\n')
    >>> f.close()
>>> f=open('새파일.txt','r')
>>> line=f.readline()
>>> line
'1 번째 줄입니다.\n'
>>> line=f.readline()
>>> line
'2 번째 줄입니다.\n'
>>> f=open('새파일.txt','r')
>>> while True:
    line=f.readline()
    line
>>> f=open('새파일.txt','r')
>>> data=f.read()
>>> print(data)
>>> f.close()
>>> f=open('새파일.txt','r')
>>> lines=f.readlines()
>>> for line in lines:
    print(line)
>>> f.close()
>>> f = open("foo.twt",'w')
>>> f.write("Life is too short, you need python")
34
>>> f.close()
>>> with open("새파일.txt","w")as f:
    f.write("Life is too short, you need python")
>>> f.close()
    