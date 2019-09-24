## WorkShop 19

### WorkShop 18에서 아래와같은 테이블을 만들었다.

### bands


| id(INTEGER) | name(TEXT) | debut(INTEGER) |
| ----------- | ---------- | -------------- |
| 1           | Queen      | 1973           |
| 2           | Coldplay   | 1998           |
| 3           | MCR        | 2001           |

 ### 1. 해당테이블에 다음과 같이 컬럼을 추가하고 데이터를 삽입하시오.

```SQL
ALTER TABLE bands ADD COLUMN members INTEGER;
UPDATE bands SET members=4 WHERE id=1;
UPDATE bands SET members=5 WHERE id=2;
UPDATE bands SET members=9 WHERE id=3;
```

### 2. id가 3인 레코드의 members를 5로 수정하는 SQL query

```SQL
UPDATE bands SET members=5 WHERE id=3;
```

### 3. id가 2인 레코드를 삭제하는 SQL query

```SQL
DELETE FROM bands WHERE id=2;
```
