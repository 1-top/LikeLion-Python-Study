# 매직메소드

# 사용자가 임의로 만든 객체에 덧셈 연산자는 그냥 수행되지 않는다.
# class Stock:
#     pass
#
# a = Stock()
# b = Stock()
# print(a +b)

# __call__
class MyFunc:
    def __call__(self, *args, **kwargs):
        print("호출됨")


f = MyFunc()
f()

# __getattriubte__
class Stock:
    def __getattribute__(self, item):
        print(item, "객체에 접근하셨습니다.")


s = Stock()
s.data