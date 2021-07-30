## 1. 매직 메소드란?

- 클래스 안에 정의된 함수를 메소드라 부름
- __로 시작해서 __로 끝나는 메소드
- 예를 들어 __init__이라는 생성자(어떤 클래스의 객체가 생성될 때 파이썬 인터프리터에 의해 자동 호출 메소드)가 있음
```python
class Car:
    def __init__(self):
        print("자동차 제작 완료")
```

##2. 언제 매직 메소드를 사용할까?

- 매직 메소드를 사용하면 클래스를 파이썬의 내장 함수처럼 동작하도록 할 수 있음

```python
# 매직 메소드 사용 전
class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

food_1 = Food('아이스크림',3000)

print(food_1)
  
```
- class 객체를 만들고 print를 하면 할당된 메모리 주소가 나옴
- 만일 객체의 정보를 보고 싶다면 매직 메서드를 정의해줘야 함
```python
# 매직 메소드 사용 후( 매직 메소드 사용 예시1)
class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return '아이템: {}, 가격: {}'.format(self.name, self.price)

food_1 = Food('아이스크림',3000)

print(food_1)
```
- 매직 메소드를 정의했을 때 올바른 결과가 출력됨

```python
# 매직 메소드 사용 예시2
class coordinate:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return coordinate(self.x + other.x, self.y + other.y)

coord1 = coordinate(5, 7)
coord2 = coordinate(3, 9)
coord3 = coord1 + coord2
print(coord3.x)
print(coord3.y)
```
- __init__ 은 x,y의 변수를 초기화 하는 데 사용
- __add__는 x는 x끼리 더하고 y는 y끼리 더함

```python
# 비교 연산자도 매직 메소드 정의해줄 필요 있음
class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __lt__(self,other):
        if self.price <other.price:
            return True
        else:
            return False

food_1 = Food('아이스크림',3000)
food_2 = Food('햄버거', 5000)
food_3 = Food('콜라',2000)

print(food_1 < food_2)
print(food_2 < food_3)
```
- 비교 연산자 역시 매직 메서드를 정의해 줄 필요 있음