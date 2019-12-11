dy,dx = [-1,1,0,0] , [0,0,-1,1]

def paths(path,chance):
    global result
    [y,x] = path[-1]
    if result <= len(path):
        result = len(path)
    for d in range(4):
        yy,xx = y+dy[d],x+dx[d]
        if -1 < yy < N and -1 < xx < N and [yy,xx] not in path:
            if roadmap[yy][xx] < roadmap[y][x]:
                paths(path+[[yy,xx]],chance)
            elif chance and roadmap[yy][xx] - K < roadmap[y][x]:
                a = roadmap[yy][xx]
                roadmap[yy][xx] = roadmap[y][x] -1
                paths(path+[[yy,xx]],chance-1)
                roadmap[yy][xx] = a
                
for tc in range(int(input())):
    N,K = map(int,input().split())
    roadmap = [list(map(int,input().split())) for _ in range(N)]
    top_hi = max(map(max,roadmap))
    tops = []
    for y in range(N):
        for x in range(N):
            if roadmap[y][x] == top_hi:
                tops.append([y,x])
    result = 0
    for top in tops:
        paths([top],1)
    print(f'#{tc+1} {result}')