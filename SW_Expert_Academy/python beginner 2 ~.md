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

