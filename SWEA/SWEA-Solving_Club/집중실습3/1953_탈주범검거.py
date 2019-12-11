dy,dx = [-1,0,1,0],[0,1,0,-1]
def time(v,n):
    visited[v] = 1
    if n:
        for u in cango[v]:
            if not visited[u]:
                time(u,n-1)

for tc in range(int(input())):
    N,M,R,C,L = map(int,input().split()) # 가,세,맨홀y,x, 시간
    arr = [list(map(int,input().split())) for _ in range(N)] 
    tunnels = []
    for y in range(N):
        for x in range(M):
            if arr[y][x]:
                tunnels.append([y,x])
    cango = []
    for tunnel in tunnels:
        [y,x] = tunnel
        dd = []
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
        tmp = []
        for d in dd:
            yy,xx = tunnel[0]+dy[d], tunnel[1]+dx[d]
            if -1< yy < N and -1 < xx <M:
                if d == 0:
                    if arr[yy][xx] in [1,2,5,6]:
                        tmp.append(tunnels.index([yy,xx]))
                if d == 1:
                    if arr[yy][xx] in [1,3,6,7]:
                        tmp.append(tunnels.index([yy,xx]))
                if d == 2:
                    if arr[yy][xx] in [1,2,4,7]:
                        tmp.append(tunnels.index([yy,xx]))
                if d == 3:
                    if arr[yy][xx] in [1,3,4,5]:
                        tmp.append(tunnels.index([yy,xx]))
        cango.append(tmp)
    print(cango)
    visited = [0]* len(tunnels)
    time(tunnels.index([R,C]),L-1)
    print(visited)
    print(f'#{tc+1} {sum(visited)}')    