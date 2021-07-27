- 참고자료 : 제대로 파이썬

[위키독스](https://wikidocs.net/22805)

## C. 컴프리헨션

### 1) 리스트 컴프리헨션

- 리스트 생성하기

```python
numbers = []
for n in range(1, 10+1):
    numbers.append(n)
```

컴프리헨션으로 표기하면 아래와 같음.

```python
[x for x in range(10)]
```

리스트를 생성하는 방식은 `[]` 를 통해 생성.. (동일)

하지만, 컴프리헨션은 리스트 내부에 코드를 작성한다. 만약 딕셔너리 컴프리헨션 또는 셋 컴프리헨션 문법을 사용할때는 대괄호를 사용.

반복문은 별도로 작성하지 않고 리스트 컴프리헨션은 리스트 내부에 작성하여 반복한다.

리스트 컴프리헨션은 for문에서 반복되는 변수를 콜론(`:`)다음에 줄을 바꿔 들여쓰기하는것이 아니라, for문앞에 작성한다.

컴프리헨션에서 사용한 `x`는 for문 내부에서 `append`메소드에 인자로 넣은 변수 `n`과 같다. 만약 2의 배수를 10개 가지고 있는 리스트를 컴프리헨션을 사용해서 만들면 다음과 같다.

```python
[ 2*x for x in range(1, 10+1) ]
```

- 조건 걸기

ex) 1~10중 짝수만 순차적으로 들어있는 리스트 생성

일반적 방법

```python
even_numbers = []
for n in range(1, 10+1):
    if n % 2 == 0:
        even_numbers.append(n)
```

리스트 컴프리헨션 방법

```python
[x for x in range(1, 10+1) if x % 2 == 0]
```

- 중복 표현

컴프리헨션은 내부에서 `for` 키워드와 `if`키워드를 몇번이고 반복할 수 있습니다.

for

```python
[ (x, y) for x in ['쌈밥', '치킨', '피자']
for y in ['사과', '아이스크림', '커피']]

[ (x, z, y) for x in ['쌈밥', '치킨', '피자'] 
for y in ['사과', '아이스크림', '커피'] 
for z in ['배달 시키기', '가서 먹기']]
```

for문 예시

```python
for x in ['쌈밥', '치킨', '피자']:
    for y in ['사과', '아이스크림', '커피']:
        for z in ['배달 시키기', '가서 먹기']:
            print(x, z, y)
```

if

```python
[ x for x in range(10) if x < 5 if x % 2 == 0 ]
```

### 2) 딕셔너리 컴프리헨션

`{}` 중괄호를 사용해서 컴프리헨션 문법을 구현하면 set 컴프리헨션이 된다.

```python
[ x+y for x in range(10) for y in range(10) ]

{ x+y for x in range(10) for y in range(10) }
```

더불어, 중괄호를 이용하면서 `key: value` 형식으로 내용을 채우면 딕셔너리 컴프리헨션이 되어 `dict` 을 만들 수 있다.

```python
students = ['철수', '영희', '길동', '순희']
{ student: 0 for student in students }
```

dict 컴프리헨션을 이용한 dict 데이터 변경 활용

```python
scores = {'철수': 50, '영희': 80, '길동': 90, '순희': 60, '전학생': 100}
scores = { name: score for name, score in scores.items() if name != '전학생'}
print(scores)

grades = { name: 'PASS' if value > 70 else 'No-PASS' for name, value in scores.items()}
print(grades)
```

### 3) 튜플일땐??

만약 컴프리헨션으로 만든 정보를 수정할 필요가 없는 정보라면 `tuple`로 생성하는게 더 좋은 방법입니다.