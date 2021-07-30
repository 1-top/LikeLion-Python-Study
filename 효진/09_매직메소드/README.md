## 매직메소드
1. 개념
   * 메소드 : 클래스 안에 정의된 함수
   * 매직메소드 : 특정 클래스의 객체가 built-in 함수(혹은 사칙연산)의 input 값으로 사용될 때 그 output 값을 정의하는 것  
     (`special method`라고도 부르며, `__`로 시작해서 `__`로 끝나는 메소드를 의미. ex: `__init__`)
     
2. 활용
   * 객체를 내장타입처럼 동작하고자 할 때  
     (직접 만든 타입에서 인덱싱 기능을 제공하거나, 기본 연산자를 통해 다른 동작을 수행시키고자 할 때 등)
     
     ```python
     class Myclass:
         def __init__(self,name,tall):
             self.name=name
             self.tall=tall
    
         def __repr__(self): # print()했을때 이름이 나오게 정의
             return self.name
    
         def __add__(self,other): # + 했을때 키가 더해지게 정의
             return self.tall+other.tall
    
         def __len__(self): # len()했을때 키가 나오게 정의
             return self.tall
    
     # print()
     d=Myclass("dave",180)
     print(d)
    
     # +
     p=Myclass("park",170)
     y=Myclass("yun",160)
     print(p+y)
    
     # len()
     print(len(d))   
     ```
    
   * 함수의 호출이 `()`로 되는 이유는 매직 메소드인 `__call__` 때문이며,
     객체의 접근이 `.`으로 되는 이유는 매직 메소드인 `__getattribute__` 때문
     
3. 각 매직메소드의 기능  
   (각 기능을 막거나, 대신할 다른 기능을 추가하기 위해 매직 메소드 활용)
    * `__delattr__` : 속성을 삭제
    * `__dict__` : dictionary를 반환
    * `__eq__` : `==` 작업을 수행
    * `__ge__` : `>=` 비교를 수행
    * `__hash__` : 개체를 정수로 변환
    * `__init__` : 생성자를 호출하여 인스턴스화
    * `__new__` : 클래스의 새 인스턴스를 인스턴스화
    * `__str__` : 개체를 인쇄 가능한 형식으로 인쇄하려고 할 때 실행
    * `__add__` : `+`연산자
    * `__and__` : `&`연산자
    * `__bool__` : 부울 검사를 수행
    * `__index__` : 객체를 인덱스로 사용하려고 할때
    * `__len__` : 문자열의 길이를 반환  
    이 외에도 다양한 메소드들이 있음(참조 : https://velog.io/@hyeseong-dev/Python-magic-method%EB%9E%80)
      