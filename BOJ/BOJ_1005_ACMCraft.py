import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def find(a):
  global cost
  if cost[a] > -1:
    return cost[a]
  else:
    tmp = 0
    for i in pre[a]:
      tmp = max(find(i),tmp)
    cost[a] = tmp + D[a]
    return cost[a]
for _ in range(int(input())):
  N,K = map(int,input().split())
  D = list(map(int,input().split()))
  pre = [[] for _ in range(N)]
  for _ in range(K):
    a,b = map(int,input().split())
    pre[b-1].append(a-1)
  cost = [-1] * N
  W = int(input())
  find(W-1)
  print(cost[W-1])