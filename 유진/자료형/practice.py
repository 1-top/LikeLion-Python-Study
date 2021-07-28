# q1
ko = 80
en = 75
ma = 55
score = ko+en+ma/3
print(score)

# q2
num = 13
if num%2 == 0:
    print("짝수")
else:
    print("홀수")

#q3
jumin = '881120-1068234'
print(jumin[:6])
print(jumin[7:])

#q4
pin = "881120-1068234"
print(pin[7])

#q5
a = "a:b:c:d"
a.replace(':', '#')
print(a)

#q6
li = [1, 3, 5, 4, 2]
li.sort()
li.reverse()
print(li)

# q7
word = ['Life', 'is', 'too', 'short']
words = " ".join(word)
print(words)

# q8
tu = (1,2,3)
tu+(4,)

#q9
# 3, 리스트 키값으로 불가능

#10
a = {'A': 90, 'B': 80, 'C': 70}
a.pop('B')

#11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aset = set(a)
result = list(aset)
print(result)

#12
# b값 또한 변경됨. 동일한 메모리 주소를 가리키기 때문에.