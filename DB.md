# DB
## 개요
- 데이터베이스: 체계적인 데이터 모음
- 데이터: 저장이나 처리에 효율적인 형태로 변환된 정보
- 기존 데이터 저장 방식:  
  - 1. 파일 이용  
    - 1. 어디서나 쉽게 사용 가능
    - 2. 데이터를 구조적으로 관리하기 어려움움
  - 2. 스프레드 시트 이용  
    - 1. 테이블의 열과 행을 사용해 데이터를 구조적으로 관리 가능
    - 2. 하지만 100만행까지만 저장 가능
    - 3. 단순히 파일이나 링크 소유 여부에 따른 단순한 접근 권한 기능 제공
    - 4. 만약 한 데이터를 바꾸면 이 변경으로 인해 모든 테이블 위치에서 해당 값을 업데이트 해야 한다.
    - 5. 만약 여러 시트에 분산되어 있으면 누락이나 추가 문제가 발생할 수 있음.
- 결국 데이터베이스는 데이터를 저장하고 조작한다.

## Relational Database
- 데이터 간에 관계가 있는 데이터 항목들의 모음이다.
- 테이블, 행, 열의 정보를 구조화하는 방식
- 서로 관련된 데이터 포인터를 저장하고 이에 대한 액세스를 제공
- 관계: 여러 테이블 간의 (논리적) 연결
- 관계로 할 수 있는것: 특정 날짜에 구매한 고객 조회, 지난 달에 배송일이 지연된 고객 조회 등
- 만약 고객 데이터 간 비교를 위해서는 기본키(PK) 를 사용해야 한다.
- 만약 주문 테이블에서 누가 어떤 주문을 했는지 식멸하려면 외래키(FK)를 사용해야 한다.
- 관련 키워드:  
  - 1. Table: 데이터를 기록하는 곳
  - 2. Field: 각 필드에는 고유한 데이터 형식이 지정됨(세로)(컬럼)
  - 3. record: 각 레코드에는 구체적인 데이터 값이 저장됨(가로)(로우)
  - 4. Database: 테이블의 집합
  - 5. PK(기본키): 각 레코드의 고유한 값. 레코드의 식별자로 활용
  - 6. FK(외래키): 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키  
    - 다른 테이블의 기본 키를 참조
    - 각 레코드에서 서로 다른 테이블 간의 관계를 만드는데 사용
## RDBMS
- DBMS: 데이터베이스를 관리하는 소프트웨어 프로그램
- 데이터 저장 및 관리를 용이하게 하는 시스템
- 데이터베이스와 사용자 간의 인터페이스 역할
- 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움
- RDBMS: 관계형 데이터베이스를 관리하는 소프트웨어 프로그램
- sqlit, 오라클 등이 RDBMS 서비스 종류이다.
- 데이터는 기본 키 또는 왜리키를 통해 결합될 수 있는 여러 테이블에 걸쳐 구조화 됨.
## SQL
- 데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
- 정확히는 관계형 데이터베이스와의 대화를 위해 사용하는 프로그래밍 언어이다.
- SELECT colunb_name FROM table_name;
- sql 키워드는 대소분자 구분하지 않는다. 하지만 대문자로 작성하는 것을 권장한다. 위의 문장에서 대문자로 된 것이 sql 키워드 이다.
- 그리고 각 sql 문장 끝에는 세미콜론이 필요하다. 
## SQL statements
- SELECT colunb_name FROM table_name; 여기서 예시 코드는 SELECT statement라고 부른다.
- 이 문장은 select, from 2개의 키워드로 구성된다.
- 4가지 유형이 있다.  
  - DDL: 데이터 정의, 데이터의 기본 구조 및 형식 변경, CREATE, DROP, ALTER
  - DQL: 데이터 검색, SELECT -> 검색이 가장 중요!
  - DML: 데이터 조작(추가, 수정, 삭제), INSERT, UPDATE, DELETE
  - DCL: 데이터 제어, 데이터 및 작업에 대한 사용자 권한 제어, COMMIT, ROLLBACK, GRANT, REVOKE
## Querying data
- SELECT: 테이블에서 데이터를 조회한다.
- selsect 키워드 이후 데이터를 선택하려는 필드를 하나 이상 지정
- from 키워드 이후 데이터를 선택하려는 테이블의 이름을 지정
- 1. create-connections -> sqlite -> 아래 파란색 파일 버튼 누르기 -> 데이터베이스가 있는위치에서 찾기 -> 선택한 후 connect 누르기
- SELECT 
  LastName
FROM
  employees;
- 위의 코드는 employees테이블에서 lastname 필드의 모든 데이터를 조회한다.
- SELECT 
  *
FROM
  employees;
- 위의 코드는 employees테이블의 모든 필드를 가져온다.
- 만약 필드 옆에 AS '이름' 이렇게 하면 조회시 firstname이 아니라 '이름'으로 출력 될 수 있도록 변경
- Milliseconds / 60000 이런식으로 분 단위 값으로 출력이 가능하다.
- ORDER BY statement: 조회 결과의 레코드를 정렬, 기본적으로 오름차순으로 정렬한다.
- 내림차순은 FirstName DESC 이렇게 desc를 붙여야 한다.
- Country DESC, city; 이런 식은 country는 내림차순, city는 오름차순이다. 그런데 country필드를 기준으로 내림차순하고 이 기준으로 city 필드를 오름차순 한다. 그러니까 같은 나라별로 city가 오름차순 되는 것이다.
- 만약 null 값이 존재할 경우 null 값이 먼저 출력된다.
## Filtering data
- Clause:  
  - DISTINCT
  - WHERE
  - LIMIT
- Operator:  
  - BETWEEN
  - IN
  - LIKE
  - Comparison
  - Logical
- Distinct :조회 결과에서 중복된 레코드를 제거  
  - 1. select 키워드 바로 뒤에 작성해야 한다.
  - 2. select distinct 키워드 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정
- where: 조회 시 특정 검색 조건을 지정  
  - 1. from clause 뒤에 위치
  - 2. between을 쓰면 어디 사이의 값을 나오게 된다.
  - 3. in을 쓰면 or처럼 되서 해당하는 필드를 뽑게 된다.
  - 4. LastName LIKE '%son'; 이렇게 쓰면 lastname필드 값이 son으로 끝나는 데이터의 필드를 조회
- 이때 select -> from -> where -> order by 순으로 정렬한다.\
- Like: 값이 특정 패턴에 일치하는지 확인
  - %: 0개 이상의 문자열과 일치 하는지 확인
  - -: 단일 문자와 일치하는지 확인
  - '___a' 이건 모두 4자리이면서 끝자리가 a로 끝나는 것을 찾으라는 것이다.
- LIMIT: 조회하는 레코드 수를 제한  
  - 만약 limit 2, 5라고 하면 인덱스 처럼 2번 오프셋부터 5개의 오프셋을 뽑는다. 그러니 7번 오프셋까지 뽑는다.
  - ORDER BY Bytes DESC  
    LIMIT 7; - 이거는 바이츠를 기준으로 내림차순 하고 큰것부터 7개를 뽑으라는 의미 이다.
  - LIMIT 3, 4; 이거는 4번째부터 7번째 데이터만 조회. 인덱스처럼 이해해야 한다.
- group by:
- 레코드를 그룹화하여 요약본 생성. 이를 위해 집계함수가 필요
- 집계함수:  
  - sum, avg, max, min, count -> 전부 대문자로 써야 한다.
- GROUP BY  
  Country; - 이거는 country를 그룹화 하는 것이다.
- COUNT(*) - 이 함수가 각 그룹에 대한 집계된 값을 계산. 그러니까 만약 나라고 하면 해당 나라에 몇 명의 사람이 있는지 나타낼 수 있다.
- 그런데 집계 항목에 대한 세부 조건을 지정하기 위해서는 HAVING을 써야 한다.
- 예를 들어 AVG(Milliseconds / 60000) 이렇게 세부 조건이 있을 때는 having을 써야 한다.

## Managing Tables
### create a table
- 테이블 생성
- CREATE TABLE table_name(이건 테이블 이름) (열 이름, 데이터 타입, 제약조건) 이 순서대로 작성된다.
- PRAGMA table_info('examples'); 이거는 테이블 schema(구조) 확인을 한다.
- AUTOINCREMENT 이거는 그냥 키워드. 제약조건 아니다.  
  - 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성
  - 필드의 자동 증가를 나타낸다.
  - 주로 pk 필드에 적용
  - 삭제된 값은 무시되며 재사용 할 수 없게 된다.
  - INTEGER PRIMARY KEY AUTOINCREMENT가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값을 할당한다.
- 데이터 타입 5개:  
  - NULL - 아무런 값도 포함하지 않음
  - INTEGER - 정수
  - REAL - 부동 소수점
  - TEXT - 문자열
  - BLOB - 이미지, 동영상, 문서 등의 바이너리 데이터
- Constraints(제약조건) - 데이터의 무결성 유지 및 데이터베이스의 일관성 보장.
- 대표 3가지:  
  - PRIMARY KEY - 해당 필드를 기본 키로 지정. Integer타입에만 적용된다!
  - NOT NULL - 해당 필드에 null값을 허용 않도록 지정
  - FOREIGN KEY - 다른 테이블과의 외래 키 관계를 정의
### Modifying table fields
- ALTER TABLE: 테이블 및 필드 조작  
  - ALTER TABLE ADD COLUMN : 필드 추가
  - ALTER TABLE RENAME COLUMN : 필드 이름 변경
  - ALTER TABLE DROP COLUMN : 필드 삭제
  - ALTER TABLE RENAME TO : 테이블 이름 변경
- 구조는 다음과 같다.  
  - alter table
  - table_name(테이블 이름)
  - add column
  - colunm_definition;(열 제약조건)
- NOT NULL DEFAULT : null 값이 없고 기본값은 넣을 거다.
- 그런데 한번에 여러개의 열을 추가하는 것은 안되고 하나씩 해야 한다. 
- 무조건 alter table - add column 이 구조를 반복해야 한다.
### Delete a table
- Drop Table : 테이블 삭제
- DROP Table new_examples; 이렇게 짜면 테이블이 삭제된다.
## Modifying Data
### Insert data
- 사전 준비 필요(그냥 테이블 새로 만들기!)
- INSERT INTO table_name(c1, c2 ...)
- VALUES (v1,v2, ..)
- insert는 동시에 여러개 삽입 가능
- VALUES  
  ('title1', 'content1', '2000-01-01'),
  ('title2', 'content2', '1900-01-01'),
  ('title3', 'content3', '1800-01-01');
- ('mytitle', 'mtcontent', DATE()) : 이거는 그 일자 자동 생성
### Update data
- 테이블 레코드 수정
- UPDATE table_name
- SET column_name = expression,
- WHERE condition;
- condition쪽에는 id = 1 이렇게 지정하면 된다.
- set 절 다음에 수정할 필드와 새 값을 지정
- where절에서 수정할 레코드를 지정하는 조건 작성
- where절을 작성하지 않으면 모든 레코드를 수정
### Delete data
- 테이블 레코드 삭제
- DELETE FROM table_name
- WHERE condition;
- 만약 where작성하지 않으면 테이블의 모든 레코드 삭제
- DELETE FROM
- articles
- WHERE id IN(
  SELECT id FROM articles
  ORDER BY createdAt
  LIMIT 2
); -> 괄호 안이 서브 쿼리이다.
- 위와 같은 코드는 articles 테이블에서 작성일이 오래된 순으로 레코드 2개를 삭제한다는 뜻이다.
## Multi table queries
### Joing
- join
- 관계(여러 테이블 간의 (논리적)연결)
- 동명이인을 출력할 수도 있다. 그래서 테이블을 나누어서 분류하자.
- 이때 pk가 아니라 외래 키 필드가 필요하다.
- 만약 articles에 이름, 내용이 있다면 userid를 가지고 있어야 하고 user테이블의 경우 이름이 있을 때 roleid가 있어야 한다. 그래서 관리자인 사람만 보고 싶으면 roleid를 확인하면 되고 만약 한 사람이 이름을 변경했으면 userid 하나만 변경하면 보두 자동으로 변경된다.
- 즉, 다른 테이블과 결합하여 출력하기 위해 join이 필요하다.
### Joining tables
- join: 둘 이상의 테이블에서 데이터를 검색하는 방법, select문과 같이 쓰인다.
- FOREIGN KEY (userId) 
    REFERENCES users(id)
- users의 id를 참조하여 외래키를 만들겠다.
- INNER JOIN: 
  - 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
  - select -> from -> inner join 참조할 테이블 on 참조할 테이블의 fk = 원본 테이블의 pk
  - 문제는 1번 회원이 작성한 모든 게실글의 제목과 작성자명을 조회 이런 식으로 나온다.
- LEFT JOIN:
- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
- select -> from 원본 테이블 -> left join 참조할 테이블 -> on 참조할 테이블의 fk = 원본 테이블의 pk

## Many to one relationships
### 모델 관계
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
- comment에 id 포함 4개 생성. -> content, created-at, updated_at
- Article에 id 포함 5개 생성. -> title, content, created_at, updated_at
- comment쪽에서 article에 대한 외래키를 가지고 있어야 한다. 이때 외래키는 article의 id와 연동되어 있어야 한다.
- 보통 N:1 or 1:N 관계인데 commet(N) - article(1) 이 경우는 0개 이상의 댓글은 1개의 게시글에 작성될 수 있다는 뜻이다. 
### 댓글 모델 정의
- 외래키: 모델 정의 시 클래스 인스턴스 이름은 참조하는 모델 클래스의 이름의 단수형으로 작성하는 것은 권장
- 외래키는 작성 위치 상관 없이 무조건 마지막 필드로 생성됨
- 작성법:  
  - ex) article = models.ForeignKey(Article, on_delete=models.CASCADE)
  - ForeignKey(to, on_delete)
  - to : 참조하는 모델 class 이름
  - on_delete : 외래키가 참조하는 객체가 사라졌을 때, 외래키를 가진 객체를 어떻게 처리할 지를 정의
  - 만약 1번 게시글에 막 200개의 파일 등이 있는데 1번 게시글이 사라진다면? 어떻게 처리할 지 정의하는 것
  - CASCADE: 부모 객체가 삭제될 때 이를 참조하는 모든 객체도 삭제되도록 지정
  - 만약 1번 개시글을 지우면 하위 폴더나 파일 전부 지우겠다는 뜻
  - protect, restrict 등 기능이 다른 것은 많다. 공식 홈페이지 참조하기
  - python manage.py sqlmigrate articles 0003 이거는 미리보기
  - 외래키의 경우 article 이렇게 설정하면 db 생성 시 article_id로 표시된다.
  - 외래키 설정시 단수형으로 해놔야 어느 클래스를 참조하는지 확인하기 편하다.
### 댓글 생성 연습
- 1. shell_plus 실행
- 2. Comment 클래스의 인스턴스 comment 생성.(모델 생성 시 대문자로 꼭 하자! 안그러면 설계도 삭제하던가 아니면 다시 찍고 추가해야 한다!)
- 3. 인스턴스 변수 저장
- 4. db에 댓글 저장
- 5. 그럼 에러 발생하는데 articles_comment테이블의 외래키, article_id 값이 누락되었기 때문이다.
- 6. 해결하기 위해서 일단 게시글 조회. article = Article.objects.get(pk=1)
- 7. 외래키 데이터 입력 comment.article = article, 만약 comment.article_id = article.pk로 하고싶으면 할 수도 있는데 권장은 안함.
- 8. 댓글 저장 comment.save()
- 9. comment = Comment.objects.get(pk=1) -> comment -> comment.article => 이걸로 게시글의 내용까지 가져올 수 있음
- 10. comment = Comment(content='second', article=article) -> comment.save() 이렇게 하면 2번째 입력하고 정보가져올 수 있음.
## 관계 모델 참조
### 역참조
- 참조(comment -> Article)
- 역참조(Article -> comment)
- 그런데 1은 N에 대한 역참조가 물리적으로 불가능해 별도의 역참조 키워드 필요
- article.comment_set.all() -> 모델 인스턴스.역참조 이름.쿼리셋 api
- 특정 게시글에 작성된 댓글 전체를 조회하는 요청
- 특정 댓글의 게시글 참조: comment.article
- 특정 게시글의 댓글 목록 참조: article.comment_set.all()
## 댓글 구현
### 댓글 create
- view와 detail 수정
- 그리고 article은 필요 없어서 forms에서 fields = ('content',)로 출력 필드 조절
- url 추가 필요 path('<int:pk>/comments/', views.comment_create, name='comment_create') 이런식으로 pk를 받아야 한다.
- save(commit=False) 필요
### 댓글 read
- detail view함수에서 전체 댓글 데이터 조회
### 댓글 delete
- 삭제 url 작성
- view함수 정의
- 삭제버튼 작성
- 테스트
- path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
- 위와 같이도 된다.
- 댓글이 없으면 {%empty%}를 for 문 안에 쓰고 p같은 것으로 '댓글 없음'이런식으로 하면 된다.
## Article & User
- Article- User -> N : 1구조이다.
- get_user_model은 user object즉, 객체를 반환한다. 그리고 models.py가 아닌 다른 모든 위치에서 사용한다.
- settings.AUTH_USER_MODEL 이거는 accounts.User을 반환하며 models.py에서만 사용한다.
- 게시글 create 방법:  
  - 1. 불필요한 input 확인
  - 2. articleform 필드 수정 -> 이건 임시 방편 아직 안끝났다!
  - 3. 그러면 입력 시 user_id가 없기에 오류남. view의 create에서 유효성 검사 아래 다음과 같이 작성한다.  
    - article = form.save(commit=False) 유효성 검사 한 form 저장
    - article.user = request.user 이미 요청 객체에 어떤 사람인지 들어있기 때문에 조회하지 않는다.
    - 그 다음 article = form.save() article 변수 저장한다.
- 게시글에서 작성자를 읽으려면 <p>작성자 : {{ article.user }}</p> 이 코드 쓰면 된다.
- 게시글 업데이트:  
  - 1. 기존 update에 
- Comment - User -> N : 1구조이다.
## decorators
- view 함수의 동작을 수정하거나 추가 기능을 제공하는데 사용되는 데코레이터
- 코드의 재사용성을 톺이고 뷰 로직을 간결하게 유지
## Allowed HTTP methods
- 특정 http method로만 view 함수에 접근할 수 있도록 제한하는 데코레이터
- require_http_methods : 지정된 http method만 허용
- require_safe : get과 head method만 허용
- require_POST : post method만 허용
- 만약 지정되지 않은 http method로 요청이 들어오면 405 를 반환. 대문자로 HTTP method를 지정
## ERD
- 데이터베이스의 구조를 시각적으로 표현하는 도구
- 엔티티, 속성, 관계로 이루어진다.
- 표처럼 그려진다.
- 주로 관계:  
  - 일대일
  - 다대일
  - 다대다