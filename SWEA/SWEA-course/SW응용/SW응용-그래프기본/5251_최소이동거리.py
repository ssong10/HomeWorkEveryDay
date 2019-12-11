for tc in range(int(input())):
    N, E = map(int,input().split())
    nodes = [list(map(int,input().split())) for _ in range(E)]
    V = [[] for _ in range(N+1)]
    for node in nodes:
        V[node[0]].append((node[1],node[2]))
        V[node[1]].append((node[0],node[2]))
    D = [0xffffff] * (N+1)
    D[0] = 0
    for i in range(N):
        for t in V[i]:
            D[t[0]] = min(D[t[0]], D[i]+t[1])
    print('#{} {}'.format(tc+1,D[-1]))