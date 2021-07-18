#####리스트#####
odd = [1, 3, 5, 7, 9]

a = [1, 2, 3]
a[0]
a[0] + a[2]
a[-1]

a = [1, 2, 3, ['a', 'b', 'c']]
a[0]
a[3]
a[-1][0]

a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][2][0]

a = [1, 2, 3, 4, 5]
a[0:2]

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
b
c

#리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
a + b
a * 3
len(a)

a[2] = 4
a

del a[1]
a

a = [1, 2, 3, 4, 5]
del a[2:]
a

#리스트 함수
a = [1,2,3]
a.append(4)
a

a.append([5,6])
a

a = [1,4,3,2]
a.sort()
a
a.reverse()
a

a = [1,2,3]
a.index(3)
a.index(1)
a.insert(0,4)
a
a.insert(3,5)
a

a = [1,2,3,1,2,3]
a.remove(3)
a
a.remove(3)
a

a = [1,2,3]
a.pop()
a.pop(1)
a

a = [1,2,3,1]
a.count(1)

a = [1,2,3]
a.extend([4,5])
a
b= [6,7]
a.extend(b)
a

#####튜플#####
t1 = (1, 2, 'a', 'b')
del t1[0]
t1[0] = 'c'

#튜플 연산
t1 = (1,2, 'a', 'b')
t1[1:]

t2 = (3,4)
t1 + t2

t2 * 3

len(t1)

#####딕셔너리#####
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a = {1: 'a'}
a[2] = 'b'
a

a['name'] = 'pey'
a[3] = [1,2,3]
a

del a[1]
a

grade = {'pey': 10, 'julliet': 99}
grade['pey']
grade['julliet']

a = {1:'a', 1:'b'}
a[1]

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()

for k in a.keys() :
    print(k)

list(a.keys())

a.values()
a.items()
a.clear()
a

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a.get('name')
a.get('phone')
print(a.get('nokey'))
a.get('foo', 'bar')

'name' in a
'email' in a

