## HomeWork 6

### 1. Python에서 정의되어있는 클래스 5가지

```text
int, float, str, complex, dict, list
```

### 2. 매직 메서드의 역할

* `__init__` :  생성자. 인스턴스가 처음 생성될 때의 초기값 설정, 호출 되는 메서드
* `__del__` :  소멸자. 인스턴스가 소멸, 삭제될때 자동으로 호출되는 메서드

* `__str__` : print()했을때 보여지는 값. 가면이라고 생각하자

  ​				`str` 만 있을 땐 print()값만 바뀌고 out값은 객체 형태

* `__repr__` : 객체의 모습,  `repr`만 있을땐 출력과 out 둘다 바뀜

### 3. `.sort()` 와 같이 문자열,리스트,딕셔너리 조작메서드

```python
numbers = [5, 1 ,2]
numbers.sort()
print(numbers)  # [1, 2, 5]
```

`.append()` : list에 값을 추가할 수 있게 해줌

`.pop()` : list의 하나를 뽑아낼 수 있음

`.capitalize()`: 문자열은 대문자로 변경해줌

`.split()` : 문자열을 해당 문자로 slicing 해줌

`.get()`: dictionary의 값을 인덱싱해줌 

`.keys()` : dictionary의 key 값을 뽑아줌

`.items()` : dictionary 의 key와 value값을 튜플형태로 뽑아줌