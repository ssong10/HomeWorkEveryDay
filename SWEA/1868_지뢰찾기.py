from collections import deque

def chk(tmplist):
    global result
    while tmplist:
        for _ in range(len(tmplist)):
            [y,x] = tmplist.popleft()
            if arr[y][x] != '*':
                arr[y][x] = '*'
            for d in range(8):
                yy,xx = y+dy[d], x+dx[d]
                if -1< yy <N and -1< xx <N and type(arr[yy][xx]) ==int and arr[yy][xx] >= 0:
                    if not arr[yy][xx]:
                        tmplist.append([yy,xx])
                    arr[yy][xx] = '*'
                    result -= 1

for tc in range(int(input())):
    N =int(input())
    arr = [list(input()) for _ in range(N)]
    dy,dx = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]
    result = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] =='.':
                result += 1
                tmp = 0
                for d in range(8):
                    yy,xx = y+dy[d],x+dx[d]
                    if -1<yy<N and-1<xx<N and arr[yy][xx]=='*':
                        tmp += 1
                arr[y][x] = tmp
    for y in range(N):
        for x in range(N):
            if not arr[y][x]:
                chk(deque([[y,x]]))
    print('#{} {}'.format(tc+1,result))