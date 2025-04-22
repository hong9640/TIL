# Javascript
## ECMAScript
- 스크립트 언어가 준수해야 하는 규칙, 세부사항 등을 제공
- 자바 스크립트는 ecmascript 표준을 구현한 프로그래밍 언어로 웹 브라우저는 node.js와 같은 환경에서 실행됨
- 2015년 ES6에서 많은 발전을 이룸
- 자바스크림트는 현재 서버 사이드 개발에도 사용되기 시작됐다.
## 변수 작성 규칙
- 반드시 문자, 달러('$') 또는 밑줄('_')로 시작
- 대소문자 구분
- 예약어 사용 불가: for, if, function 등
- 식별자 Naming case  
  - 카멜 케이스: 변수, 객체, 함수에 사용
  - 파스칼 케이스: 클래스, 생성자에 사용
  - 대문자 스네이크 케이스: 상수에 사용
## 변수 선언 키워드
- let, const
- let: 블록 스코프를 갖는 지역 변수를 선언  
  - 재할당 가능  
    - let number = 10, number = 20 이렇게 재할당은 가능
  - 재선언 불가능  
    - let number = 10으로 하면 let number = 20 이렇게 안된다. 파이썬하고 다름.
  - ES6에서 추가
- const: 블록 스코프를 갖는 지역 변수를 선언  
  - 재할당 불가능
  - 재선언 불가능 
  - ES6에서 추가
- 블록스코프  
  - if, for 함수 등의 '중괄호 내부를 가리킴'
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
- 기본적으로 const를 기본으로 사용한다.
- 필요한 경우에만 let으로 전환.  
  - 재할당이 필요한 경우
  - let을 사용하는 것은 해당 변수가 의도적으로 변경될 수 있음을 명확히 나타냄.
- const를 기본으로 사용해야 하는 이유  
  - 코드의 의도 명확화  
    - 개발자들에게 변수의 용도와 동작을 더 쉽게 이해할 수 있게 해줌.
    - 해당 변수가 재할당되지 않을 것임을 명확히 표현
  - 버그 예방  
    - 의도치 않은 변수 값 변경으로 인한 버그를 예방
    - 큰 규모의 프로젝트나 팀 작업에서 중요.
## DOM
- 자바스크립트 실행 환경 종류:  
  - HTML script 태그
  - js 확장자 파일
  - 브라우저 Console
- 브라우저 문서를 표현하기 위해 데이터 구조가 나눠져 있는데 각 상자는 객체이고 개발자는 이 객체와 상호작용하여 어떤 콘텐츠가 포함되어 있는지, 어떤 html 태그를 나타내는지 알아낼 수 있다.
- 이 표현을 DOM이라고 한다.
- DOM은 웹 페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공하는데 문서 구조, 스타일 , 내용 등을 변경할 수 있도록 한다.
- DOM API 다른 프로그래밍 언어가 웹 페이지에 접근 및 조작할 수 있도록 페이지 요소들을 객체 형태로 제공하며 이에 따른 메서드 또한 제공
### document
- document 객체:  
  - 웹 페이지를 나타내는 DOM트리의 최상위 객체
- DOM tree:  
  - html 태그를 나타내는 elements의 노드는 문서의 구조를 결정한다.
  - 이들은 다시 자식 노드를 가질 수 있는데 이 트리 구조를 DOM tree 라고 한다.
- DOM 핵심:  
  - 문서의 태그를 객체로 본다고 이해하면 된다.
  - 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 방법을 제공하는 API 
- DOM 조작 시 조작하고자 하는 요소를 선택해야 하고 선택된 요소의 콘텐츠 또는 속성을 조작해야 한다.
- 선택 메서드:  
  - querySelector:요소 한개 선택  
    - 제공한 선택자와 일치하는 element 한 개 선택
    - 제공하는 선택자를 만족하는 첫 번째 element 객체를 반환
  - querySelectorAll: 요소 여러 개 선택  
    - 제공한 선택자와  일치하는 여러 element를 선택
    - 제공한 선택자를 만족하는 Nodelist를 반환
## DOM 조작
- 속성 조작:  
  - 클래스 속성 조작:  
    - element.classList.add()  
      - 지정한 클래스 값을 추가
    - element.classList.remove()  
      - 지정한 클래스 값을 제거
    - element.classList.toggle()  
      - 클래스가 존재한다면 제거하고 false를 반환
- const h1Tag = document.querySelector('.heading')  
  console.log(h1Tag.classList)

- h1Tag.classList.add('red')  
  console.log(h1Tag.classList)
- 위와 같은 형식으로 만들어진다.
  
- 일반 속성 조작 메서드  
  - Element.getAttribute()  
    - 해당 요소에 지정된 값을 반환
  - Element.setAttribute(name. value)  
    - 지정된 요소의 속성 값을 설정
    - 속성이 이미 있으면 기존 값을 갱신
  - Element.removeAttribute()  
    - 요소에서 지정된 이름을 가진 속성 제거

- html 콘텐츠 조작  
  - textContent: 요소의 텍스트 콘텐츠를 표현
- const h1Tag = document.querySelector('.heading')  
  console.log(h1Tag.textContent)

- h1Tag.textContent = '내용 수정'  
  console.log(h1Tag.textContent)
위와 같은 형식으로 된다.

- DOM 요소 조작 메서드  
  - document.createElement(tagname):  
    - 작성한 tagname의 html요소를 생성하여 반환
  - Node.appendChild():  
    - 한 노드를 특정 부모 노드의 자식 노드리스트 중 마지막 자식으로 삽입
    - 추가된 노드 객체를 반환
  - Node.removeChild():  
    - DOM에서 자식 node를 제거
    - 제거된 node를 반환
- style 조작  
  - 해당 요소의 모든 style 속성 목록을 포함하는 속성
  - const pTag = document.querySelector('p')  
  - pTag.style.color = 'crimson'
## 데이터타입
- 원시자료형: 변수에 값이 지정 저장되는 자료형(불변, 값이 복사)
  - number: 정수 또는 실수형 숫자를 표현
  - string: 텍스트 데이터를 표현, 더하기만 가능하다! 나머지 불가능!  
    - 사용방법: backtick('')을 이용하고 표현식은 '$'과 중괄호로 표기
    - const message = '홍길동은 ${age}세 입니다.'
  - null: 값이 없음 나타냄, 의도적으로 값이 없음을 나타냄
  - undefined : 값이 할당되지 않음.
  - Boolean: boolean이 아닌 데이터 타입이 자동 형변환 규칙에 따라 true 또는 false로 변환됨(소문자!)
- 참조자료형: 객체의 주소가 저장되는 자료형(가변, 주소가 복사)
## 연산자
- 할당 연산자 :  
  - 오른쪽에 있는 피연산자읜 결과를 왼쪽 피연산자에 할당
  - 단축 연산자 지원
- 증가 연사자('++'): 피연산자를 증가시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환.
- 감소 연산자('--')
- +=나 -+쓰는 것을 추천
- 비교연산자
- 동등연산자(==): 특별한 경우 아니면 안씀
- 일치 연산자(===) : 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
- console.log(0 === false) 이건 false다! 두 값이 하나는 number이고 하나는 Boolean이어서 서로 다름!
- 논리연산자  
  - and연산: &&
  - or연산: ||
  - not 연산:
  - !
  - 단축 평가 지원
## 조건문
- 결과값을 boolean타입으로 변환 후 참/거짓 판단
### 반복문
- while
- for  
  - for (let i = 0; i<6; i++) { console. log(i):} 0부터 5까지
- for in: for (variable in object) {statement} 객체의 열거 가능한 속성에 대해 반복, 딕셔너리, 리스트 전부 가능
- for of: 반복 가능한 객체에 대해 반복, for (variable of iterable) {statement}, 딕셔너리 쓰려고 하면 오류, 리스트 써야 함
- for in은 순서가 보장이 안된다. 그래서 순서가 중요한 배열에서는 사용하지 않는다. 객체 전용
- 배열, 문자열 등 에서는 for이나 for of문을 사용한다.
- 만약 [a, b, c]이렇게 있을 경우 for in을 쓰면 0,1,2가 나오고 for of를 쓰면 a, b, c가 나온다.
- for문에서는 let만 써야 한다. i를 재할당 하면서 사용하기에 const를 사용하면 에러 발생한다.
- for in, for of의 경우 const를 사용해도 에러가 발생하지 않는다. 단, conts 특징에 따라 블록 내부에서 변수 수정 불가능
## 함수
- Function
- 'function add(num1, num2) {
      return num1 + num2
    }' (선언식)
- 위와 같이 구조를 가진다. 만약 return이 없다면 undefined를 반환
- 정의 방법은 2가지:  
  - 선언식
  - 표현식
- 'const sub = function (num1, num2) {
      return num1 - num2
    }' (표현식)
- 선언식 장점: 호이스팅 됨, 코드의 구조오 가독성 면에서는 표현식에 비해 좋다.
- 표현식 특장: 변수선언만 호이스팅 되고 함수 할당은 실행 시점에 이루어진다.
- 함수 이름이 없는 익명 함수를 사용할 수 있음.
## 매개변수
- 기본함수 매개변수 : Anonymous
- 나머지 매개변수: 임의의 수의 인자를 배열로 허용하여 가변 인자를 나타내는 방법
- funtion ( parma1, param2, ...resPrams) return[param1, param2, restPrams]
- 만약 매개변수의 개수가 인자 개수보다 만으면 누락된 인자는 undefined로 할당된다.
- 인자개수가 더 많을 경우 초과 입력한 인자는 사용하지 않는다.
## 화살표 함수 표현식
- 위의 표현식을 화살표 함수로 바꾸면 const sub = (num1, num2) => {return num1 - num2}
- 소괄호는 매개변수가 1개일 때문 가능하다. 그래서 생략하지 않는 것을 권장한다. 또한 표현식 ㅣ한줄이라면 중괄호와 return을 제거할 수 있다. 일단은 중괄호와 return을 함께 쓰는것 추천