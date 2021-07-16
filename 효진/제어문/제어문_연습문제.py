# 초보자를 위한 파이썬 300제 중 분기문, 반복문 부분 일부
#1. 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라.
#   단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
num1 = int(input("입력값: "))
num2 = num1 + 20
if num2 > 255:
    print(255)
else:
    print(num2)

#2. 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
num1 = int(input("첫번째 숫자:"))
num2 = int(input("두번째 숫자:"))
num3 = int(input("세번째 숫자:"))
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)

#3. 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
for i in range(2002, 2051, 4) :
    print(i)

#4. 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
sum = 0
for i in range(1,11,2):
    sum += i
print("홀수의 합:",sum)

#5. 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
ans = 1
for i in range(1, 11):
    ans *= i
print(ans)