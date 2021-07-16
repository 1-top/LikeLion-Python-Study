# 04-1 함수

# 여러 개의 입력값을 받는 함수 - 매개변수 '*args'형태 이외의 예시
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

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("정래현", 24)
say_myself("김뚜뚜", 23, False)

