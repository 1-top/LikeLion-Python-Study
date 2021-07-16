### 04장 프로그램의 입력과 출력은 어떻게 해야 할까?

04-1 함수

- 파이썬 함수의 구조

```python
def 함수명(매개변수):
<수행할 문장1>
<수행할 문장2>
...
```

: def == 함수를 만들 때 사용하는 예약어

: 파이썬의 경우에는 반환자료형을 적어주지 않는다.

- 매개변수와 인수

매개변수 == 함수에 입력으로 전달된 값을 받는 변수

인수 == 함수를 호출할 때 전달하는 입력값

```python
def add(a, b):  # a, b는 매개변수
    return a+b

print(add(3, 4))  # 3, 4는 인수
```

- 입력값이 없고 결괏값만 있는 함수의 사용 ⇒ '결괏값을 받을 변수 = 함수이름()'
- 결괏값이 없는 함수의 사용 ⇒ '함수이름(입력인수1, 입력인수2, ...)'
- 입력값도 결괏값도 없는 함수 ⇒ '함수이름()'

- 여러 개의 입력값을 받는 함수

```python
def 함수이름(*매개변수): 
    <수행할 문장>
    ...

def add_many(*args): 
     result = 0 
     for i in args: 
         result = result + i 
     return result
```

: 위의 add_many 함수에서는 입력값이 몇 개이든 상관 없음. 매개변수 이름 앞에 `*` 을 붙이면 입력값을 전부 모아서 튜플로 만들어 줌.

- 키워드 파라미터 kwargs

: 키워드 파라미터를 사용할 때는 매개변수 앞에 별 두 개(**)를 붙임.

```python
def print_kwargs(**kwargs):
print(kwargs)

print_kwargs(a=1)
{'a': 1}
print_kwargs(name='foo', age=3)
{'age': 3, 'name': 'foo'}
```

- 함수의 결괏값은 언제나 하나이다

: 함수는 return을 만나는 순간 결괏값을 돌려준 다음 함수를 빠져나가게 된다!

- 매개변수에 초깃값 미리 설정하기

: 함수의 매개변수에 들어갈 값이 항상 변하는 것이 아닐 경우, 함수의 초깃값을 미리 설정해주면 유용!

: 주의점) 초기화 시키고 싶은 매개변수는 항상 뒤쪽에 놓아주어야 한다!

- 함수 안에서 선언한 변수의 효력 범위

: 지역 변수... 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 함수 밖에서는 사용되지 않는다!

- 함수 안에서 함수 밖의 변수를 변경하는 방법

1) return 사용

```python
a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a) 
print(a)
```

2) global 명령어 사용 (함수는 독립적으로 존재하는 것이 좋음. 외부 변수에 종속적인 함수는 그다지 좋은 구조가 아님. 따라서 필자 또한 가급적 global 명령어 사용대신 앞선 'return 사용'방식을 권고하고 있음)

```python
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)
```

- lambda

: lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할. 보통 함수를 한줄로 간결하게 만들 때 사용함. def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰임.

- lambda 사용법

```python
lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
```

```python
add = lambda a, b: a+b
result = add(3, 4)
print(result)
7

# 동일한 구조
def add(a, b):
...     return a+b
...
>>> result = add(3, 4)
>>> print(result)
7
```

※ lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.

04-2 사용자 입력과 출력

- 사용자 입력

: input을 사용한다!

```python
input("받을 내용")
```

```python
>>> a = input()
Life is too short, you need python
>>> a
'Life is too short, you need python'
```

input은 입력되는 모든 것을 문자열로 취급하기 때문에 숫자가 아님에 주의!

- print 자세히 알기

: 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일

: 문자열 띄어쓰기는 콤마로 한다

: 한 줄에 결괏값을 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정해주어야 함.

```python
for i in range(10):
...     print(i, end=' ')
...
0 1 2 3 4 5 6 7 8 9
```