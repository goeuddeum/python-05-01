>> class Cookie:
    pass

>>> class Buiskit:
    ...
    
Ellipsis
>>> b=Buiskit)
  File "<stdin>", line 1
    b=Buiskit)
             ^
SyntaxError: unmatched ')'
>>> b=Buiskit()
>>> type(b)
<class '__main__.Buiskit'>
>>> c=Cookie()
>>> type(c)
<class '__main__.Cookie'>
>>> class FourCal:
    pass

>>> a=FourCal()
>>> type(a)
<class '__main__.FourCal'>

>>> class FourCal:
    def setdata(inst,first,second):
        inst.first = first
        inst.second = second
>>> a=FourCal()
>>> a.setdata(4,2)
>>> a.first
4
>>> a.second
2
>>> b=FourCal()
>>> b.setdata(3,7)
>>> id(a)
2855798912624
>>> id(b)
2855798902256
>>> b.setdata(3,7)
>>> FourCal.setdata(b,5,8)
>>> b.first
5
>>> b.second
8
>>> class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    
>>> a=FourCal()
>>> a.setdata(4,2)
>>> print(a.add())
6

>>> class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
>>> a=FourCal()
>>> b=FourCal()
>>> a.setdata(4,2)
>>> b.setdata(3,8)
>>> a.add()
6
>>> a.mul()
8
>>> a.sub()
2
>>> a.div()
2.0
>>> b.add()
11
>>> b.mul()
24
>>> b.sub()
-5
>>> b.div()
0.375

>>> class Family:
    lastname = "김"
    
>>> print(Family.lastname)
김
>>> a=Family()
>>> b=Family()
>>> print(a.lastname)
김
>>> print(b.lastname)
김

>>> Family.lastname = "박"
>>> print(a.lastname)
박
>>> print(b.lastname)
박
