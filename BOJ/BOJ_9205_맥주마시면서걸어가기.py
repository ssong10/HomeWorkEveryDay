from collections import deque

t = int(input())

def BFS(q):
  while q:
    tmp = q.popleft()
    for nt in V[tmp]:
      if not visited[nt]:
        q.append(nt)
        visited[nt] = True
for _ in range(t):
  n = int(input())
  arr = [list(map(int,input().split())) for _ in range(n+2)]
  V = [[] for _ in range(n+2)]
  for i in range(n+1):
    for j in range(i+1,n+2):
      diff = abs(arr[i][0]-arr[j][0]) + abs(arr[i][1]-arr[j][1])
      if diff <= 1000:
        V[i].append(j)
        V[j].append(i)
  visited = [True] + [False]* (n+1)
  BFS(deque([0]))
  if visited[-1]:
    print('happy')
  else:
    print('sad')