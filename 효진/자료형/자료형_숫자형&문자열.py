#####숫자형#####
#정수형
a = 123
a = -178
a = 0

#실수형
a = 1.2
a = -3.45

a = 4.24E10
a = 4.24e-10

#8진수와 16진수
a = 0o177
a = 0x8ff
b = 0xABC

#사칙연산
a = 3
b = 4
a + b
a * b
a / b

#제곱
a ** b

#나머지
7 % 3
3 % 7

#몫
7 / 4
7 // 4

#####문자열#####
"Hello World"
'Python is fun'
"""Life is too short, You need Python"""

food = "Python's favorite food is perl"
food = 'Python's favorite food is perl'

say = '"Python is very easy." he syas.'

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

print(food)
print(say)

#이스케이프 코드
multiline = "Life is too short\nYou need python"
print(multiline)

multiline = '''
Life is too short
You need python
'''
print(multiline)

multiline="""
Life is too short
You need python
"""

print(multiline)

#문자열 연산
head = "Python"
tail = " is fun!"
head + tail

a = "python"
a * 2

print("="*50)
print("My Program")
print("="*50)

a = "Life is too short"
len(a)

#문자열 인덱싱, 슬라이싱
a = "Life is too short, You need python"
a[3]
a[0]
a[12]
a[-1]
a[-0]
a[-2]

b = a[0] + a[1] + a[2] + a[3]
print(b)

a[0:4]
a[0:5]
a[5:7]
a[12:17]
a[19:]
a[:17]
a[:]
a[19:-7]

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
date
weather

year = a[:4]
day = a[4:8]

year
day

#문자열 포매팅
"I eat %d apples" %3
"I eat %s apples" % "five"
number = 3
"I eat %d apples" % number

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number,day)

"%10s" % "hi"

"%-10sjane." % 'hi'

"%0.4f" % 3.42134234

"%10.4f" % 3.42134234

"I eat {0} apples".format(3)
"I eat {0} apples".format("five")

number = 3
"I eat {0} apples".format(number)

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)

"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)

"{0:<10}".format("hi")
"{0:>10}".format("hi")
"{0:^10}".format("hi")
"{0:=^10}".format("hi")
"{0:!<10}".format("hi")

y = 3.42134234
"{0:0.4f}".format(y)
"{0:10.4f}".format(y)
"{{ and }}".format()

name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
f'나는 내년이면 {age+1}살이 된다.'

d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

f'{"hi":<10}'
f'{"hi":=^10}'
f'{y:0.4f}'
f'{{ and }}'
a = "hobby"
a.count('b')

a = "Python is the best choice"
a.find('b')
a.find('k')

a = "Life is too short"
a.index('t')
a.index('k')
",".join('abcd')
",".join(['a', 'b', 'c', 'd'])

a = "hi"
a.upper()
a = a.upper()
a.lower()

a = " hi "
a.lstrip()
a.rstrip()
a.strip()

a = "Life is too short"
a.replace("Life", "Your leg")

a = "Life is too short"
a.split()