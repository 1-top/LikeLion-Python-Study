# 클래스

## 클래스 필요한 이유
- 더하기 기능을 구현한 코드
```
result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))
```
- 클래스를 사용하면 함수 두개를 각각 사용하지 않아도 됨

## 클래스와 객체
```
 class Cookie:
    pass
    
 a = Cookie()
 b = Cookie()
```
- 객체와 인스턴스의 차이  
  'a는 객체'  
  'a는 cookie의 인스턴스'
  
## 사칙연산 클래스 만들기
클래스 속 함수를 '메서드' 라고 부름  
- def 함수명(매개변수):  
수행할 문장
```
def setdata(self, first, second):   # ① 메서드의 매개변수
    self.first = first              # ② 메서드의 수행문
    self.second = second            # ② 메서드의 수행문
```
1. setdata 매서드의 매개변수

- 클래스이름.매서드 형태로 호출할 때는 a를 매개변수 self에 전달해 주어야 할 필요 있음.
```
a = FourCal()
 FourCal.setdata(a, 4, 2)
```
-  객체.매서드 형태로 호출할 때는 self를 호출해야 함.
```
a = FourCal()
a.setdata(4, 2)
```
2. setdata 메서드의 수행문

```
a = FourCal()
a.setdata(4, 2)
print(a.first)
4
print(a.second)
2
```

## 더하기 기능 만들기
- add 메소드 추가, print(a.add())로 더하기 기능 구현.
```
class FourCal:
     def setdata(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result
a = FourCal()
a.setdata(4, 2)
```

## 곱하기, 빼기, 나누기 기능 만들기
- mul, sub, div 모두 add 메서드에서 배운 것과 동일한 방법

## 생성자
- __init__를 사용하면 메서드는 생성자가 됨.
```
def __init__(self, first, second):
    self.first = first
    self.second = second
```
- 메서드 이름을 __init__으로 하게 되면 생성자로 인식되어 객체 생성 시점에 자동 호출됨

## 클래스의 상속
- class 클래스 이름(상속할 클래스 이름)
```
class MoreFourCal(FourCal):
```
- 수정이 허용되지 않는 상황에서  상속을 사용함

## 메서드 오버라이딩
 - 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것

## 클래스 변수

```
 class Family:
     lastname = "김"
```

- family 클래스에 선언한 lastname이 클래스 변수
- 클래스 안에 변수를 선언해서 생성
- '클래스 이름. 클래스 변수' 로 사용
- 클래스 변수는 클래스로 만든 모든 객체에 공유됨

------

## 모듈

### 모듈 만들기  
- .py로 만든 파일은 모두 모듈

### 모듈 불러오기  
- .py 파일을 불러오기 위해 import 사용
- 예시) import mod1 (뒤에 .py를 붙이지 않음)
- import의 사용방법은 다음과 같음
  ```python
  import 모듈이름
  ```
- 모듈 이름 없이 함수 이름만 쓰고 싶은 경우, 다음과 같이 작성
```python
from 모듈 이름 import 모듈 함수
```

### if __name__ == "_main_"

- if __name__ == "_main_" 을 대화형 인터프리터나 다른 파일에서 모듈을 불러서 사용할 때는
거짓이 되어 if 다음 문장이 수행되지 않음  
    

- __name__ 변수란?  
직접 파일을 실행하는 경우, _name_변수에는 _main_값이 저장됨
  하지만 파이썬 셸이나 모듈에서 import 하는 경우에, __name__ 변수에 모듈 이름 값 mod1이 저장됨
  
### 클래스나 변수 등을 포함한 모듈

- 모듈은 클래스나 변수를 포함할 수 있음
```python
PI = 3.141592

class Math: 
    def solv(self, r): 
        return PI * (r ** 2) 

def add(a, b): 
    return a+b 

>>> a = mod2.Math()
>>> print(a.solv(2))
12.566368

>>> print(mod2.add(mod2.PI, 4.4))
7.541592
 ```

### 다른 파일에서 모듈 불러오기
```python
import mod2
result = mod2.add(3, 4)
print(result)
 ```
- import로 모듈 불러와서 사용 가능(동일한 디렉터리 안에 있어야 함)


- 모듈을 불러오는 다른 방법들

1. sys.path.append  
우선 import sys를 불러오고 sys.path라고 입력하면 디렉터리를 보여줌  
   이후 sys.path.append를 사용해서 추가함  
     

2. PYTHONPATH 환경 변수 사용하기
디렉터리 이동이나 모듈 추가 없이 set PYTHONPATH를 사용하면 모듈이 불러짐
   
-----------------------

## 패키지
예를 들어 A.B의 경우 A는 패키지 이름이고 B는 A 패키지의 B모듈이 됨

## 패키지 만들기, 실행하기

1. import로 실행
2. from ...import로 실행
3. 모듈을 직접 import해서 실행


## __init__.py의 용도

- __init__.py는 디렉토리가 패키지의 일부임을 알려주는 역할
- * 사용해서 import 할 때 __init__.py 파일에 __all__변수 설정하고 
    import 할 수 있는 모듈을 정의해 주어야 함
    
## relative 패키지

- from game.sound.echo import echo_test 를 from ..sound.echo import echo_test 로 변경
- ..은 부모 디렉터리를 의미함 / .은 현재 디렉터리를 의미함

--------------------------

## 예외 처리
- 오류를 무시하고 싶을 때 try와 except를 사용해서 예외적으로 오류를 처리할 수 있게 해줌

## 오류가 나타나는 상황
- 디렉토리에 없는 파일을 열려고 할 때
- 0으로 다른 숫자를 나누는 경우
- 리스트에 없는 값을 찾을 때

## 오류 예외 처리 기법
- try, except 문

1. try, except만 쓰는 방법

```python
try:
    ...
except:
    ...
 ```
- 오류가 발생하면 except 수행

2. 발생 오류만 포함한 except문
```python
try:
    ...
except 발생 오류:
    ...
 ```
- except 문에 미리 정해놓은 오류 이름하고 일치할 때만 except 블록 수행

3. 발생 오류와 오류 메시지 변수까지 포함한 except문
```python
try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...
 ```
- 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때 사용

## try finally
- finally 절은 try문 예외 발생 여부에 상관 없이 항상 수행됨
- finally 절은 사용한 문장을 close 할 때 많이 사용함
```python
f = open('foo.txt', 'w')
try:
    # 무언가를 수행한다.
finally:
    f.close()
 ```
- try문의 예외 발생 여부와 상관 없이 finally 절 수행

## 여러개의 오류 처리하기
```python
try:
    ...
except 발생 오류1:
   ... 
except 발생 오류2:
   ...
 ```
## 오류 회피하기
-pass 사용

## 오류 일부러 발생시키기
- 자식 클래스가 특정 함수를 구현하지 않고 호출하면 오류 발생

---------------------
## 내장 함수
- 모듈과 달리 import가 필요하지 않기 때문에 설정 없이 사용 가능
- .py 파일에 정리


