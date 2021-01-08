def DFS(s):
    visit[s] = True
    for n in V[s]:
        if not visit[n]:
            DFS(n)

N = int(input())
M = int(input())
visit = [False] * N
V = [[] for _ in range(N)]

for _ in range(M):
    v,w = map(int,input().split())
    V[v-1].append(w-1)
    V[w-1].append(v-1)
DFS(0)
print(sum(visit)-1)