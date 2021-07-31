# 클래스

클래스가 필요한 이유? 같은 것을 여러번 반복할 때 단순하게 하기 위함
-> 계산기 예시를 통해 확인

```python
result = 0
def add(num):
    global result
    result += num
return result

print(add(3))
print(add(4))
```
계산기 = __이전 계산값을 기억하고 있어야 된다__ 는 기능에 초점을 맞춰서, result를 전역변수로 선언한 후 작성.

하지만 동시에 여러개의 계산을 하려면 위 함수를 여러번 만들어야 됨. 클래스를 통해 이런 점을 간단하게 구현할 수 있음.

```python
class cal:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result

cal1 = cal()
cal2 = cal()

print(call.add(3))
print(call.add(4))
```

cal 클래스로 만든 별개의 객체 cal1, cal2는 각각 다른 일을 수행한다. 둘의 결과값 또한 독립적으로 유지됨.
객체만 생성하면 되기 때문에 각각의 연산을 하는 경우 객체를 더 생성하면 된다.

### 구현해보기
1. 클래스 구상하기

두 수를 더하는 계산기 만들기
```python
a = fourcal() # a객체 만들기
a.setdata(4,2) # 4와 2를 a에 지정
print(a.add()) # 두 수를 합한 결과 반환
```

2. 구상을 바탕으로 구조 만들기

```python
class fourcal:
    pass
```
아무 기능 없는 pass로 일단 만든다.
```python
a = fourcal() # a 객체 만들기
a.setdata(4,2) # 대상 4, 2 wlwjd
```

3. 메서드 만들기
```python
class fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
```
pass를 지우고 setdata 함수를 작성한다.

메서드 = 클래스 안에 함수

* self 매개변수는 쓰지 않고 자동으로 매서드를 호출한 객체 a가 전달된다.

4. 기능 만들기

두 개의 숫자값을 설정했으니, 더하기 기능을 갖춘 메서드를 작성한다.

```python
def add(self):
    result = self.first + self.second
    return result
```
실행
```python
a = fourcal()
a.setdata(4, 2)
print(a.add())
```

### 생성자
setdata를 먼저 수행하지 않으면 add를 사용할 수 없다.
setdata를 통해 a의 객체변수 first와 second가 생성되기 때문이다.

객체의 초기값을 설정할 필요가 있을 때는 setdata의 경우처럼 메서드를 통해 초기값을 설정하는 것보단 __생성자__ 를 구현하는 게 안전하다.

`생성자` 객체가 생성될 때 자동으로 호출되는 메서드
`__init__` 으로 사용.

###  상속
어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 개념.
* 예시: a^b 기능을 더한 클래스
```python
class morecal(fourcal):
    def pow(self):
        result = self.first ** self.second
        return result
```
> class 클래스명(상속할 클래스 이름):


### 메서드 오버라이딩
0으로 나누면 오류 발생. 이걸 수정하기 위해
```python
class safefourcal(fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second
```
여기선 부모에 있는 메서드 div를 그대로 사용했다(있다고 가정). 이것을 `메서드 오버라이딩` (덮어쓰기) 라고 한다.
