Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
treeHit = 0
while treeHit <
SyntaxError: incomplete input
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다")

        
나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무가 넘어갑니다
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다떨어졌습니다. 판매를 중지합니다")
        break

    
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 9개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 8개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 7개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 6개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 5개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 4개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 3개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 2개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 1개입니다.
돈을 받았으니 커피를 줍니다.
남은 커피의 양은 0개입니다.
커피가 다떨어졌습니다. 판매를 중지합니다
a=0
while a<10:
    a=a+1
    if a % 2 == 0:continue
    print(a)

    
1
3
5
7
9
# coffee.py
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다 % (money - 300))
              
SyntaxError: incomplete input
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %개입니다." % coffee)
    if coffee = 0
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %개입니다." % coffee)
    if coffee = 0:
        
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
...         coffee = coffee - 1
...     else:
...         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
...         print("남은 커피의 양은 %개입니다." % coffee)
...     if coffee == 0:
...         print("커피가 다 떨어졌습니다.판매를 중지합니다")
...         break
... 
...     
돈을 넣어 주세요: 100
돈을 다시 돌려주고 커피를 주지 않습니다.
Traceback (most recent call last):
  File "<pyshell#43>", line 11, in <module>
    print("남은 커피의 양은 %개입니다." % coffee)
ValueError: unsupported format character '?' (0xac1c) at index 11
>>> while True:
...     money = int(input("돈을 넣어 주세요: "))
...     if money == 300:
...         print("커피를 줍니다")
...         coffee = coffee - 1
...     elif money > 300:
...         print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
...         coffee = coffee - 1
...     else:
...         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
...         print("남은 커피의 양은 %개입니다." % coffee)
...     if coffee == 0:
...         print("커피가 다 떨어졌습니다.판매를 중지합니다")
...         break
... 
...     
돈을 넣어 주세요: 3000
거스름돈 2700를 주고 커피를 줍니다.
돈을 넣어 주세요: 100
돈을 다시 돌려주고 커피를 주지 않습니다.
Traceback (most recent call last):
  File "<pyshell#45>", line 11, in <module>
    print("남은 커피의 양은 %개입니다." % coffee)
ValueError: unsupported format character '?' (0xac1c) at index 11
