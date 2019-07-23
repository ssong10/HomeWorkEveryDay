## WorkShop 5

### 1. calc.py 작성 

 >(나누기에서  try except 구문사용 ZeroDivisionError 예외처리)

```python
### calc.py에 저장합니다.
def sum(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a * b
def div(a, b):
    try:
    	return a / b
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'
```

### 2. calc.py 모듈을 import하여 실행

```python
import calc
a = calc.sum(6,3)
print(a)  # 9
b = calc.sub(6,3)
print(b)  # 3
c = calc.mul(6,3)
print(c)  # 18
d = calc.div(6,3)
print(d)  # 2.0
e = calc.div(6,0)
print(e)  # 0으로는 나눌 수 없습니다.
```

```python
from calc import div   # from 모듈 import 함수 
a = div(6,0)
print(a)  # 0으로는 나눌 수 없습니다.
```
