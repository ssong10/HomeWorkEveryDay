## 파이썬 프로그래밍 기초(2)

3차시.한 학생의 국어, 수학 점수를 튜플로 저장하고 이 튜플을 항목으로 갖는 리스트 객체가 있습니다. 이 때 첫 번째 학생은 (90, 80), 두 번째 학생은 (85, 75), 세 번째 학생은 (90, 100)의 점수를 갖습니다. 다음과 같이 결과를 만들기 위한 프로그램을 작성하십시오.

```python
stu1 = (90,80)
stu2 = (85,75)
stu3 = (90,100)
list = [stu1,stu2,stu3]

for stu in range(len(list)):
    a = int(list[stu][0]) + int(list[stu][1])
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2}입니다.".format(stu+1,a,a/2))
```

4차시. 리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오. 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

```python
vowels = 'aeiou'
sentence = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
for i in vowels:
	sentence = sentence.replace(i,'')
print(sentence)
```

5차시.   다음의 결과와 같이 구구단 2단부터 9단의 결과값 중에 3의 배수거나 7의 배수인 수를제외한 값을 리스트 객체 result 안에 각 단마다 리스트를 만들어 삽입하고 이를 출력하십시오.  

```python
total_list=[]
for i in range(2,10):
	if not (i % 3 == 0 or i % 7 == 0) :
		list = []
		for j in range(1,10):
			if not (j % 3==0 or j % 7 ==0):
				list.append(i*j)        
		total_list.append(list)
	else:
		list = []
		total_list.append(list)
        
print(total_list)
```

6차시. 리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.

```python
input() = 10
	10
	20
	30
	40
```

```python
a =[]
for i in range(5):
	a.append(int(input()))
b= sum(a) /len(a)
print(f"입력된 값 {a}의 평균은 {b}입니다.")
```



7차시. 다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오.

```python
a = int(input())
lst = []  
for i in range(1,a+1):
    if a % i == 0 :
        lst.append(i)
print(lst)
```

8차시.   다음의 결과와 같이 정수를 입력하면 리스트 내포를 이용해 약수 리스트를 출력하는 코드를 작성하십시오.  

```python
a = int(input())
lst = [i for i in range(1,a+1) if a % i == 0]
print(lst)
```

9차시.  [1, 3, 11, 15, 23, 28, 37, 52, 85, 100] 와 같은 리스트 객체가 주어졌을 때 다음의 결과를 출력하는 짝수만 항목으로 가지는 리스트 객체를 생성하는 코드를 작성하십시오.

```python
a = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
list = [i for i in a if i % 2 ==0]
print(list)
```

10차시. 리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.

```python
lst = []
lst.append(1)
lst.append(1)
[lst.append(lst[k-2]+lst[k-1]) for k in range(2,10)]
print(lst)
```

11차시. 리스트 내포 기능을 이용하여 1부터 20사이의 숫자 중 3의 배수가 아니거나 5의 배수가 아닌 숫자들의 제곱 값으로 구성된 리스트 객체를 출력하는 프로그램을 작성하십시오.

```python
lst = [x**2 for x in range(1,21) if x % 3 != 0 or x % 5 != 0] 
print(lst)
```

12차시.  사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환하는 프로그램을 작성하십시오.  예를 들어 123을 입력하면 1 + 2 + 3 = 6의 결과를 반환합니다.

```python
num = input()
sum = 0
for i in num:
    sum += int(i)
print(sum)
```

13차시. 

```
입력 받은 문자열 리스트를 가나다 순으로 따로 묶으려고 합니다.
다음과 같은 리스트가 주어졌을 때 결과처럼 가나다순(사전순)으로 따로 묶은 리스트가 출력되도록 리스트 내포를 이용한 프로그램을 작성하십시오.

dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))

inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다', '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그', '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']
```

```python
my_dict=[]
for i in range(len(dicBase)):
    lst = [x for x in inputWord if x >= dicBase[i][0] and x <=dicBase[i][1]]
    my_dict.append(lst)
print(my_dict)
```

14차시. 콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.

```
12, 34, 56, 78
```

```python
a = list(map(int,input().split(',')))
print(a)
b = tuple(a)
print(b)
```

15차시. 다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아 이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.

```
2, 3, 4, 5
```

```python
import math	
a = map(lambda x : '{0:.2f}'.format(2*int(x)*math.pi) ,input().split(', '))
print(*a, sep=', ')
```

16차시. 다음과 같이 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력하고, 이 리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력하는 프로그램을 작성하십시오.

```python
a= list(map(int,input().split(', ')))
# a = [3,5]  
lst_total = []
for i in range(a[0]):
    lst=[]
    for j in range(a[1]):
        lst.append(i*j)
    lst_total.append(list)
print(lst_total)
```

17차시. 단어를 콤마(,)로 구분해 입력하면 그 단어들을 사전순으로 정렬해 출력하는 프로그램을 작성하시시오.

```
python, hello, world, hi
```

```python
a = list(input().split(', '))
print(*sorted(a), sep = ", ")  
```

18차시 . 콤마(,)로 구분해 숫자를 입력하고, 입력된 숫자 중 홀수를 콤마(,)로 구분해 출력하는 리스트 내포 기능을 이용한 프로그램을 작성하십시오.

```
1, 2, 3, 4, 5
```

```python
a = input().split(', ')
b = list(map(int,a))
c= [i for i in b if i % 2==1]
print(', '.join(map(str,c)))
```

19차시. 주어진 튜플 (1,2,3,4,5,6,7,8,9,10)의 앞 항목 절반과 뒤 항목 절반을 출력하는 프로그램을 작성하십시오.

```python
a = (1,2,3,4,5,6,7,8,9,10)
print(a[0:5])
print(a[5:10])
```

20차시. 리스트 내포 기능을 이용해 [5, 6, 77, 45, 22, 12, 24]에서 짝수를 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.

```python
a= [5, 6, 77, 45, 22, 12, 24]
b = [i for i in a if i % 2 ==1]
print(b)
```

21차시.   리스트 내포 기능을 이용해 [12, 24, 35, 70, 88, 120, 155]에서 홀수번째 항목을 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.  

```python
a = [12, 24, 35, 70, 88, 120, 155]
b= [i for i in a if a.index(i) % 2 ==1]
print(b)
```

22차시.   항목 값으로는 0을 갖는 2\*3\*4 형태의 3차원 배열을 생성하는 리스트 내포 기능을 이용한 프로그램을 작성하십시오.  

```python
a = [0 for i in range(4)]
b = [a for i in range(3)]
c = [b for i in range(2)]
print(c)
```

23차시.   리스트 내포 기능을 이용해 [12, 24, 35, 70, 88, 120, 155]에서 첫번째, 다섯번째, 여섯번째 항목을 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.  

```python
a = [12, 24, 35, 70, 88, 120, 155]
b= [i for i in a if a.index(i) not in [0,4,5]]
print(b)
```

24차시.   두 개의 리스트 [1,3,6,78,35,55]와 [12,24,35,24,88,120,155]를 이용해 양쪽 리스트에 모두 있는 항목을 리스트로 반환하는 프로그램을 작성하십시오.  

```python
a = [1,3,6,78,35,55]
b = [12,24,35,24,88,120,155]
c= list(set(a) & set(b))
print(c)
```

25차시.   리스트의 항목 중 중복이 되는 항목을 제거하는 함수를 정의하고 이 함수를 이용해[12,24,35,24,88,120,155,88,120,155]에서 중복이 제거된 리스트를 출력하십시오.  

```python
a = [12,24,35,24,88,120,155,88,120,155]
print(list(set(a)))
```

27차시. 다음과 같이 등록된 학생의 이름을 출력하고, 이름을 입력하면 전화번호를 출력해주는 딕셔너리 객체를 이용한 전화번호부 프로그램을 작성하십시오.

```python
students = {'홍길동': '010-1111-1111','이순신': '010-1111-2222','강감찬': '010-1111-3333'}
print('아래 학생들의 전화번호를 조회할 수 있습니다.')
for i in students.keys():
    print(i)
a = input('전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.\n')
print(f'{a}의 전화번호는 {students[a]}입니다.')
```

### 28차시. ??

29차시.다음 두 딕셔너리 객체를 합쳐 중복된 메뉴가 없는 딕셔너리를 만들고 가격이 3000원 이상인 메뉴를 아래와 같이 출력하는 프로그렘을 작성하십시오. 중복된 메뉴의 가격이 다를 경우 딕셔너리 a의 가격을 사용하세요

```python
a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}
for menu,price in b.items():
    if menu not in a:
        a[menu] = price
a = {menu:price for menu, price in a.items() if price >=3000}
print(a)
```

30차시.   리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리 객체를 생성하는 코드를 작성해봅시다. 이 때 딕셔너리 내포 기능을 사용하며, 원소의 공백은 제거합니다  

```python
fruit = ['   apple    ','banana','  melon']
fruit_len = {}
for i in fruit:
    i = i.strip()
    fruit_len[i] = len(i)
print(fruit_len)
```

31차시.   다음과 같이 정수 N을 입력받아서 1부터 N까지의 정수를 키로 하고, 그 정수의 제곱을 값으로 하는 딕셔너리 객체를 만드는 코드를 작성하십시오.  

```python
a = int(input())
my_dict = {}
for i in range(1, a+1):
    my_dict[i] = i ** 2
print(my_dict)
```

32차시. 다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.

```python
a = input()
letter = 0
digit = 0
for i in a:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
print(f'LETTERS {letter}\nDIGITS {digit}')
```

33차시. 다음과 같이 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는 프로그램을 작성하십시오.

```python
a = input()
upper = 0
lower = 0
for i in a:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print(f'UPPER CASE {upper}\nLOWER CASE {lower}')
```

34차시. 

```
다음과 같은 기존의 맥주 가격을 5% 인상하려고 할 경우
딕셔너리 내포 기능을 이용한 코드를 작성하십시오.
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
```

```python
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
print(beer)
expensivebeer = {x:y * 1.05 for x,y in beer.items()}
print(expensivebeer)
```

35차시. 다음의 결과와 같이 입력된 문자열의 문자 빈도수를 구하는 프로그램을 작성하십시오.

```python
a = input()
for i in set(a):
    print(f'{i},{a.count(i)}')
```

37차시. 다음의 결과와 같이 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.

```python
a = input()
result = '입력하신 단어는 회문(Palindrome)입니다.'
for i in range(len(a)//2):
    if a[i] != a[-i-1]:
        result = '입력하신 단어는 회문(Palindrome)이 아닙니다'
        break
print(result)
```

38차시. 다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.

```python
a = input().split(' ')
for i in reversed(a):
    print(i,end=' ')
```

39차시. 다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로 구분하는 프로그램을 작성하십시오.

```python
a,b = input().split('://')
c,d = b.split('/')
print(f'protocol: {a}')
print(f'host: {c}')
print(f'others: {d}')
```

# 40차시. 다음의 결과와 같이 여러 문장을 입력받아 대문자로 변환해 출력하는 프로그램을 작성합니다.

```
hjkk
```



41차시.   사용자가 입력한 문장에서 공백을 이용해 단어들을 구분하고, 중복된 단어없이 단어를 콤마(,)로 구분해 사전순으로 출력하는 프로그램을 작성하십시오.  

```python
a = input().split(' ')
a = sorted(set(a))
print(*a,sep=',')
```

42차시. 다음 결과와 같이 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램을 작성하십시오.

```python
# H1e2l3l4o5w6o7r8l9d
a = input()
for i in range(len(a)//2+1):
    print(a[2*i],end='')
```

44차시. 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.  이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

```python 
student = list(map(int,input().split(', ')))
print(f'국어, 영어, 수학의 총점: {sum(student)}')
```

