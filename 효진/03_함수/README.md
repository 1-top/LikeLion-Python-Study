## 함수
1. 개념 : 입력값을 가지고 어떤 일을 수행한 다음에 그 결과물을 내어놓는 것
  (프로그램 내에서 반복적으로 사용되는 가치 있는 부분)
   

2. 구조
```
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
```


2. 용어
* 매개변수(parameter) : 함수에 입력으로 전달된 값을 받는 변수
* 인수(arguments) : 함수를 호출할 때 전달하는 입력값
* 예시
```python
def add(a, b):  # a, b -> 매개변수
    return a+b
print(add(3, 4))  # 3, 4 -> 인수
```

3. 형태
   
   (1) 일반적인 함수
    * 입력값이 있고 결괏값이 있는 함수
    ```python
    def add(a, b): 
        result = a + b 
        return result
    ```
   (2) 예외
    * 입력값이 없는 함수
    ```python
    def say():
        return 'Hi'
    ```
    * 결괏값이 없는 함수
    ```python
    def add(a, b):
        print("%d, %d의 합은 %d입니다." %(a, b, a+b))
    ```
   (문장을 출력해주지만, `return`으로 결괏값을 저장하지 않음.)
    * 입력값도 결괏값도 없는 함수
    ```python
    def say():
        print('Hi')
    ```
   (이 경우, `함수이름()`과 같은 형태로 사용)


4. 활용
* `*args`(arguments) : 매개변수 이름 앞에 `*`를 붙이면 입력값을 모아서 튜플로 만들어 줌.
```python
#  add_many(1, 2)이면 3을, add_many(1,2,3)이면 6을, 
#  add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)이면 55를 돌려주는 함수
def add_many(*args): 
    result = 0
    for i in args: 
        result = result + i 
    return result
```
```python
# 사용자의 이름을 받아서 성과 이름을 분리해주는 함수
def lastName_and_firstName(*names):
   for name in names:
       print("%s %s" % (name[0], name[1:3]), end=' ')
   return

lastName_and_firstName('안정환', '박지성')
```
(위의 예시처럼 사용자에게 입력값의 수를 제한하지 않고 입력받을 때, 입력값이 많을 때 사용)
* `kwargs` : 키워드 파라미터. 매개변수 이름 앞에 `**`를 붙이면 입력값을 딕셔너리 형태로 만들어 줌.
```python
def introduceEnglishName(**kwargs):
    for key, value in kwargs.items():
        print("{0} is {1}".format(key,value))

introduceEnglishName(Myname='Chris')
```
(`kwargs`는 `키워드 = 특정값` 형태의 함수로 호출할 수 있음.)

* 함수의 결괏값은 언제나 하나. `return`을 만나는 순간 결과값을 돌려준 다음 함수를 빠져나감. 
  (한 함수에 `return`이 여러 번 사용될 수 없으며, 결과값이 없더라도 함수를 빠져나가고 싶은 경우 `return`을 사용)
  

* 매개변수 초깃값
```python
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다" % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27) # man 변수에 입력값을 넣지 않아도 자동으로 남자로 인식
say_myself("박응용", 27, True)
say_myself("박응선", 27, False)
```
(사용자가 입력하지 않은 매개변수가 어떤 것인지 자동으로 인식하기 힘들기 때문에, 초깃값을 설정한 매개변수는 항상 뒤쪽에 작성)

* 함수 안에서 선언한 매개변수는 함수 안에서만 사용됨


* 함수는 독립적으로 존재하는 것이 좋기 떄문에 `global명령어`의 사용은 지양

5. lambda(참고자료 : https://wikidocs.net/64)
* 함수를 생성할 때 사용하는 예약어. `def`와 동일한 역할.
```python
#lamnda를 사용한 경우
add = lambda a,b : a+b
result = add(3,4)

#def를 사용한 경우
def add(a,b):
    return a+b
result = add(3,4)
```
* 함수를 파라미터로 받는 함수에서 사용(ex.`map()`, `filter()`)
    * `map(함수,리스트)` : 리스트 안의 요소에 함수를 적용시키고, 그 결과를 새로운 리스트에 담아주는 함수
      ```python
      # 리스트 안의 모든 요소를 제곱
      map(lambda x: x**2, range(5))
      ```
    * `filter(함수,리스트)` : 리스트의 요소들을 함수에 적용시켜, 결과가 참이 값들로 새로운 리스트 생성
      ```python
      # 리스트 안에서 5보다 작은 요소들 추출
      filter(lambda x: x<5, range(10))
      ```

6. 사용자 입력과 출력
* `input()` : 입력되는 모든 것을 문자열로 취급. 안내문구는 괄호 안에 작성.
* `print()` : 자료형을 출력.
   * 문자열 띄어쓰기는 `,`사용
   * 한 줄에 결과값을 출력하기 위해서는 매개변수 `end`사용
    
7. 파일 읽고 쓰기  
   (1) 파일 생성하기
   ```python
   f = open("새파일.txt", "w")
   f.close
   ```
    * `파일객체 = open(파일 이름, 파일 열기 모드)`의 형태로 사용  

   |**파일열기모드**|설명|
   |:---:|:---|
   |**r**|읽기모드 - 파일을 읽기만 할 때 사용|
   |**w**|쓰기모드 - 파일에 내용을 쓸 때 사용|
   |**a**|추가모드 - 파일의 마지막에 새로운 내용을 추가시킬 때 사용|

    * 파일경로와 슬래시(`/`) : 파일 경로를 표시할 때는 슬래시 사용. 역슬래시(`\`)를 사용할 경우 `\n`과 같은
    이스케이프 문자가 있을 경우 줄바꿈으로 인식되어 파일 경로가 달라짐.

    (2) 쓰기모드로 열기
    ```python
    # writedata.py
    f = open("새파일.txt", 'w')
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close
    ```
    ```python
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        print(data)
    ```   
   첫번째 방법은 파일에 결과값을 저장하고, 두번째 방법은 모니터에만 결과값을 출력하는 방법

   (3) 파일 읽기
    * `readline()` : 파일을 한줄 한 줄 읽어오는 방법
    ```python
    f = open("새파일.txt", 'r')
    line = f.readline()
    print(line)
    f.close()
    ```
    ```python
    # readlined_all.py (파일의 모든 줄을 읽어오고 싶을 때)
    f = open("새파일.txt", 'r')
    while True:
        line = f.readline()
        if not line : break
        print(line)
    f.close()
    ```
    * `readlines()` : 파일의 모든 줄을 읽어오는 방법
    ```python
    f = open("새파일.txt", 'r')
    lines = f.readlines()
    for line in lines :
        line = line.strip() # 줄 끝의 줄바꿈 문자(\n)를 제거
        print(line)
    f.close
    ```
    * `read` : 파일의 내용 전체를 읽어오는 방법
    ```python
    f = open("새파일.txt", 'r')
    data = f.read()
    print(data)
    f.close
    ```

    (4) 파일에 새로운 내용 추가하기
    ```python
    f = open("새파일.txt", 'a')
    for i in range(11, 20):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()   
    ```
   
    (5) `with`문
    ```python
    with open("foo.txt", "w") as f:
        f.write("Life is too short, you need python")
    ```
    `with`문을 사용하게 되면 with 블록을 벗어나는 순간 f(파일객체)가 자동을 close됨.
   
    (6) `sys` 모듈로 매개변수 주기(참고자료: https://wikidocs.net/78)
    * `sys`모듈 : 파이썬 인터프리터를 제어할 수 있는 방법.
    * `argv` : argument(인수). `sys` 모듈의 `argv`는 명령 창에서 직접 입력한 인수를 의미.
    ```python
    # 입력받은 값을 출력해주는 프로그램
    import sys
    
    args = sys.argv[1:]
    for i in args:
        print(i)
    ```
    ```python
    # 입력받은 값을 대문자로 바꾸어 주는 프로그램
    import sys
    args = sys.argv[1:]
    for i in args:
        print(i.upper(), end=' ')
    ```