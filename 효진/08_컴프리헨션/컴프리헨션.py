# 리스트 컴프리헨션
# numbers = []
# for n in range(1, 10+1):
#     numbers.append(n)
[x for x in range(10)]

[2 * x for x in range(1, 10 + 1)]

# even_numbers = []
# for n in range(1, 10+1):
#     if n % 2 == 0:
#         even_numbers.append(n)
# 조건문
[x for x in range(1, 10 + 1) if x % 2 == 0]

# 중복표현
[(x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]
# for x in ['쌈밥', '치킨', '피자']:
#     for y in ['사과', '아이스크림', '커피']:
#         for z in ['배달 시키기', '가서 먹기']:
#             print(x, z, y)
[(x, z, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피'] for z in ['배달 시키기', '가서 먹기']]

[x for x in range(10) if x < 5 if x % 2 == 0]

# 딕셔너리 컴프리헨션
students = ['철수', '영희', '길동', '순희']
{student: 0 for student in students}

# 기존 딕셔너리 내용 변경
scores = {'철수': 50, '영희': 80, '길동': 90, '순희': 60, '전학생': 100}
scores = {name: score for name, score in scores.items() if name != '전학생'}

# 기존 딕셔너리 내용을 추출하여 새로운 딕셔너리 생성
grades = {name: 'PASS' if value > 70 else 'No-PASS' for name, value in scores.items()}

# 튜플
(x for x in range(10))
