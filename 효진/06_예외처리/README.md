## 예외 처리
1. `try, except`문  
    * 기본구조
    ```
    try:
        ...
    except [발생 오류[as 오류 메시지 변수]]:
        ...
    ```
    * try, except만 쓰는 방법
        ```
        try:
            ...
        except:
            ...
        ```
    * 발생오류만 포함
        ```
        try:
            ...
        except 발생 오류:
            ...
        ```
    * 발생오류, 오류 메시지 변수 포함
        ```
        try:
            ...
        except 발생 오류 as 오류 메시지 변수:
            ...
        ```
    * try, finally  
     : `finally`절은 `try`문 수행 도중 예외 발생 여부와 상관없이 항상 수행됨.(사용한 리소스를 close해야 할 때 사용)  
    

2. 여러 개의 오류 처리
    ```
    try:
        ...
    except 발생 오류1:
        ... 
    except 발생 오류2:
        ...
    ```
    ```python
    # try문에 else절 사용
    try:
        ...
    except [발생 오류[as 오류 메시지 변수]]:
        ...
    else:  # 오류가 없을 경우에만 수행된다.
        ...
    ```
  
3. 오류 회피하기
    ```python
    try:
        f = open("나없는파일", 'r')
    except FileNotFoundError:
        pass
    ```
 
4. 오류 일부러 발생시키기 : `raise` 명령어를 사용해 오류를 강제로 발생시킴
    ```python
    class Bird:
        def fly(self):
            raise NotImplementedError
    class Eagle(Bird):
        class Eagle(Bird):
            def fly(self):
                print("very fast")
    ```
    (`NotImplementedError` : 파이썬 내장오류. 꼭 작성해야하는 부분이 구현되지 않았을 경우 일부러 오류를 발생시키기 위해 사용)

5. 예외 만들기
    ```python
    class MyError(Exception):
        pass
    ```
    * 파이썬 내장클래스인 `Exception`클래스를 상속받아 작성
    ```python
    class MyError(Exception):
        pass
    def say_nick(nick):
        if nick == '바보':
            raise MyError()
        print(nick)
    try:
        say_nick("천사")
        say_nick("바보")
    except MyError:
        print("허용되지 않는 별명입니다.")
   
    # 오류메시지를 사용하고 싶은 경우
    try:
        say_nick("천사")
        say_nick("바보")
    except MyError as e:
        print(e)
    class MyError(Exception):
        def __str__(self):
            return "허용되지 않는 별명입니다."
    ```
    