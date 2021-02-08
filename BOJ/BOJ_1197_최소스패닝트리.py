import heapq
import sys
input = sys.stdin.readline
def find(tmp):
  global result
  while sum(visit) < V:
    t = heapq.heappop(tmp)
    v,n = t
    if not visit[n]:
      visit[n] = True
      result += v
      answer[n] =  min(answer[n], n)
      for vv, nn in tree[n]:
        if not visit[nn] and answer[nn] > vv:
          answer[nn] = vv
          heapq.heappush(tmp,(vv,nn))

V, E = map(int,input().split())
tree = [[] for _ in range(V+1)]
answer = [10**6] * V
for _ in range(E):
  a,b,c = map(int,input().split())
  tree[a-1].append((c,b-1))
  tree[b-1].append((c,a-1))
visit = [False] * V
visit[0] = True
result = 0
tmp = []
for t in tree[0]:
  heapq.heappush(tmp,t)
find(tmp)

print(result)