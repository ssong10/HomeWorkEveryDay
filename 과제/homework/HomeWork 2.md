## Home Work 2

### 1.  mutable, immutable 구분

```
List,  Set, Dictionary  = Mutable

string, tuple, range= immutable
```

```python 
a = 123
a[0] = 3  # error
## Mutable == 접근만 가능하고 변경 불가
range(1,10)[0] ##=> 1
range(1,10)[0] = 3  # error
(1,2)[0] = 2 # error
```



### 2. range와 slicing을 활용하여 1~ 50까지의 홀수 리스트

```python
print(list(range[1:50:2]))
```

### 3. 반 학생들의 정보를 이용하여 key-이름, value-나이 인 딕셔너리

```python
classes = {'이승열': 9302 , '장은비': 9409 , '김태우': 910707}
```

