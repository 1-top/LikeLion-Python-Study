# 더하기 코드
result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

# 클래스를 사용한 더하기

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 사칙연산 4.클래스 만들기
#class FourCal:
      # def setdata(self,first,second):
      # self.first = first
     # self.second = second
# a = FourCal()
# a.setdata(4,2)


# 더하기 기능 추가

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4,2)
print(a.add())

# 곱하기,뺴기, 나누기 기능 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

# 생성자
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
print(a.first)
print(a.second)
print(a.add())
print(a.div())

# 클래스의 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4,2)
print(a.pow())

# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a = SafeFourCal(4, 0)
print(a.div())

# 4.클래스 변수
class Family:
    lastname = "김"
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
Family.lastname = "박"
print(a.lastname)
print(b.lastname)

#--------------------------------
#모듈 mod1.py
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

print(add(1,4))
print(sub(4,2))

# if _name_ == "_main_" 사용
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

if __name__ == "_main_":
    print(add(1,4))
    print(sub(4,2))

# 클래스나 변수 등을 포함한 모듈

PI = 3.141592

class Math:
    def solv(self,r):
        return PI * (r ** 2)

    def add(a , b):
        return a+b
a = Math()
print(a.solv(2))

#----------------------

# 예외 처리

try:
    4/0
except ZeroDivisionError as e:
    print(e)

# 여러개의 오류 처리하기
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

# 두개 이상의 오류를 동일하게 처리하기 위해서 괄호를 묶은 예시

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# try문에 else절 사용하기
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

#-----------------------------

# abs(절대값)

print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all(모두 참이면 true, 하나라도 거짓이면 false)

print(all([1,2,3,0]))
print(all([]))

# any( 하나라도 참이 있으면 true, 모두 거짓이면 flase)

print(any([1,2,3,0]))

# chr(유니코드 입력받아서 해당 문자 출력)

print(chr(97))

# dir( 객체가 자체적으로 가지고 있는 변수, 함수)

print(dir([1,2,3]))

# divmod( (a,b)가 있을 때 a를 b로 나눈 몫과 나머지를 튜플 형태로 출력)

print(divmod(7,3))

# enumerate(1.자료형(리스트, 튜플, 문자열)을 입력받아 enumerate 객체를 돌려줌)

for i, name in enumerate(['body', 'foo' , 'bar']):
    print(i, name)

# eval(실행 가능한 문자열을 입력받아 문자열을 실행한 결과값을 돌려주는 함수)

print(eval('1+2'))

# filter( 함수 이름, 반복 가능한 1.자료형, 자료형을 함수에 입력했을 때 반환 값이 참인 것만 돌려줌)

def positive(x):
    return x>0

print(list(filter(positive, [1,-3,2,0,-5,6])))

# hex( 정수 값을 입력받아 16 진수로 변환하여 돌려주는 함수)

print(hex(234))

# id( 객체를 입력받아 고유 주소 값(레퍼런스)을 돌려주는 함수)

a=3
print(id(3))
print(id(a))
b=a
print(id(b))

# input( 사용자 입력을 받는 함수)

a = input()
print(a)

# int(정수 형태로 바꿔서 출력)

print(int(3.4))

# isinstance(첫 번째 인수: 인스턴스, 두 번째 인수: 4.클래스 이름, 그 클래스의 인스턴스이면 true, 거짓이면 false)

class Person: pass
a = Person()
print(isinstance(a, Person))

# len( 입력값의 길이)

print(len("python"))

# list( 자료형을 입력받아 리스트로 만들어서 돌려주는 함수)

print(list("python"))

# map( map(f,iterable) f가 수행한 결과를 묶어서 돌려주는 함수)

def two_times(x):
    return x*2
print(list(map(two_times, [1,2,3,4])))

# max( 최댓값 출력)

print(max([1,2,3]))

# min (최솟값 출력)

print(min([1,2,3]))

# oct(8진수 문자열로 바꿈)

print(oct(34))

# ord(유니코드 출력, chr와 반대)

print(ord('a'))

# pow(x의 y제곱)

print(pow(2,4))

# range(반복 가능한 객체로 만듦)

print(list(range(5)))
print(list(range(1,10,2))) #인수가 세 개일 때 마지막은 숫자 사이의 거리

# round(반올림)

print(round(4.6))

# sorted(정렬해서 리스트로 출력)

print(sorted([3,1,2]))

# str (문자열 형태로 객체를 변환해서 출력)

print(str(3))

# sum(입력받은 리스트나 튜플의 합)

print(sum([1,2,3]))

# tuple(튜플 형태로 바꿔서 돌려줌)

print(tuple("abc"))

#type(자료형이 무엇인지 알려줌)

print(type("abc"))

# zip(동일한 개수로 이루어진 자료형을 묶어주는 역할)

print(list(zip([1,2,3],[4,5,6])))