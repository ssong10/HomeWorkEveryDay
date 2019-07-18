## Home Work 3

### 1. Python에서 기본 사용할 수 있는 Bulit in function 5개

```python
dir(__bulitins__)
```

```
abs(), dict(), bool(), min(), set(), sorted(), len(), print()
range()
```



### 2. 다음 함수중 오류 발생 코드

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')
```

```python
ssafy(location='대전', name='철수') # 순서가 바뀌어도 key값을 다 주어줬기때문에 가능
ssafy('길동', location='광주')  # 처음온값이 name으로 들어가고 마지막값에 location 지정!
ssafy(name='허준', '구미')  # 앞에값을 key를 주어지면 key를 다 주어져야함 error
```



### 3.  변수 result에 저장된 값.

```python
def my_func(a,b):
	c = a + b
	print(c)
	
result = my_func(4,7)
print(result)

# def문 안에서 print(c)인 11 출력하고 result는 None 이 남게됨.

print(a,b,c) # a, b, c 값은 사라지므로 에러
```