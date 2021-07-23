# 05-4 예외처리

# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError


# Bird 클래스를 상속받는 자식 클래스는 반드시 fly 함수를 구현해야 한다는 의지를 보여 준다.
# 만약 자식 클래스가 fly 함수를 구현하지 않은 상태로 fly 함수를 호출한다면 어떻게 될까?

# class Eagle(Bird):
#     pass
# eagle = Eagle()
# eagle.fly()
# Eagle 클래스는 Bird 클래스를 상속받음. 하지만 Eagle 클래스에서 fly함수 구현 X => Bird 클래스의 fly 함수 호출
# raise문에 의해 NotImplemented Error가 발생

class Eagle(Bird):
    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()


# 예외 만들기 -- 질문사항...
# class MyError(Exception):
#     pass
#     def say_nick(nick):
#         if nick == '바보':
#             raise MyError()
#         print(nick)
#         try:
#             say_nick("천사")
#             say_nick("바보")
#         except MyError:
#             print("허용되지 않는 별명입니다.")