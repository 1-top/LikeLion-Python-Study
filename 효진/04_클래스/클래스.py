# 사칙연산 계산 클래스
class FourCal:
    def __init__(self, first, second):          # 생성자
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
a.add()
a.mul()
a.sub()
a.div()
b = FourCal(3,7)
print(b.first)
print(b.second)

# 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
a.pow()

# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4,0)        # a = FourCal(4,0) 의 경우 오류!
a.div()

# 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)
a = Family()
b = Family()

Family.lastname = "박"
print(a.lastname)
print(b.lastname)
