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

# <점프 투 장고>

## 2-02 모델

### Question 조회

- 모델에 메서드가 추가될 경우에는 makemigrations와 migrate를 수행할 필요가 없다. migrate 명령이 필요한 경우는 모델의 속성이 변경되었을때 뿐이다.
- get은 반드시 1건의 데이터를 조회할 때 사용한다. 보통 get은 id와 같은 유일한 값으로 조회할 경우에만 사용한다.

## 2-04 조회와 템플릿

### 템플릿 디렉터리

- 일반적으로는 `C:\projects\mysite\pybo\templates` 과 같이 많이 지정하는데, 필자는 `C:\projects\mysite\templates\pybo` 의 형식을 권장함. 그리고 공통으로 사용하는 템플릿은 `C:\projects\mysite\templates` 에 저장할 것...
- 왜냐하면 하나의 사이트에서 여러 앱을 사용할 때 여러 앱의 화면을 구성하는 템플릿은 한 디렉터리에 모아 관리하는 편이 여러모로 좋기 때문이다. 예를 들어 여러 앱이 공통으로 사용하는 공통 템플릿을 어디에 저장해야 할지 생각해 보면 왜 이런 방법을 선호하는지 쉽게 이해될 것이다.

### 템플릿 태그

1. 분기

```java
{% if 조건문1 %}
    <p>조건문1에 해당되는 경우</p>
{% elif 조건문2 %}
    <p>조건문2에 해당되는 경우</p>
{% else %}
    <p>조건문1, 2에 모두 해당되지 않는 경우</p>
{% endif %}
```

파이썬의 if 문과 다를바가 없다. 다만 항상 {% endif %} 태그로 닫아주어야 한다는 점을 잊지 말자.

1. 반복

```java
{% for item in list %}
    <p>순서: {{ forloop.counter }} </p>
    <p>{{ item }}</p>
{% endfor %}
```

이 역시 파이썬의 for 문과 다를게 없다. 역시 마지막은 항상 {% endfor %} 태그로 닫아주어야 한다.

1. 객체 출력

```python
{{ 객체 }}
# 객체를 출력하기 위한 태그의 사용법은 다음과 같다.

{{ 객체.속성 }}
# 객체에 속성이 있는 경우는 파이썬과 동일한 방법으로 도트(.) 문자를 이용하여 표시하면 된다.
```