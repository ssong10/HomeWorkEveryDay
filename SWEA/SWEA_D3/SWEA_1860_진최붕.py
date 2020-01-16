for tc in range(int(input())):
    N, M, K = map(int,input().split())
    sonnim = list(map(int,input().split()))
    sonnim.sort()
    result = True
    for i in range(N):
        bung = (sonnim[i] // M) * K
        bung -= i+1
        if bung < 0:
            result = False
            break
    if result:
        print(f'#{tc+1} Possible')
    else:
        print(f'#{tc+1} Impossible')