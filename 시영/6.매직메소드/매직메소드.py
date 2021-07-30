# 매직 메소드 __init__
class Car:
    def __init__(self):
        print("자동차 제작 완료")


# 매직 메소드 사용 전(예시1)
class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

food_1 = Food('아이스크림',3000)

print(food_1)

# 매직 메소드 사용 후(예시1)
class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return '아이템: {}, 가격: {}'.format(self.name, self.price)

food_1 = Food('아이스크림',3000)

print(food_1)

# 매직 메소드 예시2
class coordinate:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return coordinate(self.x + other.x, self.y + other.y)

coord1 = coordinate(5, 7)
coord2 = coordinate(3, 9)
coord3 = coord1 + coord2
print(coord3.x)
print(coord3.y)

# 매직 메소드 예시3
class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __lt__(self,other):
        if self.price <other.price:
            return True
        else:
            return False
food_1 = Food('아이스크림',3000)
food_2 = Food('햄버거', 5000)
food_3 = Food('콜라',2000)

print(food_1 < food_2)
print(food_2 < food_3)
