# 05-1 클래스

# 객체에 숫자 지정할 수 있게 만들기
# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

# 더하기 기능 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4, 2)
print(a.add())

# 곱하기, 빼기, 나누기 기능 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

# 생성자
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
print(a.first)
print(a.second)
print(a.add())
print(a.div())

# 클래스의 상속
class MoreFourCal(FourCal):
    pass
a = MoreFourCal(4,2)
a.add()
a.mul()
a.sub()
a.div()

class MoreFourCal2(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal2(4,2)
print(a.pow())

# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a = SafeFourCal(4, 0)
print(a.div())

# 클래스 변수
class Family:
    lastname = "정"
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
Family.lastname = "김"
print(a.lastname)
print(b.lastname)