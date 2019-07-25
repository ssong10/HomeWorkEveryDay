## HomeWork 5

### 1. fibo.py 파일에 작성 되어있을 때, import 구문을 채워 넣으시오.

```python
def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
```

```python
from fibo import fibo_recursion as recursion
recursion(4)
```

### 2. 다음 에러 발생 경우

```text
* ZeroDivisionError
	0으로 나누기를 할 때 발생
* NameError
	정의되지 않은 이름을 사용했을 때
	import되지 않은 모듈에 대해서도 NameError 발생
* TypeError
	피연산자(operand)나 함수(Function)에서 지원하지 않는 해당 type을 사용했을 때  
	인자의 갯수가 부족하거나, 많은 경우 (argument의 갯수가 맞지 않을때)
* IndexError
	a = [1, 2]
	a[3]
    # list index out of range
    # 리스트 범위밖의 인덱스를 참조했을 때
* KeyError
	딕셔너리에서 존재하지 않는 키값을 사용했을 때
* ModuleNotFoundError
	import mat
	## 존재하지 않는 모듈을 import했을 때
* ImportError
	from math import math.ad
    # 모듈은 맞게 불러왔지만 해당 변수, 함수, 클래스 등이 없는 경우
```

