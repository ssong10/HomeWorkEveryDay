## HomeWork 1

### 1. 

```python
import keyword
print(keyword.kwlist)
```

```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### 2. 

```python
a = 0.1 *3
b = 0.3
a==b  # False출력
```

```python
if abs(a-b) <= 1e-10:
    print(True)
```

```python
import sys
abs(a - b) <= sys.float_info.epsilon
```

### 3. 

```python
name = '철수'
print('Hello, %s' % name)
print('Hello, {}'.format(name))
print(f'Hello, {name}')
print('Hello, ' + name)
```

### 3. 

```python
str(1)  # 가능
int('30') # 가능
int(5) # 가능
bool('50') #가능
int('3.5') #불가능 => float은 int로 변경가능, float에서 str으로 전환은 불가
```

