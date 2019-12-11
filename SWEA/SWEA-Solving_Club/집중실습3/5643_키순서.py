def longer(long):
    for ll in long:
        if not chk[ll]:
            chk[ll] = 1
            longer(v[ll][0])

def shorter(short):
    for ss in short:
        if not chk[ss]:
            chk[ss] = 1
            shorter(v[ss][1])

for tc in range(int(input())):
    result = 0
    N,M = int(input()),int(input())
    v = [[[],[]] for _ in range(N+1)]
    for i in range(M):
        a,b = map(int,input().split())
        v[a][0].append(b)
        v[b][1].append(a)
    for i in range(N+1):
        chk = [0] * (N+1)
        longer(v[i][0])
        shorter(v[i][1])
        if sum(chk) == N-1:
            result += 1
    print(f'#{tc+1} {result}')