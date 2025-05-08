# VUE
## Frontend Development
- 웹사이트와 웹 애플리케이션의 사용자 인터페이스(UI)와 사용자 경험(UX)을 만들고 디자인 하는 것
## Client-side frmeworks
- 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 자바스크립트 기반 프레임워크
- 이것이 필요한 이유:  
  - 웹에서 하는 일이 많아졌다.
  - 다루는 데이터가 많아졌다.
  - 단순히 무언가를 읽는 곳에서 -> 무언가를 하는 곳으로
  - 동적이고 반응적인 웹 애플리케이션을 개발
  - 코드 재사용성 증가
  - 개발 생산성 향상
## SPA
- 단일 페이지에서 동작하는 웹 애플리케이션
## CSR
- 클라이언트에서 콘텐츠를 랜더링 하는 방식
- SPA, CSR 단점: 느린 초기 로드 속도, 검색엔진 최적화 문제

## Vue
- 낮은 학습 곡선
- 확장성과 생태계
- 유연성 및 성능
- 2가지 핵심 기능  
  - 선언적 렌더링
  - 반응성
- Component: 재사용 가능한 코드 블록

## Template Syntax
- DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바이닝 할 수 있는 html 기반 템플릿 구문을 사용
- Text Interpolation:  
  - <p>Message: {{ msg }}</p> -> 데이터 바인딩의 가장 기본적인 형태, 이중 중괄호 구문 사용
- Rax Html:  
  - <div v-html="rawHtml"></div>
  - const rawHtml = ref('<span style="color:red">This should be red.</span>')
  - 콧수염 구문은 데이터를 일반 텍스트로 해석한다.
  - 그래서 실제 html을 출력하려면 v-html을 사용해야 한다.
- Attribute Bindings:  
  - <div v-bind:id="dynamicId"></div>
  - const dynamicId = ref('my-id')
  - v-bind를 사용해서 html의 id속성 값을 vue의 dynamicId속성과 동기화 되도록 한다.
- JavaScript Expressions:  
  - vue는 모든 데이터 바인딩 내에서 자바스크립트 표현식의 모든 기능을 지원한다.
  - {{ number + 1 }}
  - {{ ok ? 'YES' : 'NO' }}
  - {{ msg.split('').reverse().join('') }}
  - <div v-bind:id="`list-${id}`"></div>
- 각 바인딩에는 하나의 단일 표현식만 가능하다.
- Directive: 소성 값은 단일 자바 스크립트 표현식ㅇ어야 하낟.
- 표서현식 값이 변경될 때. DOM에 변셩될 때. dom에 반은적인 업데이트를 적용
- Directive:  
  - v-on:submit.prevent="onSubmit"
  - 일부 directive 는 directive 뒤에 콜론으로 표시되는 입자를 사용할 수 있음
  - 위의 코드는 event.preventDefault를 호출하도록 한다.
  - v-text, v-show, v-if, v-for 같은 것들이 있다.
## v-bind
- 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩
- html의 속성 값을 vue의 상태 속성 값과 동기화 되도록 한다.
- 동적 인자 이름: 대괄호로 감싸서 표현식을 사용할 수 있음. 대괄호 안은 반드시 소문자로만 구성 가능
- 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨
- 또한 v-bind는 생략이 가능하다. <img :src="imageSrc"> 이런식으로 콜론을 붙여 생략이 가능하다.
## class and style Bindings
- class와 style은 모두 html 소것ㅇ이므로 다른 속성과 마찬가지로 v- bind를 사용하여 동적으로 문자열 값을 할당할 수 있음
- 객체를 :class에 전달하여 클래스를 동적으로 전환 가능
- 객체에 더 많은 필드를 포함하여 여러 클래스를 전환할 수 있음
- inline 방식이 아닌 반응형 변수를 활용해 객체를 한번에 작성하는 방법
- class를 배열에 바인딩하여 클래스 목록을 적용할 수 있음
- style은 자바스크립트 객체 값에 대한 바인딩을 지원
- 실제 css에서 사용하는 것처럼 kebab-cased 키 문자열도 지원