# <점프 투 장고>

[위키독스](https://wikidocs.net/book/4223)

## 1-04 장고 프로젝트 생성하기

- 장고의 프로젝트는 하나의 웹 사이트라고 생각하면 된다. 즉, 장고 프로젝트를 생성하면 한 개의 웹사이트를 생성하는 것과 같다. 프로젝트 안에는 여러 개의 앱이 존재한다. 이 앱들이 모여 웹 사이트를 구성한다.

---

## 2-01 URL과 뷰

### 앱

- 프로젝트에 기능을 추가하기 위해서 앱을 생성한다.
- django-admin startapp 앱이름

### urls.py

- 장고의 [urls.py](http://urls.py) 파일은 페이지 요청이 발생하면 가장 먼저 호출되는 파일로, URL과 뷰 함수 간의 매핑을 정의한다. 뷰 함수는 [views.py](http://views.py) 파일에 정의된 함수를 말한다.
- URL 매핑을 추가하기 위해서는 아래와 같이 수정해야 한다.

[파일이름: C:\projects\mysite\config\[urls.py](http://urls.py/)]

```python
from django.contrib import admin
from django.urls import path
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', views.index),
]
```

특별한 경우가 아니라면 URL 매핑시 항상 끝에 슬래시를 붙여 주도록 하자. (path의 'pybo/'와 같이!!)

### views.py

- URL 매핑에 추가한 뷰 함수를 추가하자.

[파일이름: c:\projects\mysite\pybo\[views.py](http://views.py/)]

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
```

index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.

### 장고 개발 흐름 정리하기

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c3503990-afdc-46c6-b9d8-695c133c8ebb/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c3503990-afdc-46c6-b9d8-695c133c8ebb/Untitled.png)

브라우저에서 로컬 서버로 [http://localhost:8000/pybo](http://localhost:8000/pybo) 페이지를 요청하면[1] [urls.py](http://urls.py/) 파일에서 /pybo URL 매핑을 확인하여 [views.py](http://views.py/) 파일의 index 함수를 호출하고[2] 호출한 결과를 브라우저에 반영하는[3] 흐름이다.

### URL 분리

- 한 앱에 관련된 것들은 그 앱의 디렉터리 하위에 위치해야 한다. 따라서 pybo앱도 pybo 하위에서 url매핑을 관리하는 것이 좋다.

```python
from django.contrib import admin
from django.urls import path, include
# from pybo import views  # 더 이상 필요하지 않으므로 삭제

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), 
]
```

path('pybo/', include('pybo.urls'))의 의미는 pybo/로 시작하는 페이지를 요청하면 이제 pybo/urls.py 파일의 매핑 정보를 읽어서 처리하라는 의미.

그리고 pybo/urls.py 파일은 다음과 같이 작성하면 된다.

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]
```

---

## 2-02 모델

### models.py

생각한 데이터들을 [models.py](http://models.py) 파일에 저장...

### 파이보 앱 등록

```python
(... 생략 ...)
INSTALLED_APPS = [
    'pybo.apps.PyboConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    (... 생략 ...)
]
(... 생략 ...)
```

### makemigrations

- makemigrations (ex - 모델이 신규로 생성되거나 변경되었을 때 migrate 명령을 수행해주기 위해 필요)

    : 앱 내의 migration 폴더를 만들어서 models.py의 변경사항 저장

    python [manage.py](http://manage.py) makemigrations

    : models.py의 변경사항을 감지해서 migrations에 저장시켜줌

### migrate

- migrate (ex - 실제 테이블 생성)

    : Migration폴더를 실행시켜 데이터베이스에 적용

    python [manage.py](http://manage.py) migrate

    : migrations의 폴더를 뒤져서 db.sqlite3에 적용시켜 줌

### 모델 사용하기 - Question 조회

- 모델에 메서드가 추가될 경우에는 makemigrations와 migrate를 수행할 필요가 없다. migrate 명령이 필요한 경우는 모델의 속성이 변경되었을때 뿐이다.
- get은 반드시 1건의 데이터를 조회할 때 사용한다. 보통 get은 id와 같은 유일한 값으로 조회할 경우에만 사용한다.

---

## 2-03 장고 관리자

### 슈퍼유저

- python [manage.py](http://manage.py) createsuperuser
- 장고 관리자를 사용하기 위해 장고 관리자 화면에 접속할 수 있는 슈퍼유저...

### 모델 관리

- 장고 관리자 화면에서 모델을 관리할 수 있다. 신규 질문을 생성할 수도 있고, 조회, 수정, 삭제도 가능하다.

### 모델 검색

[파일명: C:\projects\mysite\pybo\[admin.py](http://admin.py/)]

```python
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
```

이를 코드와 같이 작성하면 모델 검색 가능... 장고 관리자는 이 외에도 무수한 많은 기능들이 존재한다.

---

## 2-04 조회와 템플릿

### 질문 목록

```python
# from django.http import HttpResponse  # 삭제
from django.shortcuts import render
from .models import Question

def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
```

- 질문 목록 데이터는 Question.objects.order_by('-create_date') 로 얻을 수 있다.
- order_by는 조회 결과를 정렬하는 함수이다. order_by('-create_date')는 작성일시 역순으로 정렬하라는 의미이다.  (`-` 기호가 붙어 있으면 역방향, 없으면 순방향 정렬을 의미한다. )
- render 함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수이다. 즉, 위에서 사용한 render 함수는 question_list 데이터를 pybo/question_list.html 파일에 적용하여 HTML을 리턴한다. 여기서 사용된 pybo/question_list.html과 같은 파일을 템플릿(Template)이라고 부른다. 템플릿 파일은 HTML 파일과 비슷하지만 장고에서 사용하는 태그를 사용할수 있는 HTML 파일이다.

### 템플릿 디렉터리

- 템플릿 파일을 작성하기 전에 템플릿 파일을 저장할 디렉터리를 먼저 만들어야 한다. 템플릿을 저장할 디렉터리는 `config/settings.py` 파일의 TEMPLATES 항목에 추가해야 한다.

- 일반적으로는 `C:\projects\mysite\pybo\templates` 과 같이 많이 지정하는데, 필자는 `C:\projects\mysite\templates\pybo` 의 형식을 권장함. 그리고 공통으로 사용하는 템플릿은 `C:\projects\mysite\templates` 에 저장할 것...
- 왜냐하면 하나의 사이트에서 여러 앱을 사용할 때 여러 앱의 화면을 구성하는 템플릿은 한 디렉터리에 모아 관리하는 편이 여러모로 좋기 때문이다.(템플릿 상속?!...)

### 템플릿 파일

- 템플릿을 보면 {% if question_list %} 처럼 {% 와 %} 로 둘러싸인 문장들을 볼 수 있는데 이러한 것들을 템플릿 태그라고 한다.

### 템플릿 태그 (장고에서 사용되는 3가지 유형)

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

### urls.py

- 어떠한 URL이 동작할 수 있게 하기 위해서는 pybo/urls.py 파일을 수정해 주어야 함.

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
]
```

이제 [http://localhost:8000/pybo/2/](http://localhost:8000/pybo/2/) 페이지가 요청되면 위 매핑 룰에 의해 [http://localhost:8000/pybo/](http://localhost:8000/pybo/)int:question_id/ 가 적용되어 question_id 에 2가 저장되고 views.detail 함수가 실행될 것이다. int:question_id 에서 int는 숫자가 매핑됨을 의미한다.

### 오류 페이지

- 없는 데이터를 클라이언트가 요청할 경우 404페이지를 출력하도록 유도하는 것이 좋음. 이를 위해 detail 함수를 수정해보자.

```python
from django.shortcuts import render, get_object_or_404
from .models import Question

(... 생략 ...)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
```

Question.objects.get(id=question_id)를 get_object_or_404(Question, pk=question_id)로 바꾸어 주었다. 여기서 사용한 pk는 Question 모델의 기본키(Primary Key)인 id를 의미한다.

(오류 코드 추가 찾아보기!...)

---

## 2-05 URL과 네임스페이스

### URL 별칭

- 링크의 주소 대신 별칭을 사용하려면 URL 매핑에 name 속성을 부여해야 한다.

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
]
```

### 템플릿에서 URL 별칭 사용하기

```python
{% if question_list %}
    <ul>
    {% for question in question_list %}
        <li><a href="{% url 'detail' question.id %}">{{ question.subject }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>질문이 없습니다.</p>
{% endif %}
```

하드코딩 되어 있던 /pybo/{{ [question.id](http://question.id/) }} 링크가 {% url 'detail' [question.id](http://question.id/) %}로 변경되었다. 여기서 question.id는 URL 매핑에 정의된 int:question_id에 전달해야 하는 값을 의미한다.

### URL 네임스페이스

- 여러 개의 앱이 프로젝트에 추가될 경우, 만약 서로 다른 앱에서 동일한 URL 별칭을 사용하면 중복이 발생할 수 있음. 따라서 [urls.py](http://urls.py) 파일에 네임스페이스를 의미하는 app_name 변수를 지정해 주어야 함.

```python
from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
]
```

이 다음, 템플릿에서 사용한 URL 별칭에 아래와 같이 지정해 준다.

```python
{% if question_list %}
    <ul>
    {% for question in question_list %}
        <li><a href="{% url 'pybo:detail' question.id %}">{{ question.subject }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>질문이 없습니다.</p>
{% endif %}
```

detail 앞에 pybo 라는 네임스페이스를 붙여준 것!