from collections import deque
def BFS(s):
    D = [0xffffff] * (V+1)
    visit = [False] * (V+1)
    D[s] = 0
    cnt = V
    while cnt:
        for v,w in G[u]:
            if D[v] > D[u]+ w:
                D[v] += D[u] + w
        cnt -= 1