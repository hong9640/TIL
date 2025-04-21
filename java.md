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