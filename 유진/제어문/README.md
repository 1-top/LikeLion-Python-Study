# 제어문

### if
들여쓰기 주의(자바와 다르게)

* 비교연산자 ==, !=, >, <, >=, <=
* 판단연산자 and, or, not

* 파이썬에만 있는 기능

x (not) in 리스트, x in 튜플, x in 문자열

* pass 아무 실행도 하지 않음

* elif == else if

### while 반복문

* break 반복문 중지
* continue 실행 멈추고 돌아가기

### 무한루프
1. 형식: while True

2. ctrl + c 강제 종료

### for
> for 변수 in 리스트(튜플, 문자열):

* range
> for i in range(시작, 끝, 간격):

1. 시작, 간격 생략 가능

2. 디폴트: 0부터 1씩 증가 

### 리스트 내포 사용
더 직관적인 표현 가능
> a = [1, 2, 3, 4]
> 
> result = []
> 
> for num in a:
> 
>       result.append(num*3)

 > a = [1, 2, 3, 4]
> 
> result = [num * 3 for num in a]

로 간략하게 표현 가능
