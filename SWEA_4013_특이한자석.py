def next(n,r, d):
    if 0 < n and d != -1:
        if arr[n-1][2] + arr[n][6] == 1:
            spinlists.append([n-1,-r])
            next(n-1,-r, 1)
    if n < 3 and d != 1:
        if arr[n][2] + arr[n+1][6] == 1:
            spinlists.append([n+1,-r])
            next(n+1,-r,-1)

for tc in range(int(input())):
    K = int(input())
    arr = [list(map(int,input().split())) for _ in range(4)]
    spins = [list(map(int,input().split())) for _ in range(K)]
    for spin in spins:
        n, r = spin[0]-1,spin[1]
        spinlists = [[n,r]]
        next(n,r,0)
        for spinlist in spinlists:
            n,r = spinlist
            if r == 1:
                arr[n] = [arr[n][-1]] + arr[n][:-1]
            else:
                arr[n] = arr[n][1:] + [arr[n][0]]
    result = 0
    for i in range(4):
        if arr[i][0]:
            result += 2 ** (i)
    print(f'#{tc+1} {result}')