def pick(n,hi):
    global result
    if hi >=  B:
        result = min(result,hi)
    else:
        for i in range(n,N):
            if not used[i]:
                used[i] = 1
                pick(i,hi+hlist[i])
                used[i] = 0

for tc in range(int(input())):
    N,B = map(int,input().split())
    hlist = list(map(int,input().split()))
    used = [0]*N
    result = 10**6
    pick(0,0)
    print('#{} {}'.format(tc+1,result-B))