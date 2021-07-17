# 함수

### - 파이쎤 함수의 구조 
- def 함수명(매개변수):   
  <수행할 문장1>  
  <수행할 문장2>
### -매개변수와 인수  
- def add(a,b):  
    return a+b  
print(add(3,4))  
- a,b는 매개변수, 3,4는 인수

### - 입력값과 결괏값에 따른 함수의 형태  
<ol>일반적인 함수</ol>
<ol>입력값이 없는 함수</ol>
<ol>결과값이 없는 함수</ol>
<ol>입력값도 결과값도 없는 함수</ol>

### - return의 쓰임새
- return으로 함수 빠져나갈 수 있음

### - 매개변수에 초깃값 미리 설정하기
- 매개변수에 예를 들어 man=True 를 매개변수에 넣음.
초깃값 설정한 매개변수는 맨 뒤에 넣기.

## 함수 안에서 선언한 변수의 효력 범위
- 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과 상관 없음

## 함수 안에서 함수 밖의 변수를 변경하는 방법
1. return 사용  
2. global 명령어 사용

## lambda
- def와 동일한 역할  
- lambda 매개변수1, 매개변수2...: 매개변수를 이용한 표현식

# 사용자 입력과 출력

## 사용자 입력

- input의 사용.

## print 자세히 알기

- "" 따옴표로 둘러싸인 문자열은 +와 같음  
- 문자열 띄어쓰기는 콤마로 함  
- 한줄에 결괏값을 출력하기 위해서는 end를 사용해 끝 문자를 지정


***

# 파일 읽고 쓰기

## 파일 생성하기
파일 객체 = open(파일 이름, 파일 열기 모드)
```
f = open("새파일.txt", 'w')
f.close()
```
- r: 읽기모드  
- w: 쓰기모드 (파일이 원래 존재할 경우 내용이 모두 삭제됨)
- a: 추가모드  
```
f = open("C:/doit/새파일.txt", 'w')
f.close()
```
## 파일을 쓰기 모드로 열어 출력값 적기

```
f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
```
파일이 생성되고 파일에 내용이 적힌다.

## 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

1. readline 함수 이용하기  
- 파일의 첫번째 줄을 출력하는 함수
```
f = open("C:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()
```
- 파일의 모든 줄을 출력하는 함수
```
f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
```

2.  readlines 함수 사용하기
- \n을 붙인 줄이 출력됨
```
f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
```
- \n을 제거하기 위해서는   
'line = line.strip()' 을 추가함
  
3. read 함수 사용하기
- 파일 내용 전체를 문자열로 돌려준다.
```
f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()
```

## 파일에 새로운 내용 추가하기

- 'w'로 파일을 열면 원래 내용이 사라지기 때문에 'a'로 열면 됨
```
f = open("C:/doit/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
```

## with 문과 함께 사용하기

- f.close 대신 with문이 이 역할을 대체해 줌.
```
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
```

## sys 모듈로 매개변수 주기
```
import sys

args = sys.argv[1:]
for i in args:
    print(i)
```
- argv[0]은 sys1.py가 되고 argv[1]은 aaa, argv[2]는 bbb, 
argv[3]은 ccc이다.
  
