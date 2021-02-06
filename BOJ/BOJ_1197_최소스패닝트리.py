def find():
  tmp = [0]
  while result < V:
    t = heapq.heappop(tmp)

import heapq
V, E = map(int,input().split())
tree = [[] for _ in range(V+1)]
for _ in range(E):
  a,b,c = map(int,input().split())
  tree[a-1].append([b-1,c])
  tree[b-1].append([a-1,c])
print(tree)
find(0)
# heapq.heappush(tmp,)