for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = [0] * (N**2)
    dy, dx = [-1,1,0,0],[0,0,-1,1]
    for y in range(N):
        for x in range(N):
            i = arr[y][x]
            for d in range(4):
                yy,xx = y+dy[d],x+dx[d]
                if -1<yy<N and -1 < xx < N and arr[yy][xx] == i+1:
                    result[i-1] = 1
    for i in range(N**2-1,-1,-1):
        if result[i]:
            result[i] = result[i+1] + 1
        else:
            result[i] = 1
    ans = max(result)  
    for idx in range(N**2+1):
        if result[idx] == ans:
            print(f'#{tc+1} {idx+1} {result[idx]}')
            break