# 두 개의 입력값을 더해주는 함수
def add(a, b):
    return a + b
a = 3
b = 4
c = add(a,b)
print(c)

#입력값이 없는 함수
def say():
    return 'Hi'
a = say()
print(a)

#결괏값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(3,4)
a = add(3,4)
print(a)

#입력값, 결괏값이 모두 없는 함수
def say():
    print('Hi')

say()

#여러 개의 입력값을 받는 함수
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

add_many(1,2,3)
add_many(1,2,3,4,5,6)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result
add_mul('add', 1,2,3,4,5)
add_mul('mul', 1,2,3,4,5)

#키워드 파라미터
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1, name='foo', age=3)

#매개변수 초깃값 설정
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 25)
say_myself("박응선", 27, False)

#lambda
add = lambda a, b: a+b
result = add(3,4)
print(result)