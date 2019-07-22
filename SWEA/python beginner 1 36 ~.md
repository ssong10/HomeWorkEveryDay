# 파이썬 프로그래밍 기초(1) -2



36차시. 소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력

```python
a = int(input())
b=0

def sosu(num):
    if num == 2:
        return print("소수입니다.");
    for i in range(2,num):  #num= 5, i가 2에서 num까지 돌지
        if num % i == 0:  #검출되는 i 는 0개여야 소수입니다. 
            return print("소수일리가있겠냐?")
        else:
            return print("소수입니다.")

sosu(a)
```



37차시. 다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.

```python
a= int(input())
수열 = [1,1]

def 피보나치(n):   ##피보나치(2)일경우 수열[0] +수열[1]가 리턴
    return int(수열[n-2]) + int(수열[n-1])

for i in range(2,a):
    수열.append(피보나치(i))
    피보나치(i)
    
print(수열)
```



38차시.  리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고 이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하십시오.

```python
num = [1, 2, 3, 4, 3, 2, 1]
print(num)

print(list(set(num)))
```



39차시.  정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,

이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.  

```python
import random
list = [2, 4, 6, 8, 10]
print(list)
def search(n):
    return n in list
b = sorted(random.sample(range(1,11),2))
print("{0} => {1}".format(b[0],search(b[0])))
print("{0} => {1}".format(b[1],search(b[1])))
```

40차시.   다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한 팩토리얼 값을 구하는 프로그램을 작성하십시오.  

```python
a= int(input())
def factorial(num):
    n=1
    for i in range(1,num+1):
        n = n * i
    return print(n)

factorial(a)
```

41차시. 숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면 정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.

```python
a,b= input().split(', ')
def square(num):
    return int(num) * int(num)
print("square({0}) => {1}\nsquare({2}) => {3}".format(a,square(a),b,square(b)))
```

42차시. 인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고 결과를 출력하는 프로그램을 작성하십시오.

```python
a,b = input().split(', ')
if len(a) > len(b):
    print(a)
elif len(b) > len(a):
    print(b)
else:
    print("두 단어의 글자수가 같습니다.")  
```

43차시.   이 함수를 이용하여 countdown(0), countdown(10)을 순서대로 실행하십시오.

0보다 작거나 같은 인자가 전달되었을 경우 "카운트다운을 하려면 0보다 큰 입력이 필요합니다."를 출력하십시오.  

```python
def countdown(num):
    if num>=1:
        for i in range(num,0,-1):
            print(i)
    else:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
            
countdown(0)
countdown(10)
```

44차시. 올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.

```python
이름 = input()
나이 = int(input())

age = lambda x: 2118 - x

print("{0}(은)는 {1}년에 100세가 될 것입니다.".format(이름,age(나이)))
```



45차시.    다음의 결과와 같이 이름과 나이를 입력 받아 올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오. 

   * input 데이터 2개 받기 실패

```python
이름 = input()
나이 = int(input())
age = lambda x: 2118 - x
print("{0}(은)는 {1}년에 100세가 될 것입니다.".format(이름,age(나이)))
```



46차시.   "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.  



47차시.가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고, 단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.  

```python
a =input()
try:
    a = list(map(lambda x:int(x)*2,a.format(int).split(', ')))
    print(a)
except:
	print("에러발생")
```





48차시.  아스키코드 char 함수 이용 >>pass



49차시. 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해  짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.

```python
a = list(filter(lambda x:x%2==0,list(range(1,11))))
print(a)
```

50차시. 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해  항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.

```python
print(list(map(lambda x:x **2,range(1,11))))
```

51차시. 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해 짝수만을 선택한 후, map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.

```python
a = list(filter(lambda x:x%2==0,range(1,11)))
print(list(map(lambda x:x**2,a)))
```

52차시. 가변형 인자를 전달 받아 가장 큰 값을 반환하는 함수를 정의하고, 다음과 같은 결과를 출력하는 프로그램을 작성하십시오.

```python
a = 3, 5, 4, 1, 8, 10, 2
print("max{0} => {1}".format(a,max(a)))
```

53차시. 다음의 결과와 같이 'abcdef' 문자열의 각각의 문자를 키로 하고 0~5 사이의 정수를 값으로 하는 딕셔너리 객체를 생성하고, 이 딕셔너리 객체의 키와 값 정보를 출력하는 프로그램을 작성하십시오.