# 매직 메소드

* 메소드 method: 클래스 안에 정의된 함수
* 매직 메소드: __(메소드명) __ 의 메소드. 특별 메소드라고도 함. 
* print(dir()) : print(dir(int)) 와 같이 사용. 출력 결과를 통해 모든 속성 및 메소드를 확인 가능. 

`__init__` (가장 유명한 매직메소드) : 생성자. 어떤 클래스의 인스턴스(객체)가 생성될 때 파이썬 인터프리터에 의해 자동으로 호출되는 메소드.

* 메직 메소드의 사용

리스트, 튜플과 같은 기본 데이터 타입 외에도, 클래스를 사용해서 직접 타입을 만들 수 있음.

순서가 있는 데이터 타입은 대괄호[]를 사용해서 인덱싱 가능. -> 매직 메소드를 통해

### 함수도 객체
> 함수명(): 함수 호출

()를 붙이면 해당 클랫에 정의된 매직 메소드 `__call__`이 호출됨으로 어떤 클래스(타입)의 객체가 있을 때 ()를 붙임으로 호출할 수 있음.

* 예시
```python
class m:
    def __call__(self, *args, **kwargs):
        print("호출")

f = m()
f()
```

1. m 클래스의 객체 생성, f 변수로 바인딩
2. f() : 함수를 호출 = 클래스의 정의된 `__call__`메소드 호출


함수 또한 'function' 클래스의 객체이며 함수의 이름은 function 클랫의 객체를 바인딩하는 변수일 뿐. func()와 같이 작성함으로써 function클래스에 정의된 `__call__` 메소드 호출하는 것.

### .의 비밀

객체에 점(.)을 찍으면 해당 객체에 접근할 수 있음 -> 이것도 매직 메소드로

변수가 어떤 객체를 바인딩하고 있을 때 점을 찍으면 클래스의 `__getattribue__`라는 이름의 매직 메소드를 호출.

* 예시
```python
class stock:
    def __getattribute__(self, item):
        print(item, "객체 접근")

s = stock()
s.data
```

1. stock 이라는 클래스 정의, `__getattribute__` 매직 메소드 추가
2. 객체 생성, 점 찍고 아무 이름이나 접근.
3. s.data 를 코딩 -> 매직 메소드인 `__getattribute__`가 자동으로 호출되고,
data라는 이름의 item 파라미터로 전달됨.
   
> data 객체 접근 # 결과

### 다양한 매직 메서드
https://docs.python.org/ko/3.7/reference/datamodel.html#special-method-names
