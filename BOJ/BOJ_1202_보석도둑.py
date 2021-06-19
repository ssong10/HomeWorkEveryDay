import heapq
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
jews = []
for _ in range(N):
  heapq.heappush(jews, list(map(int,input().split())))
q = sorted([int(input()) for _ in range(K)])
result = 0
candi = []
for b in q:
  while jews and b >= jews[0][0]:
    m,v = heapq.heappop(jews)
    heapq.heappush(candi,-v)
  if candi:
    result -= heapq.heappop(candi)
print(result)