def move(y,x,n,stty,sttx):
    global flag,result
    for d in range(4):
        yy, xx = y+dy[d], x+dx[d]
        if -1<yy<N and -1<xx<N and arr[y][x]+1 == arr[yy][xx]:
            move(yy,xx,n+1,stty,sttx)
            flag=True
    if not flag:
        if n > result[1]:
            result[1] = n
            result[0] = arr[stty][sttx]
        elif n ==result[1]:
            result[0] =min(result[0], arr[stty][sttx])

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dy,dx = [-1,1,0,0],[0,0,-1,1]
    result = [0, 0]
    for y in range(N):
        for x in range(N):
            flag = False
            move(y,x,1,y,x)
    print('#{}'.format(tc+1),*result)