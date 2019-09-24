## HomeWork 18

### 1.

> 우리가 사용하년 SQLite는 RDBMS 에 속한다. RDBMS 의 특징을 2가지만 작성하시오.

```
관계형 모델을 기반으로 하는 데이터베이스 관리시스템.
모든데이터를 2차원 테이블로 설정을 한다.
테이블의 관계설정으로 이루어져있다.
1. 파일보다 더 빠르게 데이터를 접근할 수 있다.
2. 특정 패턴에 맞춰 데이터를 쉽게 추출 할 수 있다.
3. 많은 사용자의 동시 접근에 자체 해결방법을 가지고 있다.
4. 자체적 권한 시스템을 가지고 있다.
```

### 2.

1. RDBMS 를 조작하기 위해서는 SQL 문을 사용한다.

   > T - SQL(structured Query Language)는 관계형데이터베이스관리시스템의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어

2.  SQL에서 명령어는 대문자로 써야만 동작한다.

   > F  -  아니다 소문자도 가능하지만 구분을 위해 대문자로 표시

3.  일반적인 SQL문에서 명령어는 세미콜론(;) 으로 끝난다.

   > T - `;` 를 이용해서 문장 마무리를 해준다

4. SQLite에서 dot(.) 으로 시작하는 명령어는 SQL이 아니다.

   > T - SQL 이 아니라 설정을 위한 SQLite의 문법

5. 한 개의 DB에는 한개의 테이블만 존재한다.

   > F - 아니다 여러 테이블 존재 할 수 있다. 



## 3. 다음 코드의 실행결과로 나타나는 값을 작성하세요.

```sqlite
sqlite> .nullvalue ‘NULL’
sqlite> CREATE TABLE ssafy (
...> id INTEGER PRIMARY KEY,
...> location TEXT,
...> class INTEGER
...> );
sqlite> INSERT INTO ssafy (id, location)
...> VALUES (1, ‘JEJU’);
sqlite> SELECT class FROM ssafy WHERE id=1;
```

> nullvalue 설정을 'NULL' 로 해두고
>
> class에 값을 지정해두지 않아서 `NULL` 이 표기된다.