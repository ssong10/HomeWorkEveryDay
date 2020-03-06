dy, dx = [-1,1,0,0],[0,0,-1,1]
def made(y,x,val,):
    global cnt
    arr[y][x] = '.'
    bomblist.append([y,x])
    cnt += 1
    for d in range(4):
        yy, xx = y+dy[d],x+dx[d]
        if -1<yy<12 and -1 <xx < 6 and arr[yy][xx] == val:
            made(yy,xx,val)     

arr = [list(input()) for _ in range(12)]
result = 0
bomb = True
new_arr = [['.'] * 6 for _ in range(12)]
for y in range(12):
    for x in range(6):
        if arr[y][x] != '.':
            cnt = 0
            bomblist = []
            made(y,x,arr[y][x])
            if cnt > 3:
                bomb = True
            
arr = new_arr
print(new_arr)