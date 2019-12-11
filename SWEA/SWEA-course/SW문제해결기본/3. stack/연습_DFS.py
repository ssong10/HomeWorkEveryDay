# import sys; sys.stdin = open('DFS_input.txt','r')

def DFS(v):
    # 시작점에 방문하고, 스택에 push
    S =[]
    visit[v] = True; print(v, end=' ')
    S.append(v)
    while S:    # 빈스택이 아닐동안 반복
        for w in G[v]:
            if not visit[w]:         # v의 방문하지 않은 인접정점 w를 찾아서
                visit[w] = True; print(w, end=' ')       # w를 방문하고, v를 스택에 push
                S.append(v)
                v = w         # v를 w로 설정
                break
        else:                # 인접정점이 없다면, 스택에서 pop()해서
            v = S.pop()      # v로 설정

def DFS1(v):
    visit[v] = True; print(v, end=' ')
    for w in G[v]:
        if not visit[w]:
            DFS1(w)

V, E = map(int, input().split())  # 정점수, 간선수
G = [[] for _ in range(V+1)]     # 1~ V 까지
visit = [False] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)  # 무향그래프

for i in range(1,V+1):
    print(i, ' -->', G[i])

# DFS(1)
DFS1(1)