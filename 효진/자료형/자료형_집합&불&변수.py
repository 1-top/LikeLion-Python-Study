#####집합#####
s1 = set([1,2,3])
s1
s2 = set("Hello")
s2

s1 = set([1,2,3])
l1 = list(s1)
l1[0]

#집합 연산
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s1 & s2
s1.intersection(s2)

s1 | s2
s1.union(s2)

s1 - s2
s2 - s1
s1.difference(s2)
s2.difference(s1)

s1 = set([1, 2, 3])
s1.add(4)
s1

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
s1
s1.remove(2)
s1

#####불#####
a = True
b = False
type(a)
type(b)

a = [1, 2, 3, 4]
while a :
    print(a.pop())

if [1, 2, 3]:
    print("참")
else :
    print("거짓")

bool('python')
bool('')

#####변수#####
a = 1
b = "python"
c = [1,2,3]
id(a)
a = [1,2,3]
b = a

id(a)
id(b)

a is b

b = a[:]
a[1] = 4
a
b

from copy import copy
a = [1,2,3]
b = copy(a)

b is a

a, b = ('python', 'life')
(a, b) = 'python', 'life'

[a,b] = ['python', 'life']
a = b = 'python'

a = 3
b = 5
a, b = b, a
a
b

