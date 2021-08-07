[[무료] Django 초보 가이드 - 실습을 통해 알아보는 장고 입문 - 인프런 | 강의](https://www.inflearn.com/course/django-%EC%B4%88%EB%B3%B4-%EA%B0%80%EC%9D%B4%EB%93%9C-%EC%8B%A4%EC%8A%B5%EC%9D%84-%ED%86%B5%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-%EC%9E%A5%EA%B3%A0-%EC%9E%85%EB%AC%B8#curriculum)

## 웹 프레임워크 Django 개념 정리

### MVC & MTV

- Model : 안전하게 데이터를 저장
- View : 데이터를 적절하게 유저에게 보여줌
- Control, Template : 사용자의 입력과 이벤트에 반응하여 Model과 View를 업데이트

⇒ 특정 영역을 분리하여 관리 운용할 수 있게 하는 방법!!

### Project와 App

- 프로젝트 = 하나의 웹 사이트
- 앱 = 사이트 안에 존재하는 기능

    (명령어)

    프로젝트 생성 : django-admin startproject 프로젝트이름

    app 생성 : cd 프로젝트명 → python [manage.py](http://manage.py) startapp 앱 이름

### settings.py

프로젝트 환경 설정 파일

- DEBUG : 디버그 모드 설정 (개발할때만 True로 활용한다)
- INSTALLED_APPS : pip로 설지한 앱 또는 본인이 만든 app을 추가
- MIDDELWARE_CLASSES : request와 responese 사이의 주요 기능 레이어
- TEMPLATES : django template 관련 설정, 실제 뷰 (html, 변수)
- DATABASES : 데이터베이스 엔진의 연결 설정
- STATIC_URL : 정적 파일의 URL(css, javascript, image ...)

### manage.py

- 프로젝트 관리 명령어 모음
- 주요 명령어
    - startapp : 앱 생성
    - runserver : 서버 실행
    - createsuperuser : 관리자 생성
    - makemigrations app : app의 모델 변경 사항 체크
    - migrate : 변경 사항을 DB에 반영
    - shell : 쉘을 통해 데이터를 확인
    - collectstatic : static파일을 한 곳에 모음

---

# 멋사 장고 강의

## Django 실습 [2]

### 앱 제작 순서

1. App을 생성
2. Template 제작
3. View 제작
4. URL 연결

## Django - Model 실습

- python [manage.py](http://manage.py) makemigrations

models.py의 변경사항을 감지해서 migrations에 저장시켜줌

- python [manage.py](http://manage.py) migrate

migrations의 폴더를 뒤져서 db.sqlite3에 적용시켜 줌

- makemigrations : 앱 내의 migration 폴더를 만들어서 models.py의 변경사항 저장
- migrate : Migration폴더를 실행시켜 데이터베이스에 적용

## Django - CRUD - Read

- views.py에서 함수를 하나 만들 때, 무조건 urls.py에 path가 하나 추가된다고 생각하면 된다.
- 페이지 하나를 만들려면, urls.py에 path를 하나 만들어야 하고, 함수 하나를 만들어야 하고, html 하나를 만들었어야 했다.

## Static

- 정적 파일(Static, media)

Static : 개발자가 서버를 개발할 때 미리 넣어놓은 정적파일(img, js, css)

media : 사용자가 업로드할 수 있는 파일

## media

예컨대 웹을 이용하는 사용자가 사진을 업로드를 하면 업로드한 사진을 웹에 띄울 수 있는 기능을 해보자...

- 원본 파일이 주고받아지는 것이 아니라 url이 주고받아지는 것...

## FORM

입력 공간을 뜻함. (폼태그의 그 폼 맞음...)

폼 태그 안에 인풋태그를 넣어서 클라이언트가 db형식에 맞게 정보를 보낼 수 있도록 해줌. 장고는 이를 forms.py를 통해 객체지향적으로 만들 수 있게 지원해 줬음.

---