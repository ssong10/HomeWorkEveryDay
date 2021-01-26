import sys
input = sys.stdin.readline

def DFS(i,cnt):
  global flag
  if cnt == 4:
    flag = True
  if not flag:
    for j in friends[i]:
      if not visit[j]:
        visit[j] = True
        DFS(j,cnt+1)
        visit[j] = False

N,M = map(int,input().split())
friends = [[] for _ in range(N)]
for _ in range(M):
  v,w = map(int,input().split())
  friends[v].append(w)
  friends[w].append(v)
flag = False
for i in range(N):
  if flag:
    break
  visit = [False]*N
  visit[i] = True
  DFS(i,0)
print(1 if flag else 0)