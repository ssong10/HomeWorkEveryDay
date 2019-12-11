for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    p = [x for x in range(N+1)]

    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]
    ans = N
    for _ in range(M):
        u,v = map(int,input().split())
        a = find_set(u); b = find_set(v)
        if a != b:
            p[b] = ans - 1
    print('#{} {}'.format(tc,ans))