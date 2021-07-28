## 1. 리스트 컴프리헨션  
- 리스트 생성하기  
```python
[x for x in range(10)]
```
- 리스트를 생성하는 컴프리헨션을 리스트컴프리헨션이라고 부름
```python
[ 2*x for x in range(1, 10+1) ]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```
- 2의 배수를 10개 가지고 있는 리스트컴프리헨션

----
- 조건 걸기
```python
[x for x in range(1, 10+1) if x % 2 == 0]
[2, 4, 6, 8, 10]
```
- 1부터 10까지의 숫자 중 짝수만 리스트로 생성
- if 키워드는 for문 다음에 위치해야 함
- 컴프리헨션 내부에서 for와 if는 반복 사용 가능
----

- for 문
```python
[ (x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]
[('쌈밥', '사과'),
 ('쌈밥', '아이스크림'),
 ('쌈밥', '커피'),
 ('치킨', '사과'),
 ('치킨', '아이스크림'),
 ('치킨', '커피'),
 ('피자', '사과'),
 ('피자', '아이스크림'),
 ('피자', '커피')]
```
- 왼쪽의 for문이 먼저 작동

```python
for x in ['쌈밥', '치킨', '피자']:
    for y in ['사과', '아이스크림', '커피']:
        for z in ['배달 시키기', '가서 먹기']:
            print(x, z, y)
```
- 위의 코드를 for문으로 바꾸기
---
- if문
```python
[ x for x in range(10) if x < 5 if x % 2 == 0 ]
```
- if도 중복해서 작성 가능

---
 ## 2. 딕셔너리 컴프리헨션

- 리스트 컴프리헨션을 중괄호를 이용해서 하면 set comprehension이 됨
- 중괄호를 이용하면서 동시에 key:value의 형태면 dictionary comprehension이 됨

```python
students = ['철수', '영희', '길동', '순희']
{ student: 0 for student in students }
{'철수': 0, '영희': 0, '길동': 0, '순희': 0}
```
- 학생들이 한달간 달린 거리를 저장할 dic 생성, 처음 거리를 0으로 지정

```python
scores = {'철수': 50, '영희': 80, '길동': 90, '순희': 60, '전학생': 100}
scores = { name: score for name, score in scores.items() if name != '전학생'}
print(scores)
```
- 전학간 학생 성적 제거

---
## 3. 튜플일땐

- 컴프리헨션으로 만든 정보들이 수정될 필요가 없다면 tuple이 좋은 방법
```python
( x for x in range(10) )
<generator object <genexpr> at 0x104955f68>
```

- generator 란?  
  
  * 이터레이터를 직접 만들 때 사용하는 구문을 제너레이터라고 함 
    
- 함수 내부에 yield(양보하다)가 포함되면 해당 함수는 제너레이터가 됨
- 제너레이터를 실행하고 싶다면 next 함수 사용하면 됨 -> next(제너레이터)
```python
def 함수():
  print("출력A")
  print("출력B")
  yield 100

제너레이터 = 함수()

값 = next(제너레이터)
print(값)
```
- yield란?  
  
  yield 키워드를 사용하면 함수를 정지하고 실행하게 할 수 있다
  
```python
def 함수():
  print("출력 A")
  yield 100
  print("출력 B")
  yield 200
  print("출력 C")
  yield 300
  print("출력 D")
  yield 400

제너레이터 = 함수()
for i in 제너레이터:
  print(i)
```
    * 출처: 혼자 공부하는 파이썬 40강