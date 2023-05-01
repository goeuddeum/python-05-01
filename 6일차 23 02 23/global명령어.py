a=1
ef vartest():
    a
    
>>> vartest()
1
>>> a=2
>>> vartest()
2
def vartest():
    a=a+1
vartest()
    >> def vartest():
    global a
    a=a+1
    
>>> vartest()
>>> 
>>> a
3
>>> a
3
>>> vartest()
>>> a
4
>>> def vartest():
    global a
    a=5
>>> vartest()
>>> a
5
>>> a=4
>>> vartest()
>>> 
>>> a
5
