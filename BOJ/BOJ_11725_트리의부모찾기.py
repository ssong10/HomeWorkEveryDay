import sys
input = sys.stdin.readline
def find(q):
  while q:
    tmp = q.pop()
    for i in V[tmp]:
      if not checked[i-1]:
        checked[i-1] = tmp
        q.append(i)

N = int(input())
V = [[] for _ in range(N+1)]
checked = [True] + [False]* (N-1)
for _ in range(N-1):
  v,w = map(int,input().split())
  V[v].append(w)
  V[w].append(v)
find([1])
for i in range(N-1):
  print(checked[i+1])