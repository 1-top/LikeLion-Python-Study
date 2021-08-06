* 공부할 것


foreignkey

앱 등록시 '앱이름' vs '앱이름.apps.앱이름(첫대문자)Config' 차이

모델 메서드를 수정했을 땐 migrate 필요 없음.
(속성이 변경됐을 때만)

모듈 import 규칙

뷰함수 이해
render 함수

    return render(req, 'detail.html', context)

매직메소드

탬플릿태그해석
```html
question_list.html에 사용된 템플릿 태그들을 하나씩 살펴보자.

{% if question_list %}는 다음처럼 해석된다.

question_list가 있다면 (question_list는 render 함수로 전달받은 "질문 목록" 데이터이다.)

{% for question in question_list %}는 다음처럼 해석된다.

question_list를 반복하며 순차적으로 하나씩 question에 대입

{{ question.id }} 는 다음처럼 해석된다.

for문에 의해 대입된 question 객체의 id 번호를 출력

{{ question.subject }} 는 다음처럼 해석된다.

for문에 의해 대입된 question 객체의 제목을 출력

파이썬에 익숙하다면 여기에 사용된 태그들이 직관적으로 무엇을 의미하는지 쉽게 유추해 낼 수 있을 것이다.
```

url 작성 규칙
```html
이제 http://localhost:8000/pybo/2/ 페이지가 요청되면 위 매핑 룰에 의해 http://localhost:8000/pybo/<int:question_id>/ 가 적용되어 question_id 에 2가 저장되고 views.detail 함수가 실행될 것이다. <int:question_id> 에서 int는 숫자가 매핑됨을 의미한다.
```

204 오류 페이지 수정 부분

* 한 거 정리
1. 가상환경생성
2. 프로젝트 생성
3. 앱생성 및 등록
4. 모델 작성, makemigrations, migrate, 등록
5. 관리자

