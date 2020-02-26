from collections import deque
dy, dx = [-1,1,0,0], [0,0,-1,1]
def watergo(waters, start, t):
    global result
    if not result:
        for _ in range(len(waters)):
            y,x = waters.popleft()
            for d in range(4):
                yy, xx = y+dy[d], x+dx[d]
                if -1 <yy< R and -1 <xx < C:
                    if arr[yy][xx] == '.' or arr[yy][xx] == 'S':
                        waters.append([yy,xx])
                        arr[yy][xx] = '*'
        for _ in range(len(start)):
            y,x = start.popleft()
            for d in range(4):
                yy, xx = y+dy[d], x+dx[d]
                if -1<yy<R and -1 < xx < C and arr[yy][xx] != '*' and arr[yy][xx] != 'X':
                    if arr[yy][xx] == 'D':
                        result = t
                        return
                    elif arr[yy][xx] != 'S':
                        arr[yy][xx] = 'S'
                        start.append([yy,xx])
        if start:
            watergo(waters,start,t+1)               


R, C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
waters = deque([])
for y in range(R):
    for x in range(C):
        if arr[y][x] == '*':
            waters.append([y,x])
        elif arr[y][x] == 'S':
            start = deque([[y,x]])
result = False
watergo(waters,start,1)

if result:
    print(result)
else:
    print('KAKTUS')