# abs
abs(3)
abs(-3)
abs(-1.2)

# all
all([1,2,3])
all([1,2,3,0])      # 요소 0은 거짓이기 때문에 False를 돌려줌

# any
any([1,2,3,0])
any([0, ""])
any([])

# chr
chr(97)
chr(44032)

# dir
# 리스트, 딕셔너리 객체 관련 함수(메서드)를 보여주는 예시
dir([1,2,3])
dir({'1':'a'})

# divmod
divmod(7,3)
7 // 3
7 % 3

# enumerate
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval
eval('1+2')
eval("'hi'+'a'")
eval('divmod(4,3)')

# filter
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# 람다로 바꾼 경우
list(filter(lambda x: x > 0, [1,-3, 2, 0, -5, 6]))

# hex
hex(234)
hex(3)

# id
a = 3
id(3)
b = a
id(b)

# input
a = input()
a
b = input("Enter: ")
b

# int
int(3)
int(3.4)
# int(x,radix) : radix 진수로 표현된 문자열 x를 10진수로 변환
int('11', 2)
int('1A', 16)

# isinstance
class Person: pass
a = Person()
isinstance(a, Person)
b = 3
isinstance(b, Person)

# len
len("python")
len([1, 2, 3])
len((1, 'a'))

# list
list("python")
list((1,2,3))

# map
def two_times(x):
    return x*2

list(map(two_times, [1, 2, 3, 4]))

# 람다를 사용한 경우
list(map(lambda a : a*2, [1, 2, 3, 4]))

# max
max([1, 2, 3])

# min
min([1, 2, 3])

# oct
oct(34)
oct(12345)

# ord
ord('a')
ord('가')

# pow
pow(2, 4)
pow(3, 3)

# range
list(range(5))
list(range(5, 10))
list(range(1, 10, 2))
list(range(0, -10, -1))

# round
round(4.6)
round(5.678, 2)

# sorted
sorted([3, 1, 2])
sorted(['a', 'b', 'd', 'c'])
sorted("zero")
sorted((3,2,1))

# str
str(3)
str('hi'.upper())

# sum
sum([1, 2, 3])
sum((4, 5, 6))

# tuple
tuple("abc")
tuple([1, 2, 3])

# type
type("abc")
type([  ])

# zip
list(zip([1, 2, 3], [4, 5, 6]))
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
list(zip("abc", "def"))