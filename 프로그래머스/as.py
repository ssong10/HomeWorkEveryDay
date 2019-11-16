from collections import deque

dy,dx = [-1,1,0,0], [0,0,-1,1]
def bfs(Q,tmp,height,land,visited):
    while Q:
        (y,x) = Q.popleft()
        visited[y][x] = 1
        tmp.add((y,x))
        for d in range(4):
            yy,xx = y+dy[d],x+dx[d]
            if -1 < yy < len(land) and -1 < xx < len(land) and not visited[yy][xx]:
                if abs(land[y][x] - land[yy][xx]) <= height:
                    Q.append((yy,xx))
                    
def solution(land, height):
    N = len(land)
    visited = [[0]*N for _ in range(N)]
    result = []
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                tmp,min_hi = set([]),10**6
                bfs(deque([(y,x)]),tmp,height,land,visited)
                print(tmp)
                for t in tmp:
                    for d in range(4):
                        yy,xx = y+dy[d],x+dx[d]
                        if (yy,xx) not in tmp and -1<yy<N and -1 < xx<N:
                            min_hi = min(min_hi,abs(land[y][x] - land[yy][xx]))
                result.append(min_hi)
    print(result)
    return sum(sorted(result)[:-1])
