##파이썬 함수의 구조
def add(a,b):
    return a+b
a=3
b=4
c= add(a,b)
print(c)

##일반적인 함수
def add(a,b):
    result =a+b
    return(result)
a = add(3,4)
print(a)

##입력값이 없는 함수
def say():
    return 'Hi'
a = say()
print(a)

##결과값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a,b,a+b))
add(3,4)

##입력값도 결과값도 없는 함수
def say():
    print('Hi')
say()

##매개변수 지정하여 호출하기
def add(a,b):
    return a+b
result = add(a=3,b=7)
print(result)

##입력값이 몇개가 될지 모를 때
def add_many(*args):
    result = 0
    for i in args:
        result = result+i
    return result
result = add_many(1,2,3)
print(result)

def add_mul(choice,*args):
    if choice == "add":
        result = 0
        for i in args:
            result = result+i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
result = add_mul('add',1,2,3,4,5)
print(result)

##키워드 파라미터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo', age=3)

##함수의 결과값은 언제나 하나
def add_and_mul(a,b):
    return a+b, a*b
result1, result2 = add_and_mul(3,4)
print(result1)
print(result2)

##함수 안에서 함수 밖의 변수를 변경하는 방법

## 1.return 사용
a=1
def vartest(a):
    a = a+1
    return a
a = vartest(a)
print(a)

## 2. global 명령어 사용
a = 1
def vartest():
    global a
    a = a+1

    vartest()
    print(a)

##lambda

add = lambda a, b:a+b
result = add(3,4)
print(result)

##프롬프트를 띄워서 사용자 입력 받기

number = input("숫자를 입력하세요: ")
print(number)

## print 사용하기

print("life", "is", "too", "short")

## 한줄에 결괏값 출력하기

for i in range(10):
    print(i, end=' ')