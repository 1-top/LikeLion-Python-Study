# 컴프리헨션

파이썬 문법.
리스트 딕셔너리 셋(패턴이 있음)을 보다 간단하게 작성할 수 있도록 함.

### 1. 리스트 컴프리헨션
```angular2html
num = []
for n in rnage(1, 10+1)
    numbers.append(n)
```
이걸 컴프리헨션으로는
```angular2html
[x for x in range(10)]
```
으로 표현 가능

* 리스트 []는 동일, 다만 반복문을 내부에 작성하여 반복함.
[x(반복되는 변수) for x in range(10)]로 작성.
  
* 즉, 모든 원소에 각각 어떤 함수를 적용해서 그 반환값을 원소로하는 리스트를 쉽게 만들 수 있음. (=매핑한다)
* 오른쪽에서 왼쪽으로 읽기
### 2. 조건 걸기
if 키워드 지원. for문 다음에 위치함.
```angular2html
x for x in range(1, 10+1) if x % 2 == 0 ]
```
* 컴프리헨션은 for와 if 키워드를 반복 사용 가능

### 3. for / if
다중 for문 지원

[ (x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]
* 왼쪽에 있는 for문이 먼저 작동하는 순서.

if 문 또한 중복 작성 가능

 [ x for x in range(10) if x < 5 if x % 2 == 0 ]
 


### 4. 딕셔너리 컴프리헨션 
중괄호 {} 를 통해 set comprehension 작성 가능.
```angular2html
 { x+y for x in range(10) for y in range(10) }
# 위의 리스트 컴프리헨션 문법에서 {}만 바꿈.
```

중괄호와 key : value 형태를 사용하면 딕셔너리 컴프리헨션
```angular2html
students = ['철수', '영희', '길동', '순희']
{ student: 0 for student in students }
{'철수': 0, '영희': 0, '길동': 0, '순희': 0}
```
* 컴프리헨션을 통해 기존 데이터를 변경할 수도 있음.

### 5. 튜플
수정할 필요 없는 정보는 튜플로 생성하는 게 더 좋은 방법

단, 튜플은 컴프리헨션이 없기 때문에
리스트[]나 셋{}과 같은 방식으로 튜플()을 만들면 데이터 타입이 generator class임을 확인할 수 있다.

* 제너레이터

제너레이터 객체는 순회 가능
한번만 실행하고 값을 기억하지 않음
```generator = (number for number in range(1,11))
listvar = list(generator)
print(listvar) # [1~10]
relistvar = list(generator)
print(relistvar) # []
```
 이 결과를 통해,
1. 리스트로 만들기 위해 list() 함수 사용(형 변환)
2. relistvar로 하나 더 하면 결괏값 x
3. 제너레이터는 한 번만 실행 가능
