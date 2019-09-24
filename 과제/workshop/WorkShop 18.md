## WorkShop 18

## 1. 아래 표와 같은 스키마를 가진 DB테이블을 생성하고, 아래와 같이 데이터를 입력해 봅시다.

```sqlite
CREATE TABLE bands (
	id INTEGER PRIMARY KEY,
    name TEXT,
    debut INTEGER
)
```

> bands TABLE 생성

```SQL
INSERT INTO bands VALUES (1,'Queen', 1973),(2,'Coldplay',1998),(3,'MCR',2001);
```

> TABLE 에 데이터 값 추가

### 2.  모든 데이터 레코드의 id, name 조회

```SQL
SELECT id,name FROM bands;
```

### 3. debut 가 2000보다 작은 밴드들의 이름만 조회하는 SQL query문

```SQL
SELECT name FROM bands WHERE debut<2000;
```

