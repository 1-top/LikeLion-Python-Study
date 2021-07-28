#1.자료형.py

##[문자형 1.자료형]

#문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

#문자열 길이 구하기
a= "Life is too short"
print(len(a))

#슬라이싱으로 문자열 나누기
a="20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

#문자열 포매팅 숫자,문자,변수,2개 이상의 값 바로 대입
print("I eat %d apples" %3)
print("I eat %s apples" %"five")
number=3
print("I eat %d apples" %number)
number=10
day="three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

#format 함수를 사용한 포매팅
print( " I eat {0} apples".format(3))
print(" I eat {0} apples".format("five"))
number =3
print("I eat {0} apples".format(number))
number=10
day="three"
print( "I ate {0} apples. so I was sick for {1} days".format(number, day))
print("I ate {number} apples. so I was sick for {day} days".format(number =10,  day=3))
print("I ate {0} apples. so I was sick for {day} days".format(10, day=3))
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
y= 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("{{and}}".format())

#문자열 관련 함수들
a = "hobby"
print(a.count('b')) #세기
a="Python is the best choice"
print(a.find('b')) #위치 알려주기
print(a.find('k'))
a = "Life is too short"
print(a.index('t')) #맨 처음으로 나온 위치 반환하기
print(",".join('abcd')) #문자열 삽입
a= "hi"
print(a.upper()) #대문자, 소문자로 바꾸기
a="HI"
print(a.lower())
a = " hi "
print(a.lstrip())#공백 지우기
print(a.rstrip())
print(a.strip())
a="Life is too short" #문자열 바꾸기
print(a.replace("Life" ,"Your leg"))
print(a.split()) #문자열 나누기
b = "a:b:c:d"
print(b.split(':'))

##리스트 1.자료형

a= [1,2,['a','b',['Life','is']]] #삼중 리스트에서 인덱싱하기
print(a[2][2][0])
a = [1,2,3,['a','b','c'], 4, 5]
print(a[3][:2])
#리스트 연산하기
a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a*3)
print(len(a))
#리스트 수정과 삭제
#수정
a = [1,2,3]
a[2] = 4
print(a)
#삭제
del a[1]
print(a)

#리스트 관련 함수들
#추가
a = [1,2,3]
a.append(4)
print(a)
a.append([5,6])
print(a)
#정렬
a = [1,4,3,2]
a.sort()
print(a)
#뒤집기
a.reverse()
print(a)
#위치 반환
a = [1,2,3]
print(a.index(3))
#요소 삽입
a.insert(0,4)
print(a)
#요소 제거
a.remove(3) #첫 번째로 나오는 x값을 삭제
print(a)
#끄집어내기
a = [1,2,3]
print(a.pop())
print(a)
#리스트에 포함된 x의 요소 세기
a = [1,2,3,1]
print(a.count(1))
#리스트 확장
a = [1,2,3]
a.extend([4,5])
print(a)

##[튜플 1.자료형]

t1=(1,2,'a','b')
print(t1[0])#튜플 인덱싱하기
print(t1[1:])#튜플 슬라이싱하기
t1 = (1,2,'a','b')
t2 = (3,4)
print(t1+t2)#튜플 더하기
t2 = (3,4)
print(t2 * 3) #튜플 곱하기
print(len(t1))#튜플 길이 구하기

##[딕셔너리 1.자료형]
a = {1: 'a'} #딕셔너리에 쌍 추가하기
a[2]='b'
print(a)
#딕셔너리 요소 삭제하기
del a[1]
print(a)
#딕셔너리를 사용하는 방법(key를 사용해 value 얻기)
grade = {'pey' : 10, 'julliet':99}
print(grade['pey']) #딕셔너리변수이름[key]

#딕셔너리 관련 함수들
a = { 'name' : 'pey', 'phone': '01099993333', 'birth' : '1118'}
print(a.keys()) #key 리스트 만들기
for k in a.keys():
    print(k)

print(a.values()) #value 리스트 만들기
print(a.items()) #key와 value 쌍 얻기
print(a.get('name')) #key로 value 얻기
print('name' in a)

##[집합 1.자료형]
s1 = set("Hello")
print(s1)
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)#교집합
print(s1.intersection(s2))
print(s1|s2)#합집합
print(s1.union(s2))
print(s1-s2)#차집합
print(s1.difference(s2))

s1 = set([1,2,3])#값 1개 추가하기
s1.add(4)
print(s1)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)
s1 = set([1,2,3])
s1.remove(2)
print(s1)

##불 1.자료형
a = True #불 1.자료형 소개
b = False
print(type(a))
print(1==1) #true, false

##자료형의 값을 저장하는 공간, 변수
a=3
b=5
a,b=b,a
print(a)
print(b)









