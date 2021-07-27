## 컴프리헨션
1. 개념 : 패턴이 있는 `list`, `dict`, `set` 등의 자료형을 작성할 수 있는 문법
2. 활용  
   (1) 리스트 컴프리헨션
   * 구문 : `[ <표현식> for <변수명> in <시퀀스>]`
      ```python
      # 1부터 10까지 정수를 순서대로 가지고 있는 리스트를 생성
      numbers = []
      for n in range(1,11):
         numbers.append(n)
      # 리스트 컴프리헨션으로 작성한 경우
      [x for x in range(10)]
      ```
   * 리스트 컴프리헨션에서는 `for`문 에서 반복되는 변수를 `for`문 앞에 작성
   * 리스트 컴프리헨션에서 `for`문 안의 x는 `append`메소드의 인자인 `n`과 동일
      ```python
      # 2의 배수를 10개 가지고 있는 리스트
      [2*x for x in range(1, 11)]
      ```
   * 조건 걸기 : `if`문을 `for`문 다음에 작성
      ```python
      # 1부터 10까지 숫자 중 짝수만 순차적으로 들어있는 리스트
      even_numbers = []
      for n in range(1,11):
         if n % 2 == 0:
            even_numbers.append(n) 
      # 리스트 컴프리헨션으로 작성한 경우
      [x for x in range(1, 10+1) if x % 2 == 0]            
      ```
   * 중복 표현 : 내부에서 `for`, `if` 키워드 반복 가능  
     (중복 표현이 가능하지만, 너무 많은 조건문을 반복해서 사용할 경우 가독성이 떨어지므로 주의)
      ```python
      for x in ['쌈밥', '치킨', '피자']:
         for y in ['사과', '아이스크림', '커피']:
            for z in ['배달 시키기', '가서 먹기']:
                print(x, z, y)
      # 리스트 컴프리헨션으로 작성한 경우
      [ (x, z, y) for x in ['쌈밥', '치킨', '피자'] 
      for y in ['사과', '아이스크림', '커피'] 
      for z in ['배달 시키기', '가서 먹기']]
      ```
      ```python
      # if문을 반복하여 사용한 경우
      [ x for x in range(10) if x < 5 if x % 2 == 0 ]
      ```
    
    (2) 딕셔너리 컴프리헨션
     * 구문 : 리스트 컴프리헨션과 동일.   
      (`[]`를 `{}`로 바꾸어 주면 `set`컴프리헨션이 되고, 동시에 `key:value`형태로 내용을 채우면 `dict`컴프리헨션이 됨)
       ```python
       # 학생들이 한달간 달린 거리를 저장한 dict 생성, 처음 거리를 0으로 지정
       students = ['철수', '영희', '길동', '순희']
       { student: 0 for student in students }
      
       # 전학간 학생 성적 제거
       scores = {'철수': 50, '영희': 80, '길동': 90, '순희': 60, '전학생': 100}
       scores = { name: score for name, score in scores.items() if name != '전학생'} 
       grades = { name: 'PASS' if value > 70 else 'No-PASS' 
                  for name, value in scores.items()}
       ```
    
   (3) 튜플 컴프리헨션
    * 구문 : 리스트 컴프리헨션과 동일.  
      (`[]`를 `()`로 바꾸면 `tuple`컴프리헨션이 됨)
      ```python
      ( x for x in range(10) )
      ```
      (컴프리헨션으로 만든 정보를 수정할 필요가 없다면 튜플로 생성)