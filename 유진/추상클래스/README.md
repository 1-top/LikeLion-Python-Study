# 추상 클래스

* 파이썬에선 추상 베이스 클래스(abc)를 정의하기 위한 기반 구조를 제공함
* 메서드의 목록만 가진 클래스. 상속받는 클래스에서 메서드를 구현하지 않으면 에러 발생


객체지향프로그래밍(자바 같은)에서 `추상 클래스`란 메서드의 이름만 존재하는(메서드 구현은 없이) 클래스.

보통 객체지향 설계에서 부모 클래스에 메서드만을 정의하고 이를 상속받은 클래스가 해당 메서드를 반드시 구현하도록 강제하기 위해 사용.

* 예시

```python
from abc import *

class car(metaclass=ABCmata):
    @abstractmethod
    def drive(self):
        pass

class ks(car):
    pass

k = ks()
```
car클래스에 drive()라는 메서드가 있는데 car 클래스를 상속받은 모든 클래스에서 drive()를 재정의하도록 강제하고자 함.

위의 경우, ks 클래스는 car클래스를 상속받았지만 drive() 클래스를 정의하지 않았기 땜에 객체 생성시 에러.

```python
from abc import *

class car(metaclass = ABCMeta):
    @abstractmethod
    def drive(self):
        pass

class ks(car):
    def drive(self):
        print("ks drive")

k = ks()
```
자식 클래스 ks에서 drive 메서드를 구현하면 정상적으로 객체가 생성되고 drive 메서드도 호출됨


++++(추가)

1. 추상 클래스에서 메서드 정의하기

```python
from abc import * # 추상클래스 임폴트

class basetest(ABC):
    @abstractmethod # 추상클래스 메서드 지정
    def run(self):
        pass
    @abstractmethod # 여러개 가능
    def parse(self):
        pass

class testtset(basetest): # 상속받은 클래스에서 둘 다 정의해 줘야 됨
    def run(self):
        pass
    def parse(self):
        pass
```