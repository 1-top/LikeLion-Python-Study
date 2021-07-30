# 파이썬 매직 메소드!!

- 참고자료 :

[위키독스](https://wikidocs.net/83755)

- 매직 메소드

: 메서드 중 `__` 로 시작해서 `__` 로 끝나는 매소드들을 매직 메소드 or 특별 메소드라고 부른다.

ex) `__init__` 과 같은 생성자... (+ 생성자 == 어떤 클래스의 인스턴스가 생성될 때 파이썬 인터프리터에 의해 자동으로 호출되는 메서드)

```java
class Car:
    def __init__(self):
        print("자동차 제작 완료")
```

- 언제 매직 메소드를 사용할까?

파이썬에서 순서가 있는 데이터 타입은 대괄호를 사용하여 인덱싱할 수 있다. 파이썬에서 클래스를 사용하면 사용자가 직접 타입을 만들 수 있는데, 사용자가 직접 만든 타입도 인덱싱 기능을 제공하려면 매직 메소드를 사용하는 것이다.

ex) 파이썬에서 문자열 객체에 대해서  `+` 덧셈 연산을 실행하면 문자열이 연결됨. 이는 파이썬 문자열 타입이 덧셈 연산에 대해 문자열이 더해지도록 정의했기 때문.

다음 코드와 같이 사용자가 만든 Stock 타입에 대해 덧셈 연산자를 수행할 때 어떤 정해진 동작이 수행되도록 하려고 할 때 매직 메소드를 사용한다.

```java
class Stock:
    pass 

a = Stock()
b = Stock()
print(a +b)

# <결과!>
Traceback (most recent call last):
  File "/Users/brayden/PycharmProjects/study/s01.py", line 7, in <module>
    print(a + b)
TypeError: unsupported operand type(s) for +: 'Stock' and 'Stock'
```

위 코드를 그냥 실행하면 덧셈 연산자를 지원하지 않는다. (에러 발생) 이를 매직 메소드를 사용해서 덧셈 연산을 지원하도록 해보쟈~!~!

- 함수도 객체

파이썬에서 함수의 호출은 이름에 `( )` 를 붙여주면 되었음. 왜 `( )` 를 붙여주면 함수가 호출될까?! 바로바로 매직메소드 떄문~~

어떤 클래스 타입에 객체가 있을 때 `( )` 를 붙여주면 해당 클래스에 정의된 매직 메소드인 `__call__` 이 호출된다.

```java
class MyFunc:
    def __call__(self, *args, **kwargs):
        print("호출됨")

f = MyFunc()
f()
```

MyFunc 클래스의 객체를 생성하고 이를 f라는 변수로 바인딩 한다. 그 다음 `f( )`와 같이 적어준다. 우리는 `( )`를 함수 호출할 때 사용한다고 생각했지만 사실은 클래스 내에 정의된 `__**call__**` 메소드를 호출하는 방법이다. f는 MyFunc 클래스의 객체이므로 `f( )`는 MyFunc 클래스에 정의된 `__**call__**` 메소드를 호출하고 그 결과로 '호출됨' 이라는 문자열이 화면에 출력된다.

사실 파이썬의 함수는 'function' 클래스의 객체이다. 즉, 함수의 이름은 다음과 같이 function 클래스의 객체를 바인딩하는 변수일 뿐이다. 그래서 func( )와 같은 표현을 통해 function 클래스에 정의된 `__call__` 메소드를 호출하는 것이다. (이를 지금까지 함수 호출이라고 불렀음)

```java
def func():
    print("hello")

func()
```

- 점(.)의 비밀

`.` 도 매직 메소드 덕분에 객체에 점찍었을 때 해당 객체에 접근할 수 있는 것이었다. 변수가 어떤 객체를 바인딩하고 있을 때 점(.)을 찍으면 클래스의 `__**getattribute__**` 라는 이름의 매직 메소드를 호출해준다.

Stock 이라는 클래스를 정의하고 `__getattribute__`라는 매직 메소드를 추가한다. 객체를 생성한 후 점을 찍고 아무 이름이나 접근해보자. `s.data`라고 코딩하면 매직 메소드인 `__getattribute__`가 자동으로 호출되고 data라는 이름 item이라는 파라미터로 전달됨을 확인할 수 있다.

```java
class Stock:
    def __getattribute__(self, item):
        print(item, "객체에 접근하셨습니다.")

s = Stock()
s.data
```

- 매직메소드의 다양한 활용사례...

[[Python] magic method란?](https://velog.io/@hyeseong-dev/Python-magic-method%EB%9E%80)
