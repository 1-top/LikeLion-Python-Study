## 클래스  
1. 개념
* 필요성
```python
# 한 프로그램에서 두 개의 계산 함수가 필요한 경우
# 함수를 두 개 만든 경우
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))
```
```python
# 클래스를 사용한 경우
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
```
&#8594; Calculator 클래스로 만든 별개의 계산기(객체)가 각각의 역할을 수행. 함수를 사용했을 때 보다 간단하게 문제를 해결 할 수 있음.

* 클래스(`class`)와 객체(`object`) : 클래스는 과자 틀, 객체는 틀로 만들어진 과자.
    * 클래스로 만든 객체는 각각 고유한 성격을 가짐.(동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않음)
        ```python
        class Cookie:
            pass
    
        a = Cookie()
        b = Cookie()
        ```
        &#8594; 아무 기능도 갖고 있지 않은 클래스이지만, 무수히 많은 객체를 생성할 수 있음.
    * 객체와 인스턴스의 차이 : `a = Cookie()`에서 `a`는 객체, `a`는 `Cookie`의 인스턴스. 
      (인스턴스는 특정 객체가 어떤 클래스의 객체인지를 관계 위주로 표현할 때 사용)
      
2. 예제 - 사칙연산 클래스 만들기  
    &#10112; 클래스 구조 만들기
    ```python
    class FourCal:
        pass
    ```
    &#10113; 객채에 숫자 지정할 수 있게 만들기
    ```python
    class FourCal:
        def setdata(self, first, second):   # setdata의 매개변수
            self.first = first              # setdata의 수행문
            self.second = second            # setdata의 수행문
    ```
    * 메서드(`method`) : 클래스 안에 구현된 함수
    * 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 `self` 사용. 
      (객체를 호출할 때 객체 자신이 전달되기 때문)
    * `a.setdata(4,2)`처럼 호출하는 경우 다음과 같이 해석됨  
    ```python
    a.first = 4     # self.first = 4
    a.second = 2    # self.second = 2
    ```
    &#10114; 더하기 기능 만들기
    ```python
    class FourCal:
        def setdata(self, first, second):
            self.first = first
            self.second = second
        def add(self):
            result = self.first + self.second
            return result
    ```
    `a.add()`와 같이 호출할 경우 `result = self.first + self.second`, 곧 `result = a.first + a.second`로 해석됨    

    &#10115; 나머지 사칙연산 만들기
    ```python
    class FourCal:
        def setdata(self, first, second):
            self.first = first
            self.second = second
        def add(self):
            result = self.first + self.second
            return result
        def sub(self):
            result = self.first - self.second
            return result
        def mul(self):
            result = self.first * self.second
            return result
        def div(self):
            result = self.first / self.second
            return result
    ``` 
    &#10116; 생성자(Constructor)
    * 생성자(Constructor) : 객체가 생성될 때 자동으로 호출되는 메서드. 메서드 이름으로 `__init__`을 사용하면 생성자가 생성됨.
    ```python
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
        def sub(self):
            result = self.first - self.second
            return result
        def mul(self):
            result = self.first * self.second
            return result
        def div(self):
            result = self.first / self.second
            return result
    ```
    이 경우, `__init__` 메서드와 `setdata` 메서드의 기능이 같음.  


3. 클래스의 활용
* 상속(inheritance) : 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것.
    ```python
    # 기존에 만든 FourCal(사칙연산 계산기)에 a의 b제곱 기능을 추가할 경우
    class MoreFourCal(FourCal):
        def pow(self):
            result = self.first ** self.second
            return result
    # 기존 Fourcal은 유지하면서, 클래스의 기능을 확장
    ```
   보통 기존 클래스를 변경하지 않고 기능을 추가/변경할 때 사용. (기존 클래스가 라이브러리 형태로 제공되거나, 수정이 허용되지 않는 상황)  


* 메서드 오버라이딩(Overriding: 덮어쓰기) : 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것.
    ```python
    class SafeFourCal(FourCal):
        def div(self):
            if self.second == 0:
                return 0
            else:
                return self.first / self.second
    ```


* 클래스 변수 : 클래스 안에서 선언한 변수
    ```python
    class Family:
        lastname = "김"
    ```
  (`Family` 안에 선언한 `lastname`이 클래스 변수)
    * 클래스 변수는 `클래스이름.클래스변수`로 사용할 수 있음.  
      (`Family.lastname = "박"`을 실행하면 클래스로 만든 모든 객체의 `lastname`이 '박'으로 바뀜.)
    * 실무에서는 클래스 변수보다는 객체변수를 활용하는 비중이 높음