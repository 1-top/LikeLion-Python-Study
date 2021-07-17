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



