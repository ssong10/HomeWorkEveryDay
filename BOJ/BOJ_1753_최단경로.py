import sys
import heapq
input = sys.stdin.readline
def go(tmp):
  while tmp:
      v,t = heapq.heappop(tmp)
      for (i,n) in W[t]:
        if ans[t]+n < ans[i]:
          ans[i] = ans[t] + n
          heapq.heappush(tmp,(ans[i],i))

V, E = map(int,input().split())
s = int(input())
INF = 10**6
W = [[] for _ in range(V+1)]
ans = [INF] * (V+1)
ans[s] = 0
for _ in range(E):
  v,w,n = map(int,input().split())
  W[v].append((w,n))
Q = []
heapq.heappush(Q,(0,s))
go(Q)
for i in range(1,V+1):
  if ans[i] == INF:
    print('INF')
  else:
    print(ans[i])