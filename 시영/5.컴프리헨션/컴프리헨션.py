# 리스트 컴프리헨션
print([ 2*x for x in range(1, 10+1) ])

# 짝수 리스트 컴프리헨션
print([x for x in range(1, 10+1) if x % 2 == 0])

# for 문
print([ (x, z, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피'] for z in ['배달 시키기', '가서 먹기']])

# if 문
print([ x for x in range(10) if x < 5 if x % 2 == 0 ])

# ---------------

# 딕셔너리 컴프리헨션 - 학생들의 달린 거리 저장할 dic 생성
students = ['철수', '영희', '길동', '순희']
print({student : 0 for student in students})

# 전학간 학생 성적 제거하기
scores = {'철수': 50, '영희': 80, '길동': 90, '순희': 60, '전학생': 100}
scores = {name: score for name, score in scores.items() if name != '전학생'}
print(scores)

# 통과, 불통과
grades = { name: 'PASS' if value > 70 else 'No-PASS' for name, value in scores.items()}
print(grades)

# --------------

# generator
def 함수():
  print("출력A")
  print("출력B")
  yield 100

제너레이터 = 함수()

값 = next(제너레이터)
print(값)

# yield
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

값 = next(제너레이터)
print(값)

# 반복문 활용
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

