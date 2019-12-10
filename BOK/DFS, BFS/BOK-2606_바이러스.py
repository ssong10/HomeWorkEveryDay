def DFS(v):
    visit[v]=True
    result.append(v)
    for i in V[v]:
        if not visit[i]:
            DFS(i)

N = int(input())
M = int(input())

V = [[] for _ in range(N+1)]
visit = [False] * (N+1)
for _ in range(M):
    u,v = map(int,input().split())
    V[v].append(u)
    V[u].append(v)
result = []
DFS(1)
print(len(result)-1)

