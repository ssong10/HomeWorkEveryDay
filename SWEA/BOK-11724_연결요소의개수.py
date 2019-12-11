import sys
input=sys.stdin.readline

def DFS():
    while tmp:
        for _ in range(len(tmp)):
            j = tmp.pop(0)
            for i in V[j]:
                if visit[i] == False:
                    tmp.append(i)
                    visit[i] = True

N,M  = map(int,input().split())
visit = [False] * (N+1)
V = [[] for _ in range(N+1)]
for _ in range(M):
    v,u = map(int,input().split())
    V[v].append(u)
    V[u].append(v)
result = 0
for i in range(1,len(visit)):
    if visit[i] == False:
        tmp = [i]
        visit[i] = True
        result+=1
        DFS()
print(result)