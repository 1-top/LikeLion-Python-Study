# 초보자를 위한 파이썬 300제 중 분기문, 반복문 부분 일부
#1. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
def print_even (num_list) :
    for i in num_list:
        if i % 2 == 0:
            print(i)

#2. 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)

#3. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def is_odd(number) :
    if number % 2 == 1:
        return True
    else:
        return False

is_odd(3)
is_odd(4)

#3 - lambda 조건식을 이용하는 경우
is_odd_lambda = lambda x: True if x % 2 == 1 else False
is_odd_lambda(3)
is_odd_lambda(4)

#4. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
def avg_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)

avg_numbers(3,4,5)

#5. 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
u_input = input("저장할 내용을 입력하세요: ")
f = open('text.txt', 'a')
f.write(user_input + "\n")
f.close()