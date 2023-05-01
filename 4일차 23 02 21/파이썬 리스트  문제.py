Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
movei_rank=["닥터스트레인지","스플릿","럭키"]

movie_rank=["닥터스트레인지","스플릿","럭키"]
movie_rank=a
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    movie_rank=a
NameError: name 'a' is not defined
movie_rank+["배트맨"]
['닥터스트레인지', '스플릿', '럭키', '배트맨']
movie_rank
['닥터스트레인지', '스플릿', '럭키']
movie_rank.append("배트맨")
print(movie_rank)
['닥터스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,슈퍼맨)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    movie_rank.insert(1,슈퍼맨)
NameError: name '슈퍼맨' is not defined
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)
['닥터스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank.pop(3)
'럭키'
movie_rank
['닥터스트레인지', '슈퍼맨', '스플릿', '배트맨']
movie_rank.del(2:)
SyntaxError: invalid syntax
movie_rank.del[2:]
SyntaxError: invalid syntax
movie_rank.del(2)
SyntaxError: invalid syntax
del.movie_rank(2)
SyntaxError: invalid syntax
del movie_rank(2)
SyntaxError: incomplete input
del movie_rank[2]

del movie_rank[2]
print(movie_rank)
['닥터스트레인지', '슈퍼맨']
['닥터스트레인지', '슈퍼맨']
['닥터스트레인지', '슈퍼맨']
lang1=["C", "C++","JAVA"]
lang2=["Python", "Go", "C#"]
lang1+lang2
['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
langs=lang1+lang2
print(langs)
['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
nums=[1,2,3,4,5,6,7]
min(nums)
1
max(nums)
7
print("max",max(nums))
max 7
print("min",min(nums))
min 1
nums=[1,2,3,4,5]
sum nums
SyntaxError: incomplete input
print(sum(nums))
15
cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소시지","라면","팥빙수","김치전"]

print(len(cook))
12

nums=[1,2,3,4,5]
average=nums

nums
[1, 2, 3, 4, 5]
average(nums)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    average(nums)
TypeError: 'list' object is not callable
average=sum(nums)/len(nums)
print(average)
3.0
3.0
3.0

price=['20180728',100,130,140,150,160,170]
price[1:]
[100, 130, 140, 150, 160, 170]

nums=[1,2,3,4,5,6,7,8,9,10]
nums[0::2]
[1, 3, 5, 7, 9]

nums=[1,2,3,4,5,6,7,8,9,10]
nums[1::2]
[2, 4, 6, 8, 10]

nums=[1,2,3,4,5]
nums[::-1]
[5, 4, 3, 2, 1]

interest = ['삼성전자','LG전자','Naver']
print(interest[0],interest[2])
삼성전자 Naver

interest =['삼성전자','LG전자','Naver','SK하이닉스','미럐에셋대우']
print("".join(interest))
삼성전자LG전자NaverSK하이닉스미럐에셋대우
print(join(interest))
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(join(interest))
NameError: name 'join' is not defined
interest =['삼성전자','LG전자','Naver','SK하이닉스','미래에셋대우']
print("/".join(interest))
삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

string="삼성전자/LG전자/Naver"
list(string)
['삼', '성', '전', '자', '/', 'L', 'G', '전', '자', '/', 'N', 'a', 'v', 'e', 'r']
split(4,string)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    split(4,string)
NameError: name 'split' is not defined
interest=string.split("/")
print=interest
print
['삼성전자', 'LG전자', 'Naver']
>>> data=[2,4,3,1,5,10,9]
>>> print(sort(data))
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print(sort(data))
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
>>> data.sort()
>>> print
['삼성전자', 'LG전자', 'Naver']
>>> print(data)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    print(data)
TypeError: 'list' object is not callable
>>> print(data)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    print(data)
TypeError: 'list' object is not callable
>>> 
>>> 
>>> 
>>> 

>>> data2=sorted(data)
>>> print(data2)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print(data2)
TypeError: 'list' object is not callable
>>> data=[2,4,3,1,5,10,9]
>>> dara.sort()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    dara.sort()
NameError: name 'dara' is not defined. Did you mean: 'data'?
>>> data.sort()
>>> data
[1, 2, 3, 4, 5, 9, 10]
