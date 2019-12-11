from collections import deque
def BFS(s):
    D = [0] * (V+1)
    visit = [False] * (V+1)
    Q = deque()
    Q.append(s)
    visit[s] =True
    D[s]=0

    while Q:
        u = Q.popleft()
        for v,w in G[u]:
            if D[v] > D[u] + w:
                Q.append(v)
                D[v] = D[u] + w

V,E = map(int,input().split())
G = [[] for _ in range(V)]
for _ in range(E):
    u,v,w,=map(int,input().split())
    G[u].append((v,w))
    G[v].append((u,w))