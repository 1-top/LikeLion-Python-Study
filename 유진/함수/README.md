# 함수

반복되는 부분을 묶어 함수화

함수 구조
> def 함수명(매개변수):

def 함수의 예약어
return 결과값을 돌려주는 명령어
매개변수: 함수에 입력으로 전달된 값
인수: 호출할 때 전달하는 입력값

```python
def add(a, b):
    return a+b

print(add(3,4))
```

### 함수의 형태
1. 일반적인 함수: 입력값 결과값
```python
def 함수이름(매개변수):
    수행할 문장
    return 결과값

print(함수이름(매개변수))
```
2. 입력값이 없는 함수
```python
def say():
    return "hi"

print(say())
```
3. 결과값이 없는 함수
```python
def add(a, b):
    print("합은 %d입니다." % (a+b))

add(3, 4)
```
4. 입력값 결과값 다 없는 함수
```python
def say():
    print("hi")

say()
```

* 매개변수 지정하여 호출하기
```python
result = add(a=3, b=7)
print(result)
```
순서와 상관없이 a=, b= 해주면 됨.

* 입력값 미지정
def 함수이름(__*__매개변수):
  
### input 사용자 입력
input: 입력되는 모든 것을 __문자열__로 취급

int(input())과 같은 형태로 사용할 수 있음.

### 문자열 출력 "" +
```python
print("life" "is" "too short")
# lifeistoo short
print("life"+"is"+"too short")
# lifeistoo short
```
+ 출력의 경우 붙여서 출력됨
```python
print("life", "is","too short")
# life is too short
```
컴마 , 의 경우 띄어쓰기

* 결과값 한 줄 출력 end
```python
for i in range(10):
    print(i, end='')
```
0 1 2 3 4 ...

end를 통해 끝 문자로 이어서 출력할 수 있음.


# 파일 읽고 쓰기
> f = open("새파일.txt", 'w')
> f.close()

open : 파일을 생성하기 위한 파이썬 내장함수. `파일이름`과 `파일열기모드`를 입력값으로 받고 결과값으로 파일 객체를 돌려줌.

>파일객체 = open(파일이름, 파일열기모드)

1. r 읽기모드
2. w 쓰기모드
3. 추가모드

파일을 쓰기 모드로 열면 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일 생성.

* 경로에 파일 생성
```python
f = open("c:/doit/새파일.txt", 'w')
f.close()
```
f.close() : 열려있는 파일 객체를 닫아주는 역할(생략 가능)

경로 표시할 때 /역슬래쉬를 사용할 경우 // 와 같이 역슬래쉬를 두개 사용하면 됨.

### 파일 열고 출력값 적기
```python
f = open("c:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 출입니다 \n" % i
    f.write(data)
f.close()
```
### 프로그램 외부의 저장된 파일 읽는 방법
1. readline 함수
```python
f = open("c:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()
```
읽기모드로 파일을 열고, readline을 통해 첫번째 줄 읽어 출력한 경우
```python
f = open("c:/doit/새파일.txt", 'r')
whlie True:
    line = f.readline()
if not line:
    break
    print(line)
f.close()
```
모든 줄 출력
```python
while True:
    data = input()
if not data:
    break
    print(data)
```
사용자 입력을 받아 출력하는 방법


2. readlindes 함수
```python
f = open("c:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
```
readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄 요소를 갖는 리스트로 돌려줌.
* 줄바꿈 \n 제거
```python
f = open("c:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()
```
줄 바꿈을 제거하고 사용할 경우가 많음.


3. read 함수
```python
f = open("c:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()
```
read()는 파일 전체의 내용을 문자열로 돌려줌.

### 내용 추가
원래 값을 유지하면서 새로운 값을 추가할 경우 파일 추가 모드 a로 열면 됨
```python
f = open("c:/doit/새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()
```

### with
```python
with open("foo.txt", "w") as f:
    f.write("life is too short, you need python")
```

파일을 연 후 close를 해주면 좋은데,
with문은 열고 닫는 것을 자동으로 해줌.

위와 같이 with문을 사용하면 with 블록을 벗어나는 순간 객체f가 자동으로 close 됨

### sys
sys 모듈을 사용하여 매개변수를 직접 주 수 있음.
```python
import sys

args = sys.argv[1:]
for i in args:
    print(i)
```
입력받은 인수를 for문을 사용해 하나씩 출력하는 예시.
argv[0]은 파일 이름 sys1.py가 되고, argv[1]부터는 뒤에 따라오는 인수가 차례로 argv 의 요소가 됨.
