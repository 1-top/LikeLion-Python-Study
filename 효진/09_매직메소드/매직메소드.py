class Myclass:
    def __init__(self, name, tall):
        self.name = name
        self.tall = tall

    def __repr__(self):  # print()했을때 이름이 나오게 정의
        return self.name

    def __add__(self, other):  # + 했을때 키가 더해지게 정의
        return self.tall + other.tall

    def __len__(self):  # len()했을때 키가 나오게 정의
        return self.tall


# print()
d = Myclass("dave", 180)
print(d)

# +
p = Myclass("park", 170)
y = Myclass("yun", 160)
print(p + y)

# len()
print(len(d))
