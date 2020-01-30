from collections import deque
dy,dx = [-1,0,1,0],[0,1,0,-1]
def go(tmp,n):
    while tmp:
        if n:
            for _ in range(len(tmp)):
                y,x = tmp.popleft()
                visit[y][x] = 1
                if n > 1:
                    if arr[y][x] == 1:
                        dd = [0,1,2,3]
                    elif arr[y][x] == 2:
                        dd = [0,2]
                    elif arr[y][x] ==3:
                        dd = [1,3]
                    elif arr[y][x] == 4:
                        dd = [0,1]
                    elif arr[y][x] == 5:
                        dd = [1,2]
                    elif arr[y][x] == 6:
                        dd = [2,3]
                    elif arr[y][x] == 7:
                        dd  = [0,3]
                    for d in dd:
                        yy,xx = y+dy[d], x+dx[d]
                        if -1< yy < N and -1 < xx <M and arr[yy][xx] and not visit[yy][xx]:
                            if d == 0:
                                if arr[yy][xx] in [1,2,5,6]:
                                    tmp.append([yy,xx])
                            if d == 1:
                                if arr[yy][xx] in [1,3,6,7]:
                                    tmp.append([yy,xx])
                            if d == 2:
                                if arr[yy][xx] in [1,2,4,7]:
                                    tmp.append([yy,xx])
                            if d == 3:
                                if arr[yy][xx] in [1,3,4,5]:
                                    tmp.append([yy,xx])
            n -= 1
        else:
            return
        
for tc in range(int(input())):
    N,M,R,C,L = map(int,input().split()) # 가,세,맨홀y,x, 시간
    arr = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    tmp = deque([[R,C]])
    go(tmp,L)
    print(f'#{tc+1} {sum(map(sum,visit))}')
