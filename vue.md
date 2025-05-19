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

## Component
- 재사용 가능한 코드 블록
- UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음
- 자연스럽게 애플리케이션은 중첩된 component의 트리 형태로 구성됨
## Single-File Components
- 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식( *.vue 파일 )
- 줄여서 SFC라고 한다.
- vue sfc는 html, css 및 자바 스크립트를 단일 파일로 합친 것이다.
- 하나의 파일로 독립적으로 배치한다고 생각하면 됨
- 작성 순서는 template, script, style 순서대로 할건데 이건 편의상 이렇게 하는 거고 다르게 해도 상관은 없음
- template블록: 각 *.vue 파일은 최상위 template 블록을 하나만 포함할 수 있음
- 각 *.vue 파일은 script setup 블록 하나만 포함할 수 있음
- 컴포넌트의 setup() 함수로 사용되며 컴포넌트의 각 인스턴스에 대해 실행
- 변수 및 함수는 동일한 컴포넌트의 탬플릿에서 자동으로 사용 가능
- *.vue 파일에는 여러 style 태그가 포함될 수 있다.
## Sfc build tool(vite)
- 1. npm create vue@latest(vue 프로젝트 생성) 
- 2. 프로젝트명 설정
- 3. 프로젝트에 추가 할 설정 선택(space 클릭 시 중복 선택 가능  )
- 4. 프로젝트 생성 완료
- 5. cd vue-project(프로젝트 폴더 이동)
- 6. npm install(패키지 설치)
- 7. npm run dev(vue 프로젝트 서버 실행)
- 모듈: 프로그램을 구성하는 독립적인 코드 블록
- 모듈의 필요성: 애플리케이션의 크기가 커져서 여러개로 분리하여 관리를 하기 위해 사용함
- 하지만 모듈 간의 의존성이 깊어지며 특정한 곳에서 문제가 발생하면 어떤 모듈간의 문제인지 파악하기 어려워짐
- 그래서 의존성 문제를 해결하기 위한 도구가 필요
- 번들러: 여러 모듈과 파일을 하나의 번들로 묶어 최적화하여 애플리케이션에서 사용할 수 있게 만들어주는 도구
- 번들러 역할: 의존성 관리, 코드 최적화, 리소스 관리. 이 번들러가 하는 작업을 번들링 이라 한다.
## vue project 구조
- public:  
  - 주로 소스코드에서 참조되지 않고 항상 같은 이름을 갖고 import 할 필요가 없는 다음 정적 파일을 위치 시킨다.  
  - 항상 root 절대 경로를 사용하여 참조
- src:  
  - 프로젝트의 주요 소스코드를 포함한 곳
  - 실제로 작업하게 될 대부분의 소스 코드가 위치
- src/assets:  
  - 프로젝트 내에서 사용되는 정적 자원 관리
  - 컴포넌트 자체에서 참조하는 내부 파일을 저장하는데 사용
- src/components:  
  - 실제로 페이지에서 사용하게 될 개별 Vue 컴포넌트들이 위치
- src/App.vue:  
  - vue 앱의 root 컴포넌트
  - 다른 하위 컴포넌트들을 포함
- src/main.js:  
  - Vue 애플리케이션을 초기화하고 App.vue를 DOM에 마운트하는 시작점
  - 필요한 라이브러리를 import하고 전역 설정을 수행
- index.html:  
  - vue 앱의 기본 html 파일
  - 필요한 스타일 시트, 스크립트 등의 외부 리소스를 로드할 수 있음
## 패키지 관리
- package.json:  
  - 프로젝트에 관한 기본 정보와 패키지 의존성을 정의하는 설계도 파일
  - 프로젝트가 어떤 패키지를 사용하고 어떤 스크립트를 실행할 수 있는지 명시
  - npm install 시 이를 참조하여 패키지를 설치
- package-lock.json:  
  - package.json을 기반으로 실제 설치된 패키지들의 정확한 버전 정보를 기록하는 파일
- node_modules:  
  - packge.json과 package-lock.json에 따라 실제로 설치된 모든 패키지가 저장되는 곳
  - 이는 프로젝트 실행 시 필요한 모든 라이브러리와 코드 파일을 보관한다.
## Vue Component
- 컴포넌트 사용 2단계  
  - 1. 컴포넌트 파일 생성
  - 2. 컴포넌트 등록(import)
- 사전준비  
  - app.vue 초기화, vue 찍으면 바로 나옴
  - 컴포넌트 파일 생성
  - 컴포넌트 등록
  - 결과 확인
  - alt+shift+D 를 하면 일반 페이지에 vue볼 수 있음 
## 추가 주제
- Compositions API, OPtion API
- Composiotion API:  
  - import해서 가져온 API 함수들을 사용하여 컴포넌트의 로직을 정의, vue3 방식
- Options API:  
  - data, methods, 및 mounted 같은 객체를 사용하여 컴포넌트의 로직을 정의, vue2 방식이긴 한데 vue3에서도 지원
## 참고
- 모든 컴포넌트에는 최상단 html 요소가 작성되는 것이 권장
- 예를 들어 template 안에 div 쓰고 그 안에 요소 쓰기
- scoped 속성은 컴포넌트 내부 요소에게만 적용되도록 범위를 제한하는 기능이다.
- 즉, 스타일이 컴포넌트 바깥으로 유출되거나 다른 컴포넌트에서 정의한 스타일이 현재 컴포넌트를 침범하지 않도록 막아 줌
## pasing Props
- Props:  
  - 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성
  - 부모 속성이 업데이트되면 자식으로 전달 되지만 그 반대는 안됨
  - 부모 컴포넌트에서만 변경하고 이를 내려받는 자식 컴포넌트는 자연스럼게 갱신
- one-way data flow:  
  - 모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩을 형성
  - 단방향인 이유는 데이터 흐름의 일관성 및 단순화 때문임
- 사전준비:  
  - 1. APP > Parent > ParentChild 컴포넌트 관계 작성
  - 2. APP 컴포넌트 작성
  - 3. Parent 컴포넌트 작성
  - 4. ParentChild 컴포넌트 작성
- Props 작성:  
  - my-msg='message' props 이름=props 값
  - 무조건 html 처럼 캐밥 케이스로 작성해야 한다. mymsg -> my-msg 이렇게
  - <ParentChild my-msg="message"/> 이런식으로
  - 바인딩 하자!
  - 
- Props 선언:  
  - defineProps를 사용해 선언, script에 작성한다.
  - 문자열 배열을 이용하거나 객체를 선언하여 이용하기도 한다.(딕셔너리)
  - 자식에 작성한다.
  - defineProps({userName: String}) 이거는 자식이 부모로무터 userName 이라는 prop를 문자열 타입으로 받을 것이라는 선언
  - 만약 item: Object 이렇게 되어 있으면 객체 타입으로 받을 것이라는 의미
  - <ChildItem v-for="item in items":key="item.id":item="item"/> 이건 context로 생각하면 편함. key, value 2개 필요
  - 만약 console로 보고 싶으면 const props = 이렇게 앞에 const를 정의해 준 후 console.log를 해야 함
- emit:  
  - 부모가 props 데이터를 변경하도록 소리침
  - $emit() 형식으로 쓰며 자식 컴포넌트가 이벤트를 발생히켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드
  - $emit(event ,args) event: 커스텀 이벤트 이름, args: 추가인자

## Routing
- 네트워크에서 경로를 선택하는 프로세스
- Vue Router: Vue 공식 라우터
- router.push(): 다른 위치로 이동하기
- router.replace(): 현재 위치 바꾸기
- route:  
  - 읽기 전용
  - 반응형
  - 현재 경로에 대한 정보 확인
  - 하지만 route 객체 자체를 통해 페이지 이동을 직접 제어할 수는 없음
  - useRoute()는 현재 url상태를 일기 위한 객체를 제공하는것
- router:  
  - 페이지 이동, 네비게이션 관련 메서드 제공
  - 네비게이션 가드 등록, 히스토리 제어 같은 기능 사용 가능
  - 프로그램적으로 경로 변경, 뒤로 가기, 앞으로 가기
  - useRouter는 라우터 전체 제어를 담당하는 객체를 제공하며 push, replace등의 메서드를 사용하여 경로 이동을 실행할 수 있음
- Navigations Guard:  
  - vue router를 통해 특정 url에 접근할 때 다른 url로 redirct하거나 취소하여 내비게이션을 보호
  - Globally, Per-route, In-component 3가지 있음
  - Globally:  
    - 애플리케이션 전역에서 동작하는 가드, index.js에 작성한다.
    - beforeEach, BeforeResolve, afterEach 3가지 있음
    - beforeEach: 다른 url로 이동하기 직전에 실행되는 함수, 모든 가드의 콜백함수는 2개의 인자를 받음
  - pre-route:  
    - 특정 라우터에서만 동작
    - beforeEnter메서드 있고 index의 routes에 쓴다
    - beforeEnter는 특정 route에 진입했을 때만 실행된다.
  - In-component:  
    - 특정 컴포넌트 내에서만 동작하는 가드, 각 컴포넌트의 script에 작성
    - onBeforeRouteLeave:  
      - 현재 라우트에서 다른 라우트로 이동하기 전에 실행
    - onBeforeRouteUpdate:  
      - 라우트 업데이트 시 추가적인 로직을 처리
## state Management
- 상태 관리
- vue 컴포넌트는 이미 반응형 상태를 관리하고 있음, 상태 === 데이터
- 상태(state): 앱 구동에 필요한 기본 데이터
- 뷰(view): 상태를 선언적으로매핑하여 시각화
- 기능(Actions): 뷰에서 사용자 입력에 대해 반응적으로 상태를 변경할 수 있게 정의된 동작
- 뷰 -> 기능 -> 상태 -> 뷰 단방향 데이터 흐름이다.
- 상태 관리의 단순성이 무너지는 시점:  
  - 1. 여러 컴포넌트가 상태를 공유할 때
  - 2. 여러 뷰가 상태에 종속되는 경우
  - 3. 서로 다른 뷰의 기능이 동일한 상태를 변경시켜야 하는 경우
- 해결책: 각 컴포넌트의 공유 상태를 추출하여 중앙 저장소를 만들어 관리
- 각 컴포넌트의 공유상태를 추출하여 전역에서 참조할 수 있ㄴ는 저장소에서 관리
- vue의 공식 상태 관리 라이브러리 === "Pinia"
## Pinia
- store:  
  - 중앙 저장소
  - 모든 컴포넌트가 공유하는 상태, 기능 등이 작성됨
  - defineStore()의 반환 값의 이름은 user와 store를 사용하는 것을 권장
  - 첫번째 인자는 애플리케이션 전체에 걸쳐 사용되는 sotre의 고유 id
- state:  
  - 반응형 상태(데이터)
  - ref() === state
- getters:  
  - 계산된 값
  - computed() === getters
- actions:  
  - 메서드
  - function() === actions
- Setup Stores의 반환 값
- pinia 상태들을 사용 하려면 반드시 반환해야 함
- plugin:  
  - 애플리케이션의 상태 관리에 필요한 추가 기능을 제공하거나 확장하는 도구나 모듈
  - 애플리케이션의 상태 관리를 더욱 간편하고 유연하게 만들어주며 패키지 매니저로 설치 이후 별도 설정을 통해 추가 됨
- 경로: @는 /src이다.
- .은 현재 경로에서 시작
- ..은 한칸 위 폴더에서 시작한다.
- <p>state : {{ store.count }}</p>
- <p>getters: {{ store.doubleCount }}</p>
- <button @click="store.increment">click</button>
- <Example />
- import Example from './components/example.vue';
    import { useCounterStore } from '@/stores/counter.js'
  const store = useCounterStore()

## vue with drf
- 1. 게시글 전체 조회 화면 구성
- 2. 컴포넌트에 적절한 tag들 작성
- 3. 게시글 데이터를 화면에 그릴 수 있도록 더미데이터를 생성한다. -> store
- 4. 단순히 아무런 객체나 만드는 것이 아니라 백엔드에서 넘겨주기로 했던 데이터의 생김새와 동일하게 만들어 두면 좋겠다/
- 5. 당연하게도 코드 작성하기 전에 미리, 그러한 컴벤션등이 정의되어 있으면 좋겠다.
- SOP: 동일 출처 정책  
  - 어떤 출처에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호 작요하는 것을 제한하는 보안 방식
-  origin(출처): url의 프로토콜, 호스트, 포트를 모두 출처라고 한다.
-  ex) http://127.0.0.1:8000
- cors:  
  - 특정 출처에서 실행 중인 웹 애플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제