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

## Computed Property
- computed(): 계산된 속성을 정의하는 함수  
  - 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복 연산을 줄임
  - 복잡한 로직을 computed를 활용해 미리 값을 계산하여 계산된 값을 사용
  - 반환되는 값은 computed ref이며 이반 refs와 유사하게 계산된 결과를 .value로 참조할 수 있음
  - 의존된 반응형 데이터를 자동으로 추적
  - 의존하는 데이터가 변경될 때만 재평가
- computed 속성 말고 일반적인 함수 콜백인 method로도 동일한 기능을 정의할 수는 있다. 
- 다만 computed 속성은 의존된 반응형 데이터를 기반으로 캐시된다.
- 의존하는 데이터가 변경된 경우에만 재평가됨
- 반면 method호출은 다시 렌더링이 발생할 때마다 항상 함수를 실행
- 간단하게 computed는 한번만 호출하면 되지만 method는 일일이 호출해야 한다.
- computed: 의존하는 데이터에 따라 결과가 바꾸는 계산된 속성을 만들 때 유용, 의존된 데이터가 변경되면 자동으로 업데이트
- method: 단순히 특정 동작을 수행하는 함수를 정의할때 사용, 호출해야만 실행됨
## v-if
- 표현식의 값을 ture/false를 기반으로 요소를 조건부로 렌더링
- <p v-if="isSeen">true일때 보여요</p>
- <p v-else>false일때 보여요</p>
- 이런 식으로 v-if 에 대한 else 블록을 나타낼 수 있음
- v-else-if를 사용해 v-if에 대한 else if 블록을 나타낼 수 있음
## v-show
- 표현식 값의 true/false를 기반으로 요소의 가시성을 전환
- v-if의 경우 초기조건이 false인 경우 아무 작업도 수행하지 않는다. 토글 비용 높음
- v-show의 경우 초기조건에 관계없이 항상 렌더링 한다. 초기 렌더링 비용이 더 높음
- 콘텐츠를 매우 자주 전환해야 하는 경우에는 v-show, 실행 중에 조건이 변경되지 않는 경우에는 v-if 권장

## v-for
- 소스 데이터를 기반으로 요소 또는 템플릿 블록을 화면에 반복적으로 렌더링
- alias in sepression 형식의 특수 구문을 사용
- 인덱스에 대한 별칭을 지정할 수 있음
- 중첩된 이중 for문도 사용 가능
- 반드시 v-for와 key를 함께 사용한다. :key="item.id"
- 권장되는 key값:  
  - 데이터베이스의 고유 id
  - 항목 고유 식별자
- 동일요소에 v-for와 v-if를 함께 사용하지 않는다. 왜냐하면 동일한 요소에서 v-if가 우선순위가 더 높기 때문
- 이를 해결하기 위해서는 computed를 활용해 이미 필터링 된 목록을 반환하여 반복하도록 설정
- 또한 template를요소와 v-for를 사용해 v-if 위치를 이동한다.
- <template v-for="todo in todos" :key="todo.id">
- <li v-if="!todo.isComplete">
- 위와 같이 나눈다.

## Watchers()
- watch는 하나 이상의 반응형 데이터를 감시하고 감시하는 데이터가 변경되면 콜백 함수를 호출
- watch 구조:  
  - 첫번째(source)
  - 두번째(callback function)- newValue(감시하는 대상이 변화된 값), oldValue(감시하는 대상의 기존 값)
  - watch(count, (newValue, oldValue) =>{})
- computed는 의존하는 데이터 속성의 계산된 값을 반환할 때 사용.
- watcher는 특정 데이터 속성의 변화를 감시하고 작업을 수행
## Lifecycle Hooks
- vue 컴포넌트의 생성부터 소멸까지 각 단계에서 실행되는 함수
- 생성단계, 마운트단계, 업데이트 단계, 소멸단계 등 다양한 단계 존재
- mounting- 초기 렌더링 및 dom 요소 생성이 완료된 후 특정 로직 수행하기
- updating- dom이 업데이트 된 후 특정 로직 수행
- Lifecycle hooks with Cat API
- mounting 시점에 cat api에 요청을 보내고 애플리케이션 시작하기
## vue style guide
- 규칙범주는 필수, 적극 권장, 권장, 주의필요 이렇게 4가지 범주로 나뉜다.