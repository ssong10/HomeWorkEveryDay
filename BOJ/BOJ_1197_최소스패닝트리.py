def find(tmp):
  for _ in range(3):
    print(sum(visit))
    t = heapq.heappop(tmp)
    print(t)
    [n,v] = t
    visit[n-1] = True
    answer[n-1] =  min(answer[n-1], n)
    for next_node in tree[n]:
      if next_node[0] != n:
        heapq.heappush(tmp,next_node)

import heapq
V, E = map(int,input().split())
tree = [[] for _ in range(V+1)]
answer = [10**6] * V
for _ in range(E):
  a,b,c = map(int,input().split())
  tree[a-1].append([b-1,c])
  tree[b-1].append([a-1,c])
visit = [False] * V
visit[0] = True
tmp = []
for t in tree[0]:
  heapq.heappush(tmp,t)
find(tmp)
