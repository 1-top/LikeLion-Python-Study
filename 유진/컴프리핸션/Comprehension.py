# 리스트 딕셔너리

li = [ele for ele in range(1, 5)]

# 조건 추가

li_if = [x * 2 for x in li if x > 2]
print(li_if)

# for

li_for = [(x, y) for x in ['빨강', '파랑', '초록'] for y in ['보라', '노랑', '검정']]
print(li_for)

# 집합
li = {ele for ele in range(1, 5)}
# 딕셔너리
num = ['첫번째','두번째','세번째']
_dic = {num: range(1, 4) for num in num}

# 딕셔너리 컴프리헨션을 통한 리스트 데이터 변경
score = {'철수': 50, '영희': 80, '길동': 90, '순희': 60, '전학생': 100}
scores = {name: score for name, score in score.items() if name != '전학생'}
print(scores)

grades = {name: 'PASS' if value > 70 else 'No-PASS' for name, value in scores.items()}
print(grades)
