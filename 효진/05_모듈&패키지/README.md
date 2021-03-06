## 모듈
* 모듈 : 파이썬 확장자 `.py`로 만든 파이썬 파일. 
    * `import` : 모듈 불러오기. (확장자인 `.py`를 제외하고 `import 파일명`형태로 사용)
    * 모듈 안의 함수 사용  
      &#10112; `모듈이름.모듈함수`  
      &#10113; `from 모듈이름 import 모듈함수` : 모듈 전체를 불러오지 않고,
      모듈 내의 함수를 사용하고 싶은 경우 (`from 모듈이름 import *`은 모듈 내의 모든 함수를 불러오는 방법)
      
* `__name__` : 파이썬의 내장 변수(혹은 글로벌 변수).
    * `__name__`에는 모듈 이름이 저장됨.
    * 사용할 함수가 담긴 모듈 내에서 함수를 실행시키면 `__name__` 변수에는 모듈의 이름이 아닌 `__main__`이라는 값이 저장됨
    * `import`했을 때 모듈 안의 함수뿐만 아니라 다른 코드들(ex.함수를 실행한 코드들)이 실행되는 것을 막기 위해 `if __name__ == "__main__"`으로 메인 함수 선언을 해주어야 함.
    
* 모듈을 불러오는 다른 방법
    * `sys.path.append(모듈을 저장한 디텍터리)` : 모듈의 디렉터리를 추가하여 다른 디렉토리에 있는 모듈도 사용할 수 있도록 함.
    * `PYTHONPATH` : 환경 변수. 디렉터리를 설정하여 이동 및 디렉터리 추가 없이 모듈 사용.
    
---

## 패키지
* 패키지 : 모듈을 디렉터리 형식으로 구조화한 것. (ex. `A.B`는 A패키지의 B모듈을 의미)
    * 패키지 구조로 프로그램을 만드는 것이 공동 작업 및 유지 보수 등의 면에서 유리
    * 다른 모듈과 이름이 겹치더라도 안전하게 사용할 수 있음
    
* `__init__.py` : 해당 디렉터리가 패키지의 일부임을 알려주는 역할. (패키지에 해당 파일이 없다면 패키지로 인식되지 않음)
    * `__all__` : `*`기호를 사용하여 `import`할 경우 어떤 모듈을 `import`할지 정의하는 변수.  
      (`from [] import *`에서 `[]`내에 작성된 마지막 항목이 모듈이 아닌 경우 `__all__` 변수를 설정하여야 정상적으로 실행됨)
      
* Relative 패키지 : 상대 경로
    ```
    myproject
    ├── arithmetic
    │   ├── __init__.py
    │   ├── decimal.py
    │   ├── integer.py
    │   └── util.py
    └── runner.py
    ```
    ```python
     # runner.py

     from arithmetic import decimal

     print("3 / 2 is " + str(decimal.div(3, 2)))
    ```
    위와 같은 구조를 가진 프로그램이 있다고 가정할 때, `python3`에서 `runner.py`를 실행하면 상대경로로 `import`할 수 없다는 에러가 발생.  
    (`import`경로가 `.`로 시작하지 않아서 절대경로라고 인식하지 않음. 따라서 아래와 같은 접근자를 활용)
    * `..` : 부모 디렉터리
    * `.` : 현재 디렉터리
      