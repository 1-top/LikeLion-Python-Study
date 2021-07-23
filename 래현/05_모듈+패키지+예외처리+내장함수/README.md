### 05-2 모듈

- 모듈

: 함수나 변수 또는 클래스를 모아 놓은 파일. 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔...

- 모듈 만들기

```python
def add(a, b):
    return a + b

def sub(a, b): 
    return a-b
```

이를 예컨대 `[mod1.py](http://mod1.py)` 라고 저장한다면 모듈이되는 것. 즉, 파이썬 확장자 `.py` 로 만든 파이썬 파일은 모두 모듈이며 그동안 작성했던 것들도 모듈임...

- 모듈 불러오기

```python
import 모듈이름

import mod1
print(mod1.add(3, 4))

from 모듈이름 import 모듈함수 (여러 개일 경우 ,를 찍어주거나 * == all을 의미)

from mod1 import add
add(3, 4)
```

※ import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.

- if **name** == "**main**": 의 의미

```python
def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
```

if **name** == "**main**"을 사용하면 C:\doit>python mod1.py처럼 직접 이 파일을 실행했을 때는 **name** == "**main**"이 참이 되어 if문 다음 문장이 수행된다. 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 **name** == "**main**"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.

- 클래스나 변수 등을 포함한 모듈

```python
a = mod2.Math()
print(a.solv(2))
12.566368
```

mod2.PI처럼 입력해서 [mod2.py](http://mod2.py/) 파일에 있는 PI 변수 값을 사용할 수 있다. 위 예처럼 모듈 안에 있는 클래스를 사용하려면 "."(도트 연산자)로 클래스 이름 앞에 모듈 이름을 먼저 입력해야 한다.

- 다른 파일에서 모듈 불러오기

다른 파이썬 파일에서도 import 모듈이름으로 해당 모듈을 불러와서 사용가능...

### 05-3 패키지

- 패키지란 무엇인가?

패키지(Packages)는 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다. 예를 들어 모듈 이름이 A.B인 경우에 A는 패키지 이름이 되고 B는 A 패키지의 B모듈이 된다.

### 05-4 예외 처리

- 오류 예외 처리 기법 - try, except문

```python
try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
```

try, except문의 기본 구조

try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

※ 위 구문을 보면 기호를 사용하는데, 이 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이다. 즉 except 구문은 다음 3가지 방법으로 사용할 수 있다.

1) try, except만 쓰는 법

: 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행함

```python
try:
    ...
except:
    ...
```

  

2) 발생 오류만 포함한 except문

: 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행함

```python
try:
    ...
except 발생 오류:
    ...
```

3) 발생 오류와 오류 메시지 변수까지 포함한 except문

: 두번째 케이스에서 오류 메시지 내용까지 알고 싶을 때 사용...

```python
try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
```

- try .. finally

finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행됨. 보통 finally절은 사용한 리소스를 close해야 할 때에 많이 사용한다.

```python
f = open('foo.txt', 'w')
try:
    # 무언가를 수행한다.
finally:
    f.close()
```

- 여러개의 오류처리하기

```python
try:
    ...
except 발생 오류1:
   ... 
except 발생 오류2:
   ...

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
```

try문에서 여러 오류 처리 시...

```python
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
```

위와 같은 형태로 2개 이상의 오류를 동일하게 처리하게끔 할 수도 있다.

+) try문에 else절 사용!

```python
try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
else:  # 오류가 없을 경우에만 수행된다.
    ...

try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
```

try문 수행중 오류가 발생하면 except절이 수행되고 오류가 없으면 else절이 수행된다.

- 오류 회피하기

```python
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass
```

단순하게 `pass` 를 이용하면 된다

- 오류 일부러 발생시키기

파이썬은 `raise` 명령어를 사용해 오류를 강제로 발생시킬 수 있음.

```python
class Bird:
    def fly(self):
        raise NotImplementedError
```

- 예외 만들기

예외는 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있음.

### 05-5 내장 함수

"Don’t Reinvent The Wheel, 이미 있는 것을 다시 만드느라 쓸데없이 시간을 낭비하지 말라"

파이썬 내장 함수는 외부 모듈과 달리 import가 필요하지 않기 때문에 아무런 설정 없이 바로 사용할 수 있다.

원문 참고...
