dz,dy,dx = [-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,-1,1]

def go(tmp):
    visit = [[[0]*5 for _ in range(5)] for _ in range(5)]
    while tmp:
        for _ in range(len(tmp)):
            z,y,x = tmp.popleft()
            for d in range(6):
                zz ,yy, xx = z+dz[d] , y+dy[d] , x+dx[d]
                if -1 < zz < 5 and -1 <yy< 5 and -1 < xx< 5:
                    if arr[zz][yy][xx] and not visit[zz][yy][xx]:
                        visit[zz][yy][xx] = 1
                        tmp.append((zz,yy,xx))

def make(pan,n):
    if n ==5 :
        print(pan)
        return
    for i in range(5):
        if not used[i]:
            pan[n] = i
            used[i] = 1
            make(pan,n+1)
            used[i] =0

from collections import deque
maze = [[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]
pan, used = [[] for _ in range(5)], [0] * 5
make(pan,0)