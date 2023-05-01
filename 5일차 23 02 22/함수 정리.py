Python 3.10.9 (C:\Users\16\AppData\Local\Programs\Thonny\python.exe)
>>> a,b,*c=1,2,3,4,5,6
>>> c
[3, 4, 5, 6]
>>> def f(a,b,*c):
    a
    b
    c
    
>>> f(1,2,3,4,5,6)
1
2
(3, 4, 5, 6)
>>> def g(*args):
    args
    
>>> g(1,2,3,4,5,6,7)
(1, 2, 3, 4, 5, 6, 7)
>>> *args,=1,2,3,4,5,6,7
>>> args
[1, 2, 3, 4, 5, 6, 7]
>>> g(1)
(1,)
>>> g(1,2)
(1, 2)