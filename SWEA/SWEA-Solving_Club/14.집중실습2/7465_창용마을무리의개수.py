def find(n):
    for i in know[n]:
        if not used[i]:
            used[i] = 1
            find(i)

for tc in range(int(input())):
    N,M = map(int,input().split())
    know = [[] for _ in range(N+1)]
    for _ in range(M):
        i,j = map(int,input().split())
        know[i].append(j)
        know[j].append(i)
    used=[0]*(N+1)
    result =0
    for i in range(1,N+1):
        if not used[i]:
            used[i] = 1
            find(i)
            result += 1
    print('#{} {}'.format(tc+1,result))