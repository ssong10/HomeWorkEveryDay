def find(n,d):
    if not chk[n-1]:
        chk[n-1] = True
        tmp.append([n,d])
        if n < 4 and arr[n-1][2] + arr[n][6] == 1:
            find(n+1,d* -1)
        if n > 1 and arr[n-1][6] + arr[n-2][2] == 1:
            find(n-1,d*-1)
    
arr = [list(map(int,input())) for _ in range(4)]
k = int(input())
spins = [list(map(int,input().split())) for _ in range(k)]
for spin in spins:
    chk = [False] * 4
    tmp = []
    find(spin[0],spin[1])
    for n,d in tmp:
        if d == 1:
            arr[n-1] = arr[n-1][-1:] + arr[n-1][:7]
        else:
            arr[n-1] = arr[n-1][1:8] + arr[n-1][:1]

result = 0
for idx in range(4):
    result += arr[idx][0] * (2**idx)
print(result)