# 파이썬 프로그래밍 기초 (1) -1



5차시. 1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.

```python
a = int(input())
if a >= 1 and a <=9 :
    print(a +11*a+111*a+1111*a)
else:
    print ("한자리 정수만 입력하세요")
```



7차시. 인치(inch)를 센티미터(cm)으로 변환하는 프로그램을 작성하십시오.

이 때 1 인치는 2.54 센티미터입니다.

```python
a = int(input())
print("%0.2f inch =>  %0.2f cm" %(a,a*2.54))
```



10차시.화씨(℉)를 섭씨(℃)로 변환하는 프로그램을 작성하십시오.

이 때 물의 빙점은 화씨 32도이고 비등점은 화씨 212도(표준 기압에서)입니다.

물의 비등점과 빙점 사이에 정확하게 180도 차이가 납니다.

그러므로 화씨 눈금에서의 간격은 물의 빙점과 비등점 사이의 간격의 1/180입니다.

```python
a=int(input())
print("%0.2f ℉ =>  %0.2f ℃" %(a,(a-32)*5/9))
```



11차시. 20% 농도의 소금물 100g과 물 200g을 혼합한 소금물의 농도(%)를 소수점 두 번째 자리까지 구하는 프로그램을 작성하십시오.

```python
salt = 20/100*100
print("혼합된 소금물의 농도: %0.2f%%" %(salt/300*100))
```



14차시. 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오

약수가 두개일경우 소수입니다. 표시 

```python
a = int(input())
j= 0
for i in range(1,a+1):
    if a%i==0:
        print("%d(은)는 %d의 약수입니다." %(i,a));
        i+=1
        j+=1
if j==2:
    print("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다." %(a,1,a))
```



17차시. 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고, 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.  출력 시 아스키코드를 함께 출력합니다.

```python
a= input()
b=ord(a)
c=a.swapcase()
d=ord(c)
print("%s(ASCII: %s) => %s(ASCII: %s)"%(a,b,c,d))
```



18차시. 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아  콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.

> print 마지막에도 , 찍히는 오류 수정필요 => a(빈리스트)추가 후에 * , sep 기능을 이용하여 해결

```python
a= []
for i in range(1,201):
	if i % 7 == 0 and  i % 5 != 0:
		a.append(i)
print(*a,sep = ',')
```



19차시. 100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.

> 위와 같은문제 발생  =>  해결


  ```python
num =[]
for i in range(100,301):
	b= list(str(i))
	if (int(b[0]) % 2 == 0) and (int(b[1]) % 2 == 0) and (int(b[2]) % 2 == 0):
		num.append(i)
print(*num, sep = ',')
  ```



21차시. 다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고, 60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.

```python
학생 = [88,30,61,55,95]
for a in range(0,5):
    b= int(학생[a]);
    if b>= 60:
    	result = "%d번 학생은 %d점으로 합격입니다." %(a+1,b);
    else:
        result = "%d번 학생은 %d점으로 불합격입니다." %(a+1,b);
    print(result)
```



23차시. 1부터 100사이의 숫자 중 짝수를 for 문을 이용해 다음과 같이 출력하십시오.

```python
num = [ ]
for i in range(101):
    if i % 2 == 1:
        num.append(i)
print(*num,sep = ', ')
```

25차시. 1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.

```python
b=0;
for a in range (1,101):
    if a%3 == 0 :
        b = b+a
print("1부터 100사이의 숫자 중 3의 배수의 총합: {0}".format(b))
```



26차시. 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.

['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

```python
P = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
a=0; b=0; c=0; d=0;
for i in P:
	if i == "A":
		a = a+1;
	elif i == "O":
		b = b+1;
	elif i == "B":
		c = c+1;
	else:
		d = d+1;
print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" %(a,b,c,d))
```

27차시. [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.

```python
A = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
i = 0
while i < len(A):
    if A[i] < 80:
        A.pop(i)
    else:
        i = i +1
print (sum(A))
```

29차시. while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.(가운데정렬)

```python
for i in range(7,0,-2):
    print("{0: ^7}".format("*" * i))
```



30차시. 다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.

```python
i = int(input())
list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while i>0:
    a=i % 10
    list[a] +=1
    i = i //10
print("0 1 2 3 4 5 6 7 8 9")
print(*list)
```

31차시. for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오. (오른쪽정렬)

```python
j= 5
for i in range(1,6):
    print("{0}{1}".format((" " * (5-i)) ,("*" * i)))
```

32차시. 다음의 결과와 같이 10진수를 2진수로 변환하는 프로그램을 작성하십시오.

```python
a= int(input())
print(format(a, 'b'))
```



34차시. 다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고 그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.  

```python
a=str(input())

def Palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            return  print("입력하신 단어는 회문(Palindrome)이 아닙니다.")
        return print("입력하신 단어는 회문(Palindrome)입니다.")
   	
print(a)
Palindrome(a)
```



35차시. 가위바위보

```python
man1= input(); man2= input(); man_a = input(); man_b = input()
def winner(a,b):
    if a == "가위":
        if b== "가위":
            return print("비겼습니다!")
        elif b == "바위":
            return print("%s가 이겼습니다!"%man_b)
        else:
            return print("%s가 이겼습니다!"%man_a)
    elif a == "바위":
        if b== "바위":
            return print("비겼습니다!")
        elif b == "보":
            return print("%s가 이겼습니다!"%man_b)
        else:
            return print("%s가 이겼습니다!"%man_a)
    elif a == "보":
        if b== "보":
            return print("비겼습니다!")
        elif b == "가위":
            return print("%s가 이겼습니다!"%man_b)
        else:
            return print("%s가 이겼습니다!"%man_b)

winner(man_a,man_b)
```
