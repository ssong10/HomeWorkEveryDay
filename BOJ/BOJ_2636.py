from collections import deque

dy,dx = [-1,1,0,0],[0,0,-1,1]
def melt():
    global result
    q = deque([(0,0)])
    meltlist = set([])
    visit = [[False] * M for _ in range(N)]
    while q:
        for _ in range(len(q)):
            (y,x) = q.popleft()
            for d in range(4):
                yy,xx = y+dy[d] , x+dx[d]
                if -1<yy<N and -1<xx <M and not visit[yy][xx]:
                    visit[yy][xx] = True
                    if arr[yy][xx]:
                        meltlist.add((yy,xx))
                    else:
                        q.append((yy,xx))
    
    for y,x in meltlist:
        arr[y][x] = 0
    return len(meltlist)
    
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
result = [1000]
time = 0
while result[-1]:
    result.append(melt())
    time += 1
print(time-1)
print(result[-2])