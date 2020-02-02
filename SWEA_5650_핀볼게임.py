dy, dx = [1,0,-1,0], [0,-1,0,1]
def go(y,x,d):
    yy, xx = y+dy[d], x+dx[d]
    if not arr[yy][xx]:
        go(yy,xx,d)
    elif arr[yy][xx] == 1:
        if d == 0:
            go(yy,xx+1,3)
        elif d == 1:
            go(yy-1,xx,2)
        elif d == 2:
            go(y,x,0)
        else:
            go(y,x,1)
    elif arr[yy][xx] == 2:
        if d == 0 :
            go(y,x,2)
        elif d == 1:
            go(yy+1,xx,0)
        elif d == 2:
            go(yy,xx+1,3)
        else:
            go(y,x,1)
    elif arr[yy][xx] == 3:
        if d == 0 :
            go(y,x,2)
        elif d == 1:
            go(y,x,3)
        elif d == 2:
            go(yy,xx-1,1)
        elif d == 3:
            go(yy-1,xx,0)
    elif arr[yy][xx] == 4:
        if d == 0:
            go(yy,xx-1,2)
        elif d == 1:
            go(y,x,3)
        elif d == 2:
            go(y,x,0)
        else:
            go(yy-1,xx,2)
    elif arr[yy][xx] == 5:
        if d == 0 :
            go(y,x,2)
        elif d == 1:
            go(y,x,3)
        elif d == 2:
            go(y,x,0)
        else:
            go(y,x,1)

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    print(result)
    for y in range(N):
        for x in range(N):
            if not arr[y][x]:
                goal = [y,x]
                for d in range(4):
                    go(y,x,d)