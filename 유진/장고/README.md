# 장고

### 웹 프레임워크
장고는 웹 프로그램을 __쉽고 빠르게__ 만들어주는 `프레임워크`이다.

`웹 프레임워크` 란 웹 프로그램을 위해 만들어야 할 기능(쿠키 세션 처리, 로그인 기능, 권한 처리, db 등)을 구현할 필요없이 웹 프로그램의 기능을 익혀 사용할 수 있도록 해줌. 간단하게 웹 프로그램을 만드는 키트라고 할 수 있음.

장고는 간단한 url 규칙과 함수를 작성함으로써 웹 프로그램을 만들 수 있게 함.

### 장고

파이썬의 웹 프레임워크

* 보안 기능: sql 인젝션, xss, scrf, 클릭재킹과 같은 보안 공격을 기본으로 막아줌.
* 다양한 기능: 10년 이상의 웹 프레임웤로 무수히 많은 기능이 만들어지고 추가 됨. 필요로하는 웬만한 기능이 대부분 있음.

### 파이썬 가상 환경
파이썬 프로젝트를 진행할 때 독립된 환경을 만들어주는 도구.

각각의 프로젝트는 요구하는 라이브러리의 버전이 다를 수 있는데, 이럴 때 가상 환경을 이용해서 하나의 뎃크톱에 서로 다른 버전의 파이썬과 라이브러리를 쉽게 설치해 사용할 수 있도록 함.

1. 가상 환경 생성
> 터미널
> 
>mkdir test //폴더 생성
>
> cd test //글로 이동
> 
> test> python -m venv venv(가상환경명) // 가상환경 생성

가상 환경 생성 명령을 실행하면 test 디렉토리 안에 venv라는 디렉토리가 생성되며 이 디렉토리가 가상 환경이 된다.

2. 가상 환경 진입

> cd venv
> 
> test\venv> Scripts\activate.bat

가상환경 폴더에 있는 Scripts 폴더의 activate 명령을 수행하면 가상환경에 진입한다.

> (venv) ...test\venv\Scripts>

와 같이 경로가 변경됨을 확인할 수 있다.

> test\venv\Scripts> deactivate

가상환경을 벗어나기 위해선 `deactivate` 명령을 수행하면 된다. `(venv)` 라는 프롬프트가 사라지게 됨.

### 장고 설치하기

가상 환경에 장고 설치하기

`(venv)`가 실행된 상태(가상환경 진입 상태)에서 장고 설치를 진행.

> (venv) test\venv\Scripts> pip install django(==버전, 생략 가능)

장고를 설치하는 명령

### 프로젝트 생성하기

프로젝트가 여러개가 될 수 있음으로 디렉토리 관리 잘 해야 됨.

위처럼 가상환경에 진입하고 장고를 설치한 후 장고 프로젝트를 생성한다.

1. 가상환경 폴더에 직접 생성

> (venv) test\venv\Scripts> django-admin startproject config .

2. 프로젝트 폴더 생성

> (venv) test\venv\Scripts> django-admin startproject (프로젝트명)


### 개발 서버 구동
> python manage.py runserver

http://127.0.0.1:8000/

http://localhost:8000/
입력(클릭)으로 접속


* 가상 환경 설정 배치 프로그램

https://wikidocs.net/72377

### 파이참 설정

1. 프로젝트 폴더 오픈
2. 파이썬 인터프리터 위치 설정 
>  file -> settings -> project: mysite -> project interpreter

가상 환경을 사용하므로 인터프리터 위치를 가상환경 위치로 변경.

톱니바퀴 아이콘 -> add -> existing enviroment -> 가상 환경 내 Scripts\python.exe 선택 

### settings.py

장고의 설정값이 들어 있는 파일.

* language_code 와 time_zone 설정값

> LANGUAGE_CODE = 'ko-kr'
>
> TIME_ZONE = 'Asia/Seoul'

언어와 시간 한국값으로 변경

