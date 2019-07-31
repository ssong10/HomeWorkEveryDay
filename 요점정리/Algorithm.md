# Algorithm

## 기본잡기

* 배열, 리스트
* 반복문 (for ,while) , 분기문 (if -else)
* 수식(연산자 + 피연산자)
* function, Def
* 완전 탐색
  * 백트래킹 - BFS, DFS

> 코딩을 처음하고 알고리즘을 배우면서 기본적으로 리스트의 어트리뷰트나 메소드 등 잡기술을 사용하지 말고 어렵게 접근해서 답을 찾아보자 

## 정보

* 파이썬
  * 인터프리터 언어
  * 컴파일러
  * 메모리가 많이 사용됨.
  * c와 다르게 변수 선언이 필요가 없음

## 좋은 알고리즘

* 정확성
* 작업량
* 메모리 사용량 - 언어마다 기본적으로 사용량이 다르다.
  * Time complexity : 실행되는 명령문의 개수 (Big-Oh Notation)
* 단순성
* 최적성

 

# APS(algorithm problem solving)

## 기본

### 배열(List)

#### 정렬

* 버블정렬(Bubble Sort)

  > 인접한 두개의 원소를 비교하며 자리를 계속 교환하는 방식

  ```python
  a = [14,5,24,18,7,20,13,3,19]
  n =len(a)
  for i in range(1,n-1):
      for j in range(n-i):
          if a[j] >a[j+1]:
              a[j],a[j+1] =a[j+1],a[j]
  print(a)
  ```

* 카운팅 정렬(Counting Sort)

  > 항목의 순서를 결정하기 위해 집합에 각 항목이 몇개씩 있나 세는 작업을 하여 선형 시간에 정렬하는 효율적인 알고리즘

  ```python
  arr = [0,4,1,3,1,2,4,1]
  
  cnt = [0] * 5 # 0 ~ 4 까지의 5개의 빈칸을 만들다
  
  for val in arr: # cnt리스트에 해당숫자의 카운트만큼 저장
      cnt[val] += 1
  
  print(cnt)
  result =[]
  for i in range(len(cnt)):
      for j in range(cnt[i]):
          result.append(i)
  print(result)
  ```

- 선택 정렬(Selection Sort)
- 퀵 정렬(Quick Sort)
- 삽입 정렬(Insertion Sort)
- 병합 정렬(Merge Sort)

### 최적화

#### 탐욕(Greedy) 알고리즘

> 탐욕 알고리즘은 최적해를 구하는데 사용되는 근시안적인 방법





### 문자열



###  Stack



### Queue



### 연결리스트



### Tree



## 응용

### 그래프
### 완전탐색 (완전검색?)

* 문제의 해법으로 생각 할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
* Brute-force 혹은 generate-and-test 기법이라고도 불리운다.
* 경우의 수가 상대적으로 작을 때 유용하다.

### 분할정복
### 백트래킹

> 탐색기반의 가지치기방식

### 정보

* 파이썬
  * 인터프리터 언어
  * 컴파일러
  * 메모리가 많이 사용됨.
  * c와 다르게 변수 선언이 필요가 없음