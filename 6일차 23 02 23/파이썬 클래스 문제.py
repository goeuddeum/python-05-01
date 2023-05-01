class Human:
    pass
>>> class Human:
    pass

>>> areum=Human()
>>> 
>>> class Human:
    def __init__(self):
        print("응애응애")
        
>>> areum=Human()
응애응애
>>> class Human:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        
>>> areum=Human("이름",25,"여자")
>>> print(areum.name)
이름
>>> print(areum.age)
25
>>> print(areum.sex)
여자
>>> class Human:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name,self.age,self.sex))
        
>>> areum=Human("이름",25,"여자")
>>> areum.who()    #Human.who(areum)
이름: 이름 나이: 25 성별: 여자
>>> areum=Human("조아름",25,"여자")
>>> areum.who()    #Human.who(areum)
이름: 조아름 나이: 25 성별: 여자

>>> class Human:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name,self.age,self.sex))
    def setInfo(self, name,age, sex):
        self.name = name
        self.age = age
        self.sex= sex
        
>>> areum = Human("불명","미상","모름")
>>> areum.who() #Human.who(areum)
이름: 불명 나이: 미상 성별: 모름
>>> areum = Human("조아름","25","여자")
>>> areum.who() #Human.who(areum)
이름: 조아름 나이: 25 성별: 여자

>>> class Human:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def __del__(self):
        print("나의 죽음을 알리지마라")
        
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name,self.age,self.sex))
    def setInfo(self, name,age, sex):
        self.name = name
        self.age = age
        self.sex= sex
        
>>> areum=Human("아름",25,"여자")
>>> del(areum)
>>>
>>> class stock:
    def __init__(self,name,code):
        self.name=name
        self.code=code
        
>>> 삼성=stock("삼성전자","005930")
>>> print(삼성.name)
삼성전자
>>> print(삼성.code)
005930
class stock:
    def __init__(self,name,code):
        self.name=name
        self.code=code
    def set_name(self,name):
        self.name=name
    def set_code(self,code):
        self.code=code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    
    >>> 삼성=stock("삼성전자","005930")
>>> print(삼성.name)
삼성전자
>>> print(삼성.code)
005930
>>> print(삼성.get_name())
삼성전자
>>> print(삼성.get_code())
005930

>>> class stock:
    def __init__(self,name,code,PER,PBR,배당수익률):
        self.name=name
        self.code=code
        self.PER=PER
        self.PBR=PBR
        self.배당수익률=배당수익률
    def set_name(self,name):
        self.name=name
    def set_code(self,code):
        self.code=code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    
>>> 삼성=stock("삼성전자","005930",15.79,1.33,2.83)
>>> print(삼성.배당수익률)
2.83

class stock:
    def __init__(self,name,code,PER,PBR,dividend):
        self.name=name
        self.code=code
        self.PER=PER
        self.PBR=PBR
        self.dividend=dividend
    def set_name(self,name):
        self.name=name
    def set_code(self,code):
        self.code=code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def set_PER(self,PER):
        self.PER=PER
    def set_PBR(self,PBR):
        self.PBR=PBR
    def set_dividend(self,dividend):
        self.dividend=dividend
        
>>> 삼성=stock("삼성전자","005930",15.79,1.33,2.83)
>>> 삼성.set_PER(12.75)
>>> print(삼성.PER)
12.75
>>> class stock:
    def __init__(self,name,code,PER,PBR,배당수익률):
        self.name=name
        self.code=code
        self.PER=PER
        self.PBR=PBR
        self.배당수익률=배당수익률
    def set_name(self,name):
        self.name=name
    def set_code(self,code):
        self.code=code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def set_PER(self,PER):
        self.PER=PER
    def set_PBR(self,PBR):
        self.PBR=PBR
    def set_배당수익률(self,배당수익률):
        self.배당수익률=배당수익률
        
>>> 삼성=stock("삼성전자","005930",15.79,1.33,2.83)
>>> 현대차=stock("현대차","005380",8.70,0.35,4.27)
>>> LG전자=stock("LG전자","066570",317.34,0.69,1.37)
>>> 종목=[]
>>> 종목.append(삼성)
>>> 종목.append(현대차)
>>> 종목.append(LG전자)
>>> for i in 종목:
    print(i.code,i.PER)
    005930 15.79
005380 8.7
066570 317.34

    > import random
>>> class Human:
    def __init__(inst,name,age,gender):
        inst.name=name
        inst.age=age
        inst.gender=gender
    def who(inst):
        print(f'이름 : {inst.name},나이:{inst.age}, 성별{inst.gender}')
    def setInfo(inst,name,age,gender):
        inst.name=name
        inst.age=age
        inst.gender=gender
        
>>> class OMG:
    def print():
        print('Oh Mt Good')
        
>>> OMG.print()
Oh Mt Good

>>> LG=Stock('LG전자','066570',317.34,0.69,1.37)
>>> stocks=[samsung,hyundai,LG]
>>> for stocks in stocks:
    stock.code,stock.PER
    
('005930', 12.75)
('005930', 12.75)
('005930', 12.75)