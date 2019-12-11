def chk(idx):
    for num in V[idx]:
        if not visit[num]:
            visit[num] = 1
            chk(num)

for tc in range(int(input())):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    V = [[] for _ in range(N+1)]
    visit = [0] * (N+1)
    for i in range(0,M):
        u,v = arr[i*2],arr[i*2+1]
        V[u].append(v)
        V[v].append(u)
    result = 0
    for idx in range(1,N+1):
        if not visit[idx]:
            visit[idx] = 1
            chk(idx)
            result += 1
    print('#{} {}'.format(tc+1,result))