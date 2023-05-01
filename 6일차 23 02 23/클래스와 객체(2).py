Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Student:
    def__init__(self, name, age, gender)
    self.name=name
    self.age=age
    self.gender=gender

    
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    class Student:
  File "<pyshell#6>", line 2, in Student
    def__init__(self, name, age, gender)
NameError: name 'def__init__' is not defined
class Student:
    def__init__(self, name, age, gender)
    self.name=name
    self.age=age
    self.gender=gender

    
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    class Student:
  File "<pyshell#8>", line 2, in Student
    def__init__(self, name, age, gender)
NameError: name 'def__init__' is not defined
class Student:
    def __init__(self, name, age, gender)
    self.name=name
    self.age=age
    self.gender=gender
    
SyntaxError: expected ':'
class Student:
    def __init__(self, name, age, gender):
    self.name=name
    self.age=age
    self.gender=gender
    
SyntaxError: expected an indented block after function definition on line 2
class Student:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

        
student_1=Student("홍길동,23,"남자")
                  
SyntaxError: unterminated string literal (detected at line 1)
student_1=Student("홍길동",23,"남자")
                  
student_1.name
                  
'홍길동'
student_1.age
                  
23
student_1.gender
                  
'남자'

int(3)
                  
3
i=int(3)
                  
i
                  
3
j=int(3.14)
                  
j
                  
3
dir(3)
                  
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
dir(student)
                  
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dir(student)
NameError: name 'student' is not defined. Did you mean: 'Student'?
dit(Student)
                  
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dit(Student)
NameError: name 'dit' is not defined. Did you mean: 'dir'?
class Student:
    def __init__(self, name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

        
def print(self):
    print(self.name,self.age,self.gender)

    
student_1=Student("홍길동",23,"남자")
student_1.Print()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    student_1.Print()
AttributeError: 'Student' object has no attribute 'Print'
class Student:
    def __init__(self, name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        def Print(self):
            print(self.name,self.age,self.gender)

            
student_1=Student("홍길동",23,"남자")
student_1.Print()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    student_1.Print()
AttributeError: 'Student' object has no attribute 'Print'
class Student:
    def __init__(self, name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
        def Print(self):
            print(self.name,self.age,self.gender)

            
student_1=Student("홍길동",23,"남자")
student_1.Print()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    student_1.Print()
AttributeError: 'Student' object has no attribute 'Print'
class Student:
    def __init__(self, name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

        def Print(self):
            print(self.name,self.age,self.gender)

            
student_1=Student("홍길동",23,"남자")
student_1.Print()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    student_1.Print()
AttributeError: 'Student' object has no attribute 'Print'
>>> Print()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    Print()
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> class Student:
...     def __init__(self, name,age,gender):
...         self.name=name
...         self.age=age
...         self.gender=gender
... 
...         def print(self):
...             print(self.name,self.age,self.gender)
... 
...             
>>> student_1=Student("홍길동",23,"남자")
>>> student_1.print()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    student_1.print()
AttributeError: 'Student' object has no attribute 'print'
>>> 
>>> clls RCCar:
...     
SyntaxError: invalid syntax
>>> class RCCar:
...     def __init__(self):
...         self.dir='stop'
...         self.spd= 0
...     def go_forward(self):
...         self.dir='forward'
...     def go_backward(self):
...         self.dir = 'backward'
...     def turn_left(self):
...         self.dir = 'left'
...     def turn_right(self):
...         self.dir = 'right'
...     def set_speed(self, spd):
        self.spd = spd
    def stop(self):
        self.dir = 'stop'
        self.spd = 0
    def show_state(self):
        self.dir, self.spd

        
mycar = RCCar()
mycar.go_forward()
mycar.set_speed(30)
mycar.show_state()
('forward',30)
('forward', 30)
