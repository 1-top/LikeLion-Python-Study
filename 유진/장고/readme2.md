# 장고 기본 요소 익히기

(점프 투 장고 2장)

### 앱
프로젝트에 기능을 추가하기 위한 앱(게시판 기능, 로그인 기능 ...)

1. 앱 생성
>django-admin startapp (앱이름)

2. url.py에 페이지 매핑

url.py 파일은 페이지 요청이 발생하면 가장 먼저 호출됨.

url과 뷰 함수(views.py 파일)간의 매핑을 정의함.

### url.py

url 매핑을 추가하기 위해 url.py 수정.
```python
from django.contrib import admin
from django.urls import path
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', views.index),
]
```
url이 요청되면, views.index를 호출하라는 매핑을 urlpatterns에 추가함.

주소 맨 뒤 / 슬래쉬를 붙이면 자동으로 끝에 / 슬래쉬가 붙도록 변환됨. url을 정규화하는 장고의 기능.

### views.py

url 매핑 후 뷰 함수 추가.

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
```

리턴값은 요청 페이지에 대한 응답을 할 때 사용하는 장고 클래스. 여기선 문자열을 출력하기 위해 사용됨.

`request`는 장고에 의해 자동으로 전달되는 http 요청 객체

### 정리

1. 브라우저에서 로컬 서버로 페이지 요청
2. urls.py에서 url 매핑 확인하여
3. views.py 파일에 함수 호출
4. 결과 브라우저에 반영

### + URL 분리

프로젝트 하위에 urls.py 파일에는 프로젝트 성격의 url 매핑만 추가하는 것이 좋음.

따라서 프로젝트와 앱 url 분리를 위해

다음과 같이 url 파일 정리

1. include

```python
from django.urls import include

urlpatterns = [
    path('/', include('app.urls')),
]
```

url 매핑을 `path('/', views.함수)`에서 `path('/', include('~.urls'))`로 수정.

`path('/', include('~.urls'))`의 의미는 `/`로 시작하는 페이지를 요청하면 `~.urls.py` 파일의 매핑 정보를 읽어 처리하라는 의미.

따라서 ~/urls.py (앱 내의 url) 파일을 수정함으로써 url 추가 가능.

2. 앱에 urls.py 생성

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]
```

프로젝트 url 파일에서 `~/`으로 시작하는 url이 먼저 매핑 됐음으로 첫번째 url은 ''으로.


## 모델

장고는 모델을 이용하여 db를 처리한다.

데이터를 저장하고 조회하기 위해선 sql 쿼리문을 이용해야 하지만 장고의 모델을 사용하면 sql문 없이 데이터를 처리할 수 있다.

__1. 앱 migrate__

>You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.

런서버를 실행하면 중간에 다음과 같은 문구가 뜬다.

18개의 적용되지 않은 migration들이 있다. 그게 먼지도 보여줌.

데이터베이스가 필요한 앱은 migration이 필요하다.

* settings.py 에 databases

데이터베이스 엔진, base_dir(프로젝트 디렉터리, 저장되는 파일)에 대한 정보가 나와 있음.

* python manage.py migrate

실행하면 migrate가 필요한 앱들의 테이블이 생성됨.

(어떤 테이블이 만들어지는지 궁금하면: DB Browser for SQLite)

__2. 모델 작성하기__
* models.py

models.py 파일에 모델 정의

(예시)
```python
from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
```
기존 모델을 속성으로 연결하려면 `ForeignKey` 사용

`on_delete=models.CASCADE`의 의미는 이 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제된다는 의미

그 외 필드 확인: https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types

__3. 테이블 생성__

작성한 모델을 이용하여 테이블 생성.
* settings.py에 앱 추가

```python
INSTALLED_APPS = [
    'pybo.apps.PyboConfig',
```

`앱이름.apps.앱이름Config` 클래스는 앱 생성시 자동으로 만들어지는 파일, 클래스.

* makemigrations

> python manage.py makemigrations

모델을 생성하거나 모델에 변화가 있을 경우 실행하는 명령어.

앱\migrations\0001_initial.py 파일이 자동으로 생성됨.

장고가 테이블 작업을 수행하기 위한 작업파일을 생성하는 명령어.

> (mysite) c:\projects\mysite>python manage.py sqlmigrate pybo 0001
> 
> 이 명령어(sqlmigrate)로 실제 어떤 쿼리문이 실행되는지 확인 가능.
> 
> 쿼리문을 수행하진 않음.

* migrate

> python manage.py migrate

테이블 생성

__4. 모델 사용하기__

* 장고 셸
>(mysite) c:\projects\mysite>python manage.py shell

* question 데이터 생성
> from django.utils import timezone
>
> q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=timezone.now())
>
> q.save()

위와 같이 데이터를 생성하면 id 값이 생성됨.

> q.id
> (결과값) 1

* question 데이터 조회

> Question.objects.all()
>
> <QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>

`question.objects`를 통해 데이터 조회 가능.

`.objects.all()`은 모든 데이터를 조회하는 함수.

위의 경우 id값을 보여줌

```python
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
```

`__str__` 메서드를 모델에 추가함으로 __id값 대신 제목__ 표시 가능.

__+ 필터 사용 조회__
> Question.objects.filter(id=1)

조건 걸어 (여러개) 리턴
> Question.objects.get(id=1)

get은 하나만 리턴해줌

>Question.objects.filter(subject__contains='장고')

subject에 장고 가 포함된 데이터만 조회


* 데이터 수정

> q.subject = 'Django Model Question'
> 
> q.save()

save()를 해야 저장됨

* 데이터 삭제

> q = Question.objects.get(id=1)
>
> q.delete()


## 관리자

1. 슈퍼유저

장고 관리자를 사용하기 위해 관리자 화면에 접속할 수 있는 슈퍼유저를 생성해야 됨.

> python manage.py createsuperuser

실행 후 이름 주소 비밀번호 설정

2. 장고 관리자 화면

주소/admin/ 페이지 접속

3. admin.py에 모델 등록

```python
from .models import 테이블

admin.site.register(테이블)
```

모델을 등록한 후 관리자 화면을 보면 테이블이 추가됨을 확인할 수 있다.

__+ 검색기능__
```python
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
```

위와 같이 admin 파일 수정하면 관리자 화면에 기능이 추가됨.

__++ 그외 관리자 기능__
https://docs.djangoproject.com/en/3.0/ref/contrib/admin/



