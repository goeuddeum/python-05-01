Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(10):
    i

    
0
1
2
3
4
5
6
7
8
9
for i in range(0,10,2):
    i

    
0
2
4
6
8
for i in range(10,0,-3):
    i

    
10
7
4
1
ist_list + 11
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ist_list + 11
NameError: name 'ist_list' is not defined


int_list _ []
SyntaxError: invalid syntax
int_list = []
for i in range(10):
    int_list.append(i)

    
int_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[i for i in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
int_list_2=[i for i in range(10)]
int_list_2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(5):
    i**2

    
0
1
4
9
16
[i**2 for i in rang(5)]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    [i**2 for i in rang(5)]
NameError: name 'rang' is not defined. Did you mean: 'range'?
[i**2 for i in range(5)]
[0, 1, 4, 9, 16]
for i in range(5)
SyntaxError: incomplete input
[i**2+i for i in range(5)]
[0, 2, 6, 12, 20]
import random
random.random()
0.5382457799769098
random.randint(0,100)
87
float);ist=[]
SyntaxError: unmatched ')'
float_list[]
SyntaxError: incomplete input
float_list=[]
for _ in range(10):
    float_list.append(random.random())

    
float_list
[0.13610654276542844, 0.6096053177641316, 0.4253496135407232, 0.06325436758660763, 0.8445282666323363, 0.4868054793864077, 0.5108432660034857, 0.41019834011112355, 0.28641473560838004, 0.21716003590452715]

int_list_2=[]
for _ in range (10):
    int_list_2.append(random.randint(0.100))

    
Traceback (most recent call last):
  File "<pyshell#43>", line 2, in <module>
    int_list_2.append(random.randint(0.100))
TypeError: Random.randint() missing 1 required positional argument: 'b'
int_list_2[]
SyntaxError: incomplete input
for _ in range(10):
    int-list_2.append(random.randit(0,100))

    
Traceback (most recent call last):
  File "<pyshell#47>", line 2, in <module>
    int-list_2.append(random.randit(0,100))
NameError: name 'list_2' is not defined. Did you mean: 'list'?
int_list_2=[]
for _ in range(10):
    int_list_2.append(random.randint(0,100))

    
int_list_2
[12, 8, 87, 92, 62, 53, 7, 4, 86, 6]
[12, 8, 87, 92, 62, 53, 7, 4, 86, 6]
[12, 8, 87, 92, 62, 53, 7, 4, 86, 6]

[random.random() for _ in range(10)]
[0.6949821967943783, 0.2794348035073393, 0.12874632312653866, 0.5980032839059289, 0.27885622188590464, 0.24065863756116412, 0.9237892127344951, 0.3002562583433609, 0.34823086629136535, 0.19515421556013135]
[random.randint(0,100) for _ in range(10)]
[23, 35, 69, 33, 51, 20, 77, 82, 75, 95]

float_list = [random.random() for _ in range(10)]

float_list
[0.19463611490778032, 0.5624714591001971, 0.5803395554665206, 0.1607325547281635, 0.07198973000595821, 0.2333108764964541, 0.47432229171538987, 0.6866192691625186, 0.08004674329466999, 0.1821102468710144]

int_list = [random.randint(0.100) for_ in range(10)]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
int_list = [random.randint(0,100) for _ in range(10)]
int_list
[34, 57, 33, 33, 32, 32, 45, 64, 45, 82]
[34, 57, 33, 33, 32, 32, 45, 64, 45, 82]
[34, 57, 33, 33, 32, 32, 45, 64, 45, 82]
import random
limpor string
SyntaxError: incomplete input
string.ascii_letters
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    string.ascii_letters
NameError: name 'string' is not defined
>>> import random
>>> imort string
SyntaxError: incomplete input
>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> random.choices(string.ascii_letters, k=10)
['G', 'S', 'w', 'a', 'Y', 'g', 'B', 'Y', 'M', 'D']
>>> ''.join(random.choices(string.ascii_letters, k=10))
'GSYtgGDMRI'
>>> str_list = []
>>> for _ in range(10):
...     str_list.append(''.join(random.choices(string.ascii_letters, k=10)))
... 
...     
>>> str_list
['vURQNObeqG', 'voFhNxzluO', 'bHpPFQHuKx', 'rpjqVyexuU', 'wFKcnyJfJo', 'RucRnHlGfr', 'ECLuMDrTMn', 'WJZbmfhGpX', 'tYejRRrOFh', 'GywRyjytRk']
>>> ['vURQNObeqG', 'voFhNxzluO', 'bHpPFQHuKx', 'rpjqVyexuU', 'wFKcnyJfJo', 'RucRnHlGfr', 'ECLuMDrTMn', 'WJZbmfhGpX', 'tYejRRrOFh', 'GywRyjytRk']
['vURQNObeqG', 'voFhNxzluO', 'bHpPFQHuKx', 'rpjqVyexuU', 'wFKcnyJfJo', 'RucRnHlGfr', 'ECLuMDrTMn', 'WJZbmfhGpX', 'tYejRRrOFh', 'GywRyjytRk']
>>> [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(10)]
['ykMTXBJYAO', 'MYRcsCWiWa', 'rpeOxAPZcV', 'KeCnsjGdsT', 'saswbZexlA', 'QygEigThkD', 'iiKEGorowD', 'LzExyZqeaJ', 'MuGPajNNPW', 'qolxzMkebV']
>>> str_list_2 = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(10)]
>>> str_list_2
['VCjxwFasDY', 'KvWUugjAgn', 'xudlVdrron', 'YObKjMhkZX', 'JblDvjnVYc', 'WsQXfUFiwV', 'jUyhyWgMrU', 'FLddZJVNUn', 'VGLyQGlSCx', 'AZSzxPFLzU']
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
