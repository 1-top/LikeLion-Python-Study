# 컴프리헨션

# 리스트 컴프리헨션
# 리스트 생성하기 (일반적 방법)
numbers = []
for n in range(1, 10+1):
    numbers.append(n)

# 리스트 컴프리헨션으로 표기
[x for x in range(10)]

# 2의 배수를 10개 가지고 있는 리스트 예시
print([ 2*x for x in range(1, 10+1) ])


# 조건 걸기
even_numbers = []
for n in range(1, 10+1):
    if n % 2 == 0:
        even_numbers.append(n)

# 조건 걸기(컴프리헨션)
print([x for x in range(1, 10+1) if x % 2 == 0])


# 중복 표현
# for
[ (x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]

[ (x, z, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피'] for z in ['배달 시키기', '가서 먹기']]

# if
[ x for x in range(10) if x < 5 if x % 2 == 0 ]


# 딕셔너리 컴프리헨션
print({ x+y for x in range(10) for y in range(10) })

students = ['철수', '영희', '길동', '순희']
print({ student: 0 for student in students })

scores = {'철수': 50, '영희': 80, '길동': 90, '순희': 60, '전학생': 100}
scores = { name: score for name, score in scores.items() if name != '전학생'}
print(scores)

grades = { name: 'PASS' if value > 70 else 'No-PASS' for name, value in scores.items()}
print(grades)


# 튜플일땐 ??
print(( x for x in range(10) ))
# 튜플이 결과로 나올거라 예상했는데, 기대하지 않은 결과 산출
# <generator object <genexpr> at 0x0000018916F036D0>
