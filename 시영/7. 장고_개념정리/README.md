## MVC, MVT
- Model: 안전하게 데이터를 저장
- view: 데이터를 적절하게 유저에게 보여줌
- Control,Template(Django): 사용자의 입력과 이벤트에 반응하여 Model과 View를 업데이트

## Django 개념
- models.py : sql , 데이터베이스 연결
- views.py: 데이터 가공
- urls.py: 정규 표현식에 맞춰 views.py로 보내줌
- forms.py
- settings.py: 전체 프로젝트 관리 및 설정
- admin.py : 관리자 권한을 다룸

- Template: html 파일

## Project와 APP
- 프로젝트 생성
   - django-admin startproject tutorial(이름)
- 의미있는 하나의 Project를 App으로 관리할 수 있음
- 프로젝트 내부에 다수의 App 생성
- App 생성
   - ./manage.py startapp community(앱 이름)


## settings.py
- settings.py: 프로젝트 환경 설정 파일
  

- DEBUG: 디버그 보드 설정
- INSTALLED_APPS: pip로 설치한 앱 또는 본인이 만든 app을 추가
- MIDDLEWARE_CLASSES: request와 response 사이의 주요 기능 레이어(인증,보안)
- TEMPLATES: django template 관련 설정, 실제 뷰(html, 변수)
- DATABASE: 데이터베이스 엔진의 연결 설정
- STATIC_URL: 정적 파일의 URL


## manage.py
- manage.py: 프로젝트 관리 명령어 모음


- 주요 명령어
   - startapp: 앱 생성
   - runserver : 서버 실행
   - createsuperuser: 관리자 생성
   - makemigrations app: app의 모델 변경 사항 체크
   - migrate: 변경 사항을 DB에 반영
   - shell : 쉘을 통해 데이터를 확인
   - collectstatic: static 파일을 한곳에 모음