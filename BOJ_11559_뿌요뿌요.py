dy, dx = [-1,1,0,0],[0,0,-1,1]
def made(y,x):
    arr[y][x] = '.'
    for d in range(4):
        yy, xx = y+dy[d],x+dx[d]
        if -1<yy<12 and -1 <xx < 6 and arr[yy][xx] == val:
            made(yy,xx)            

def bomb(arr):
    bomblist = []
    new_arr = [['.'] * 6 for _ in range(12)]
    print(new_arr)
    for y in range(12):
        for x in range(6):
            if arr[y][x] != '.':
                val = arr[y][x]
                made(y,x)
    if bomblist:
        bomb(new_arr)

arr = [list(input()) for _ in range(12)]
result = 0
bomb(arr)