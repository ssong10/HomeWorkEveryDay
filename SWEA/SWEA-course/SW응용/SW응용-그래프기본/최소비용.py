from collections import deque

def BFS(tmp):
    while tmp:
        for _ in range(len(tmp)):
            [y,x] = tmp.popleft()
            for d in range(4):
                yy,xx = y+dy[d],x+dx[d]
                if -1<yy<N and -1 <xx< N:
                    hight = 1
                    if arr[yy][xx] > arr[y][x]:
                        hight += arr[yy][xx]-arr[y][x]
                    nn = arrmin[y][x]+hight
                    if arrmin[yy][xx] > nn:
                        tmp.append([yy,xx])
                        arrmin[yy][xx] = nn

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arrmin = [[0xffffff]*N for _ in range(N)]
    arrmin[0][0] = 0
    tmp = deque([[0,0]])
    dy,dx = [-1,1,0,0],[0,0,-1,1]
    BFS(tmp)
    print('#{} {}'.format(tc+1,arrmin[N-1][N-1]))