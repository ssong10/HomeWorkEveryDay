### HomeWork 19

### 1. 해당 스키마를 가지는 데이터베이스 테이블 friends 를 생성

```SQL
CREATE TABLE friends (
	id INTEGER,
    name TEXT NOT NULL,
    location TEXT NOT NULL
)
```

### 2. 해당 테이블에 데이터 입력

```SQL
INSERT INTO friends 
VALUES (1,'Justin','Seoul'),(2,'Simon','New York'),
(3,'Chang','Las Vegas'), (4,'John','Sydney')
```

### 3. 스키마를 다음과 같이 변경하시오.

```SQL
ALTER TABLE friends ADD COLUMN marriged INTEGER
```

```SQL
UPDATE friends
SET marriged = 1 WHERE id=1 or id=4;
UPDATE friends
SET marriged = 1 WHERE id=2 or id=3;
```

> 스키마에 대한 데이터 변경

```SQL
ALTER TABLE freinds RENAME TO tmp;
CREATE TABLE friends (
	id INTEGER,
    name TEXT NOT NULL,
    location VARCHAR(100) NOT NULL
);
INSERT INTO friends SELECT * FROM tmp;
DROP TABLE tmp;
```

