import heapq
import sys
input = sys.stdin.readline

def find(start,end):
  visit = [False] * N
  visit[start] = True
  tmp = []
  for t in tree[start]:
    heapq.heappush(tmp,t)
  while heapq:
    t = heapq.heappop(tmp)
    v,n = t
    if n == end:
      return
    if not visit[n]:
      visit[n] = True
      answer[n] =  min(answer[n], n)
      for vv, nn in tree[n]:
        if not visit[nn] and answer[nn] > vv:
          answer[nn] = vv
          heapq.heappush(tmp,(vv,nn))

N, E = map(int,input().split())
tree = [[] for _ in range(N+1)]
answer = [10**6] * N
for _ in range(E):
  a,b,c = map(int,input().split())
  tree[a-1].append((c,b-1))
  tree[b-1].append((c,a-1))
v1,v2 = map(int,input().split())
print(tree)
find(0,v1)
find(0,v2)