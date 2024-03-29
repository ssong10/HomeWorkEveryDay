import heapq
import sys
input = sys.stdin.readline
MAX = 10 ** 6
def find(start):
  answer = [MAX] * N
  visit = [False] * N
  visit[start] = True
  tmp = []
  for t in tree[start]:
    heapq.heappush(tmp,t)
  while tmp and sum(visit) < N:
    t = heapq.heappop(tmp)
    v,n = t
    if not visit[n]:
      visit[n] = True
      answer[n] =  min(answer[n], v)
      for vv, nn in tree[n]:
        if not visit[nn] and answer[nn] > v+vv:
          answer[nn] = v+vv
          heapq.heappush(tmp,(v+vv,nn))
  return answer
N, E = map(int,input().split())
tree = [[] for _ in range(N+1)]
for _ in range(E):
  a,b,c = map(int,input().split())
  tree[a-1].append((c,b-1))
  tree[b-1].append((c,a-1))
v1,v2 = map(int,input().split())
nodes = find(v1-1)
graph1 = find(0)
graph2 = find(N-1)
result = MAX
if v1 == 1 and v2 == N:
  result = min(result,nodes[N-1])
if graph1[v1-1] != MAX and graph2[v2-1] != MAX:
  tmp = graph1[v1-1] + graph2[v2-1] + nodes[v2-1]
  result = min(tmp,result)
if graph2[v1-1] != MAX and graph1[v2-1] != MAX:
  tmp = graph2[v1-1] + graph1[v2-1] + nodes[v2-1]
  result = min(tmp,result)
if result == MAX:
  print(-1)
else:
  print(result)