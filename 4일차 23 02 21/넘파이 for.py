Python 3.10.9 (C:\Users\16\AppData\Local\Programs\Thonny\python.exe)
>>> import numpy as np
>>> np.random.randint(0,100,10)
array([80, 19, 23, 89, 93, 56, 53, 86, 10, 74])
>>> [*np.random.randint(0,100,10)]
[23, 10, 2, 48, 63, 71, 54, 67, 22, 79]
>>> *np.random.randint(0,100,10),
(22, 30, 69, 7, 75, 49, 39, 23, 52, 9)
>>> for i in np.random.randint(0,100,10):
    i
    
57
1
21
31
4
5
33
47
97
70
>>> 