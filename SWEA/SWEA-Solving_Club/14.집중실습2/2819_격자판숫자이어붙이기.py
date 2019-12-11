def move(y,x,num,n):
    if n ==6:
        result.add(num)
    else:
        for d in range(4):
            yy,xx = y+dy[d],x+dx[d]
            if -1<yy<4 and -1<xx<4:
                move(yy,xx,num+arr[yy][xx],n+1)

for tc in range(int(input())):
    arr = [list(input().split()) for _ in range(4)]
    result = set()
    dy,dx = [-1,1,0,0],[0,0,-21e1,1]
    for y in range(4):
        for x in range(4):
            move(y,x,arr[y][x],0)
    print('#{} {}'.format(tc+1,len(result)))