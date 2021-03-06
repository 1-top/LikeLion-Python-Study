02-1 숫자형

- ** 은 x**y처럼 사용했을 때 x의 y제곱값을 돌려줌.
- '/' 연산자는 소수점을 잘 반환해줌. es) 7/4 ⇒ 1.75반환  '//' 연산자를 사용해야 나눗셈 후 몫을 반환하게 됨.

02-2 문자열 자료형

- 문자열 연산. 파이썬에서는 문자열을 더하거나 곱할 수 있음. 수를 더하듯이 활용가능...

    ex) head + tail = headtail의 형태 / a * 2 = aa의 형태

- 문자열 인덱싱

첫번째 문자를 a[0]으로 기준삼아, a[양수] 또는 a[음수]로 문자열을 인덱싱하여 활용할 수 있다.

- 문자열 슬라이싱

문자열 슬라이싱에서 주의해야 할 점은 a[0:4]는 a[0] ~ a[3]까지 해당한다는 것이다. 즉, : 의 뒤에 위치한 수는 포함되지 않는다!

더불어, a[:17] == 처음부터 16번째까지를 의미. a[19:] 19번째부터 끝까지를 의미. a[19:-7] a[19]부터 a[-8]까지를 의미. 와 같은 형식으로도 사용할 수 있다.

02-3 리스트 자료형

- del a[x]는 x번재 요솟값을 삭제한다. 참고로 del 함수는 파이썬이 자체적으로 가지는 삭제 함수이다. ( del 객체 )
- .append는 덧붙이는 함수

ex) a.append(4) ⇒ 원래 a 리스트에 '4'가 덧붙여진다.

- .sort()는 리스트의 요소를 순서대로 정렬 / .reverse()는 리스트를 역순으로 뒤집어 줌. (역순으로 정렬해주는 것은 아니라 그냥 거꾸로 뒤집어주기만...)
- .index(x)는 리스트에 x 값이 있으면 x의 위치 값을 돌려줌
- .insert(a,b)는 리스트의 a번째 위치에 b를 삽입하는 함수 / remove(x)는 리스트에서 첫번째로 나오는 x를 삭제하는 함수
- .pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제
- .extend(x)는 리스트 확장. 여기서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더해줌

02-4 튜플 자료형

- 리스트는 [ ]로 둘러싸는 형태지만, 튜플은 ( )로 둘러싼다.
- 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다. 가장 큰 차이점은, 값을 변화시킬 수 있는가?이다. (튜플의 항목 값은 변화 불가능) / 실제 프로그램들 에서는 값이 변화되는 요구사항이 많기에 리스트가 자연스레 많이 활용됨

02-5 딕셔너리 자료형

- 딕셔너리는 대응 관계를 나타낼 수 있는 자료형.

    ex) dic = {'name' : 'pey'}

- 딕셔너리 요소도 del 함수를 이용해 지울 수 있음.

    ex) del a[key]

- 딕셔너리는 특정한 요솟값을 얻고자 할 때 key를 이용해서 value를 구할 수 있음. 튜플이나 리스트와 같이 인덱싱, 슬라이싱 활용 불가능

    ex) 딕셔너리변수명[key]

- 딕셔너리에서 key는 고유한 값이므로 중복되는 key값을 설정해 놓으면 하나를 제외한 나머지 것들은 모두 무시됨

02-6 집합 자료형

- 집합(set) / s1 = set([1,2,3])
- 집합 자료형은 중복을 허용하지 않고, 순서가 없다. 따라서 'Hello'라는 문자열을 집합 자료형으로 넣으면, l은 한개만 도출되고 순서는 뒤죽박죽이 된다.
- 교집합 ⇒ & / 합집합 | / 차집합 -

02-7 불 자료형

- 불(bool) 자료형이란 참과 거짓을 나타내는 자료형. 불리언...

02-8 자료형의 값을 저장하는 공간, 변수

- 변수가 가리키는 메모리 주소는 id()로 확인할 수 있음
- 일반적으로 '='를 사용하면 같은 객체를 참조하게 되는데, 다른 객체를 참조하게끔 만들기 위해서는 1) [:] 이용 2) copy 모듈 이용