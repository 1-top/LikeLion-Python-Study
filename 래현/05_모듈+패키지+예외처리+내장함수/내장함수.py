# 05-5 내장함수

# abs : 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려줌
print(abs(3))
print(abs(-3))

# all : 반복 가능한 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all([]))

# any : all의 반대

# chr : 유니코드 값을 입력받아 그 코드에 해당하는 문자 출력
print(chr(97))

# dir : dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.
print(dir([1, 2, 3]))

# divmod : divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
print(divmod(7, 3))

# enumerate(열거하다) : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# filter : filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
# 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다.
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# hex : 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수이다.
print(hex(234))

# id : 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.
a = 3
print(id(3))

# input : 사용자 입력을 받는 함수이다.
# a = input("Enter : ")
# print(a)

# int : 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.
print(int('3'))
print(int(3.4))

# (?)isinstance : 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
class Person: pass
a = Person()
isinstance(a, Person)

# len : 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.
print(len("python"))

# list : 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
print(list("python"))

# (?)map : map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.
def two_times(x):
    return x*2

list(map(two_times, [1, 2, 3, 4]))

# max : 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수이다.
print(max([1, 2, 3]))
print(max("python"))

# min : max 반대
print(min([1, 2, 3]))

# oct : 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수이다.
print(oct(34))

# open : open(filename, [mode])은 "파일 이름"과 "읽기 방법"을 입력받아 파일 객체를 돌려주는 함수이다. 읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.
# w == 쓰기 모드로 파일 열기
# r == 읽기 모드로 파일 열기
# a == 추가 모드로 파일 열기
# b == 바이너리 모드로 파일 열기
# f = open("binary_file", "rb")
# fread = open("read_mode.txt", 'r')

# ord : 문자의 유니코드 값을 돌려주는 함수이다.
print(ord('a'))

# pow : 제곱
print(pow(2,4))

# range : range([start,] stop [,step] )는 for문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다.
# 인수가 1개
print(list(range(5)))
# 인수가 2개 => 2개의 인수는 시작과 끝 숫자를 의미
print(list(range(5, 10)))
# 인수가 3개 => 세번째 인수는 숫자 사이의 거리 의미
print(list(range(1, 10, 2)))

# round : round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.
print(round(4.6))

# sorted : sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
print(sorted([3, 1, 2]))

# str : str(object)은 문자열 형태로 객체를 변환하여 돌려주는 함수이다.

# sum : sum(iterable) 은 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수이다.
print(sum((4,5,6)))

# tuple : tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다. 만약 튜플이 입력으로 들어오면 그대로 돌려준다.
print(tuple("abc"))

# type : 입력값의 자료형이 무엇인지 알려 주는 함수이다.
print(type("abc"))

# zip : 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
print(list(zip([1, 2, 3], [4, 5, 6])))
