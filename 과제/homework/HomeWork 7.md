## HomeWork 7

```python
class Calculator:
    count = 0
    
    def info(self):
        print('나는 계산기 입니다.')
        
    @staticmethod
    def add(a,b):
        Calculator.count += 1
        print(f'{a} + {b} 는 {a + b} 입니다.')
        
    @classmethod
    def history(cls):
        print(f'총 {cls.count}번 계산 했습니다.')
```

### 1.  인스턴스, 스태틱, 클래스 메서드에 해당하는 함수

```text
instance = info()
static = add()
class = history()
```

### 2. 각각의 메서드를 실행하는 코드를 작성하시오.

```python
calc = Calculator()
```

```python 
calc.info() # '나는 계산기 입니다.'
Calculator.add(1,2) # '1 + 2 는 3 입니다.'
Calculator.history()  # '총 1번 계산 했습니다.'
```

### 3. 파라미터 self와 cls에는 어떤 값이 할당되는지

```text
self -> instance 객체(c1 인스턴스)
cls - > 'Calculator' Class 객체
```



