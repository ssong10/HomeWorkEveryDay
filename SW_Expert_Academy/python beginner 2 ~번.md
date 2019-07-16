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

