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
  - 선언식 - 선언식 위주로 쓰자.
  - 표현식
- 'const sub = function (num1, num2) {
      return num1 - num2
    }' (표현식)
- 선언식 장점: 호이스팅 됨, 코드의 구조와 가독성 면에서는 표현식에 비해 좋다.
- 표현식 특장: 변수선언만 호이스팅 되고 함수 할당은 실행 시점에 이루어진다.
- 함수 이름이 없는 익명 함수를 사용할 수 있음.
- 호이스팅: 선언을 끌어올린다.
## 매개변수
- 기본함수 매개변수 : Anonymous
- 나머지 매개변수: 임의의 수의 인자를 배열로 허용하여 가변 인자를 나타내는 방법
- funtion ( parma1, param2, ...resPrams) return[param1, param2, restPrams]
- 만약 매개변수의 개수가 인자 개수보다 만으면 누락된 인자는 undefined로 할당된다.
- 인자개수가 더 많을 경우 초과 입력한 인자는 사용하지 않는다.
## 화살표 함수 표현식
- 위의 표현식을 화살표 함수로 바꾸면 const sub = (num1, num2) => {return num1 - num2}
- 소괄호는 매개변수가 1개일 때문 가능하다. 그래서 생략하지 않는 것을 권장한다. 또한 표현식 ㅣ한줄이라면 중괄호와 return을 제거할 수 있다. 일단은 중괄호와 return을 함께 쓰는것 추천

## 객체
- const user = { name: 'Alice', greeting:function() { return 'hello}} 이런 형식으로 작성한다.
- key는 문자형만, value는 모든 자료형 허용
- // 조회: console.log(user.name) => Alice
- // 추가: user.address = 'korea', console.log(user) => // {name: 'Alice', key with space: true, address: 'korea', greeting: ƒ}
- // 수정: user.name = 'Bella', console.log(user.name)
-  // 삭제: delete user.name, console.log(user)
-  in 연산자는 속성이 객체이 존재하는지 여부를 확인한다. 
- // in 연산자: console.log('greeting' in user) // true
- // 메서드 호출: console.log(user.greeting()) // hello
### this 키워드
- this 키워드: return `Hello my name is ${this.name}`
- 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용한다. 
- 위의 객체 예시에서 return에 위와 같이 this를 쓴다.
- 이때 name은 그냥 객체의 프로퍼티로 객체가 아니기에 this.name 이렇게 써야 한다.
- console.log(person.greeting()) // Hello my name is Alice
- 단순호출 => 가리키는 대상은 전역 객체로 window가 나오게 된다.
- 메서드를 호출하게 되면 예를 들어 console.log(myObj.myFunc()) myObj: 객체명, myFunc(): 함수 명 이런식으로 하면 가리키는 대상은 메서드를 호출한 객체로 console.log(myObj.myFunc()) // myObj 이와 같은 결과가 나온다.
- forEach 인자로 작성된 함수는 일반적인 함수 호출이어서 this가 전역 객체를 가리키지만 화살표 함수는 자신만의 this를 가지지 않기에 외부 함수에서 this값을 가져온다.
### 추가 객체 문법
- 키 이름과 값으로 쓰이는 변수의 이름이 같으면 단축 구문 사용 가능
- 메서드 선언 시 function 키워드 생략 가능
- 계산된 속성 : 키가 대괄호로 둘러싸여 있는 속성, 고정된 값이 아닌 변수 값을 사용할 수 있음
- 구조 분해 할당: 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당할 수 있는 문법
- 전개구문: 객체복사, 얕은 복사에서 활용 가능
- ...obj 이런 식으로 쓴다.
- const obj = { b: 2, c: 3, d: 4 }, const newObj = { a: 1, ...obj, e: 5 }, console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
- optional changing: console.log(user.address?.street) // undefined
- 위와 같이 쓰며 address가 없을 시 ? 를 붙이면 평가를 멈추고 undefined을 반환한다.
- 만약 optional changing을 안쓰면 console.log(user.address && user.address.street) 이런 식으로 해야 한다.
- 존재하지 않아도 괜찮은 대상에만 사용해야 하며 남용하면 안된다.
### json
- 형식이 있는 문자열
## Array
- 대괄호를 이용해 작성해야 한다.
- 주요 메서드:  
  - push / pop -> 뒤에
  - unshift / shift -> 앞에
- Array Helper Methods:  
  - 배열의 각 요소를 순회하며 각 요소에 대한 함수(콜백함수)fmf ghcnf
  - 대표 메서드: forEach(), map(), filter(), every(), some(), reduce()등
  - 메서드 호출 시 인자로 함수(콜백함수)를 받는 것이 특징
- 콜백 함수: 다른 함수에 인자로 전달되는 함수
- 함수는 동작이다.
- 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행
- forEach = 반환 값 없음, 배열 내의 모든 요소 각각에 대해 함수를 호출
- map = 배열 내의 모든 요소 각각에 대해 함수를 호출, 함수 호출 결과를 모아 새로운 배열을 반환
- map(함수, )
- 콜백 함수는 결국 재사용성이 좋다.
- 함수 호출 결과를 모아 새로운 배열을 반환
- 만약 내 코드에 this가 있다면 화살표 함수에서 결과가 달라진다. 그래서 올바른 코드를 작성해야 한다.
## map 함수
- arr.map(callback(itme[, index[, array]]))

## 배열 순회 조합
1. for lop
2. for of
3. forEach - 단순 반복, 기존 for문
4. map - 새로운 값을 반환

## class 필요성
- 객체를 하나 생성하고 또 같은 객체를 만들면 너무 불편함. 그래서 설계도를 만든다.
- class 키워드, 클래스 이름, 생성자 메서드 ex) constructor()
- class Member { constructor(a, b) { this.a = a this.b = b} // 메서드 sayHi() {console.log(`${this.a}`)}}
- 위의 형식처럼 만들면 된다.

## 이벤트
- 화면 스크롤 하는 것 
- 버튼을 클릭했을 때 팝업 창이 출력되는 것
- 마우스 커서의 위치에 따라 드래그 앤 드롭 하는 것
- 사용자의 키보드 입력 값에 따라 새로운 요소를 생성하는 것
- 웹에서 모든 동작은 이벤트 발생과 함께 한다.
- 이벤트는 웹 페이지 상에서 무언가 일어났다는 신호 또는 사건을 말하는데 사용자가 버튼을 클릭하거나 키보드를 누르는 등을 전부 이벤트라 한다.
### event object
- DOM에서 이벤트가 발생하면 해당 이벤트에 관한 정보를 담은 event object를 자동으로 생성
- 이벤트 객체는 이벤트 발생 순간의 상황과 관련된 상세 정보를 담고 있음
- 이를 통해 이벤트와 관련된 구체적인 정보를 참조할 수 있음.
### event handler
- 특정 이벤트가 발생했을 때 실행되는 (콜백)함수
- .addEventListener(): 이벤트 핸들러를 DOM요소에 연결하는 역할을 담당
- button.addEventListener('click', handleClick)
- DOM요소(이벤트가 발생하는 대상).addEventListener(수신할 이벤트, 핸들러)
- 핸들러는 함수이다.
## 버블링
- 한 요소에 이벤트가 발생하면 이 요소에 할당된 핸들러가 동작하고 이어서 부모 요소의 핸들러가 동작하는 현상
- currentTarget 속성:  
  - 현재 요소
  - 항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성
  - 핸들러가 연결된 outerouter요소만을 가리킴
  - this와 같음
- target 속성:  
  - 실제 이벤트가 시작된 요소
  - 버블링이 진행되어도 변하지 않음.
  - 실제 이벤트가 발생하는 요소를 가리킴
- 버블링은 각자 다른 동작을 수행하는 버튼을 하나만 할당하면 이 모든 이벤트를 한번에 다룰 수 있게 된다.
- 그래서 버블링이 필요하다.
- .preventDefault(): 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정
- 이벤트 작성 순서:  
  - 1. 버튼 요소 선택
  - 2. 이벤트 핸들러 생성
  - 3. 버튼에 이벤트 핸들러를 등록
## 비동기
- 동기: 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식
- 지금까지의 코드는 모두 동기 였었다.
- 비동기(Asynchronous): 작업의 완료 여부를 신경쓰지 않고 동시에 다른 작업들을 수행할 수 있음.  
  - gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 장업은 병렬적으로 별도로 처리됨
  - 병렬적 수행
  - 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 백그라운드에서 실행되며 **빨리 완료되는 작업**부터 처리
- 자바스크립트는 한번에 여러 일 수행 불가. 무조건 동기로 처리할 수 밖에 없는데 어떻게 비동기 처리를 할 수 있을까?
- 바로 비동기 처리를 할 수 있도록 도와주는 환경이 필요하다.
- 자바 스크립트 엔진의 Call Stack, Web API, Task Queue, Event Loop가 비동기 처리 관련 요소이다.
- 브라우저 환경에서 자밧크립트 비동기 처리 동작 방식은 다음과 같다.  
  - 모든 작업은 call stack으로 들어간 후 처리된다
  - 오리 걸리는 작업이 call stack으로 들어오면 web api로 보내 별도로 처리하도록 한다.
  - web api에서 처리가 끝난 작업들을 곧바로 Call Stack으로 들어가지 못하고 Task Queue에 순서대로 들어간다.
  - Evenvt Loop가 call stack이 비어 있는 것을 계속 체크하고 call Stack이 빈다면 Task Queue에서 가장 오래된 작업을 Call stack을 보낸다.
## Ajax
- 비동기적인 웹 애플리케이션 개발을 위한 기술
- 목적:  
  - 비동기 통신
  - 부분 업데이트
  - 서버 부하 감소
- XHR(XMLHttpRequest)객체: 웹 브라우저와 서버 간의 비동기 통신을 가능하게 하는 자바 스크립트 객체
- XHR 주요 기능: 웹 페이지의 전체 새로고침 없이도 서버로부터 데이터를 가져오거나 보낼 수 있음
- 이름에 XML이라는 데이터타입이 들어가긴 하지만 모든 종류의 데이터를 가져올 수 있음.
- 기존 방식이 서버에서 html로 응답을 한다면 Ajax는 json으로 응답한다.
- 이벤트 핸들러는 비동기 프로그래밍의 한 형태이다.
### Axios
- 클라이언트 및 서버 사이에 http요청을 만들고 응답을 처리하는데 사용되는 자바스크립트 라이브러리
- 브라우저를 위한 XHR 객체 생성
- 간편한 API를 제공하며, Promise기반의 비동기 요청을 처리
- 주로 웹 애플리케이션에서 서버와 통신할 때 사용
- XHR 객체 생성 및 요청 -> 응답 데이터 생성 -> JSON데이터 응답 -> Promise 객체 데이터를 활용해 DOM 조작
- 설치 및 사용:  
  - CDN 방식으로 사용하기
  - https://axios-http.com/
  - <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script> 이거 사용하기.
- then() : 작업이 성공적으로 완료되었을 때 실행될 콜백 함수를 지정
- catch() : 작업이 실패했을 때 실행될 콜백 함수를 지정
 ### Callback과 Promise
 - 비동기 처리의 특성:  
   - 비동기 처리의 핵심은 작업이 완료되는 순서에 따라 처리된다는 것
 - 비동기 처리의 어려움:  
   - 개발자 입장에서 코드의 실행 순서가 불명확하다는 단점 존재
 - 비동기 콜백, Promise
 - 비동기 콜백:  
   - 비동기적으로 처리되는 작업이 완료되었을 때 실행되는 함수
   - 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
   - 작업의 순서와 동작을 제어하거나 결과를 처리하는데 사용
 - 한계:  
   - 어떤 기틍의 실행 결과를 받아서 다른 기능을 수행하기 위해 많이 사용되는데 이 과정을 작성하다 보면 비슷한 패턴이 계속 발생한다.
   - 즉, 콜백 지옥이 발생하게 된다.
   - 그래서 콜백 함수를 정리해야 한다.
- Promise
- 자바스크립트에서 비동기 작업의 결과를 나타내는 객체
- 콜백 지옥 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체