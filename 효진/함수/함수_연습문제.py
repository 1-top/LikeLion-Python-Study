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