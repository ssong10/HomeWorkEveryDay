K = int(input())
W,H = map(int,input().split())
arr =  [list(map(int,input().split())) for _ in range(H)]
def horse(y,x):
    result = True
    hy, hx = [2,2,1,1,-1,-1,-2,-2],[-1,1,-2,2,-2,2,-1,1]
    for d in range(8):
        yy,xx = y+hy[d],x+hx[d]
        if -1<yy<H and -1<xx<W and not arr[yy][xx]:
            result =  False
            break
