def chk(i):
    global tmp
    for v in visit[i]:
        if not used[v]:
            used[v] = 1
            chk(v)

for tc in range(int(input())):
    N,M = map(int,input().split())
    visit = [[] for _ in range(N+1)]
    for _ in range(M):
        v,w = map(int,input().split())
        visit[v].append(w)
        visit[w].append(v)
    result = 1
    for i in range(1,N+1):
        used = [1] + [0]*N
        used[i] = 1
        tmp = 1
        chk(i)
        result = max(tmp,result)
    print('#{} {}'.format(tc+1,result))