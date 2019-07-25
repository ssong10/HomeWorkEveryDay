##  WorkShop 2

### 1. n \* m 사각형 출력(반복문 이용)

```python
n=5
m=9
for j in range(m):
    for i in range(n):
        print('*',end='')
    print('')
```

### 2. 딕셔너리 점수의 평균 점수 출력.

```python
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
sum(student.values())/len(student)
```

### 3. 혈액형 종류별 인원 딕셔너리 출력

```python
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
blood_dic = {}
for i in blood_types:
    if i not in blood_dic.keys():
        blood_dic[i] = 1
    else:
        blood_dic[i] += 1
print(blood_dic)
```

