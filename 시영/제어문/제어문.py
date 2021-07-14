money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#비교연산자
x=3
y=2
print(x>y)
print(x==y)
print(x !=y)

#비교 연산자 예시.
money = 2000
if money >= 30000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#and,or,not 연산자
    money = 2000
    card = True
    if money>=3000 or card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")

#x in s, x not in s
        pocket = ['paper', 'cellphone', 'money']
        if 'money' in pocket:
            print("택시를 타고 가라")
        else:
            print("걸어가라")

#else if
    pocket = ['paper','handphone']
    card = True
    if 'money' in pocket:
        print("택시를 타고가라")
    elif card:
        print("택시를 타고가라")
    else:
        print("걸어가라")

#조건부 표현식
    score = 70
    message = "success" if score >= 60 else "failure"
        
#while 문의 기본 구조
    treeHit = 0
    while treeHit <10:
        treeHit = treeHit +1
        print("나무를 %d번 찍었습니다." % treeHit)
        if treeHit ==10:
            print("나무 넘어갑니다.")

#while문 빠져나가기
            
coffee = 10
 
"""while True:
    money = int(input("돈을 넣어 주세요: "))
    if money ==300:
        print("커피를 줍니다.")
        coffee = coffee-1
    elif money>300:
        print("거스름돈 %d를 주고 커피를 줍니다." %(money -300))
        coffee = coffee-1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee ==0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
        """

#while문의 맨 처음으로 돌아가기

a=0
while a<10:
    a=a+1
    if a %2 ==0: continue
    print(a)


#for문의 기본 구조
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#다양한 for문의 사용

a=[(1,2),(3,4),(5,6)]
for(first,last) in a:
    print(first+last)

#for문의 응용
marks=[90,25,67,45,80]

number = 0
for mark in marks:
    number = number+1
    if mark >=60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." %number)

#for문과 continue

marks = [90,25,67,45,80]

number = 0
for mark in marks:
    number = number+1
    if mark<60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)

#for문과 함께 자주 사용하는 range 함수

a=range(10)
print(a)

#range 함수의 예시 살펴보기
add = 0
for i in range(1,11):
    add = add +i
print(add)

marks=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number]<60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))
    

#for과 range를 이용한 구구단
"""
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
        print(' ')
        """

#리스트 내포 사용하기
a = [1,2,3,4]
result =[num * 3 for num in a]
print(result)

a=[1,2,3,4]
result = [num *3 for num in a if num % 2 ==0]
print(result)

result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)



   
