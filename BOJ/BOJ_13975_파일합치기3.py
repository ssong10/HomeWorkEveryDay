import heapq
N = int(input())
for _ in range(N):
  answer = 0
  M = int(input())
  arr = list(map(int,input().split()))
  heapq.heapify(arr)
  while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    heapq.heappush(arr,a+b)
    answer += a+b
  print(answer)
