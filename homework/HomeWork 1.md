## HomeWork 1

### 1.  사용할 수 없는 식별자(예약어)

```python
import keyword
print(keyword.kwlist)
```

```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### 2. floating point rounding error

```python
a = 0.1 *3
b = 0.3
a==b  # False출력
```

```python
if abs(a-b) <= 1e-10:   # 값의 차이가 작다는 것을 의미해줌
    print(True)    # True값반환으로 충분이 작다
```

```python
import sys
abs(a - b) <= sys.float_info.epsilon  #시스템의 입실론값 대략 2.xx * 10^-16
```



### 3. 이스케이프 문자열 중 1) 줄바꿈 2)탭 3)\을 작성

```python
print('줄바꿈\n탭\t탭\n\\')
# 줄바꿈
# 탭		탭
# \
```



### 4.  String Interpolation

```python
name = '철수'
print('안녕, %s' % name) # % string
print('안녕, {}'.format(name)) # format string
print(f'안녕, {name}') # f string
print('안녕, ' + name)

# 안녕, 철수야
```

### 5.  형변환 가능 여부

```python
str(1)  # 문자 1로 형변환가능
int('30') # 숫자 30으로 가능
int(5) # 숫자 5로 가능
bool('50') # True 값 반환
int('3.5') #불가능 => float은 int로 변경가능, float에서 str으로 전환은 불가
```

