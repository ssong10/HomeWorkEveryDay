for tc in range(int(input())):
    M,N = map(int,input().split())
    arr = []
    for _ in range(M):
        arr.append(list(map(int,input().split())))
    result = 0
    for y in range(M+1-N):
        for x in range(M+1-N):
            S = 0
            for j in range(N):
                for i in range(N):
                    S += arr[y+j][x+i]
            result = max(S,result)
    print(f'#{tc+1} {result}')