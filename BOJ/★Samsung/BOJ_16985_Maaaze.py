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

def spin(pan,i):
    if not i:
        return pan
    tmp = [[0]*5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            tmp[x][4-y]= pan[y][x]
    spin(tmp,i-1)

def makeorder(panorder,n):
    if n ==5 :
        make([],panorder,0)
        return
    for i in range(5):
        if not used[i]:
            panorder[n] = i
            used[i] = 1
            makeorder(panorder,n+1)
            used[i] =0

def make(arr,panorder,i):
    if i == 4:
        print(arr)
        return
    for _ in range(3):
        arr.append(spin(maze[panorder[i]])

from collections import deque
maze = [[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]
panorder, used = [[] for _ in range(5)], [0] * 5
# makeorder(panorder,0)
make([],[0,1,2,3,4],0)
