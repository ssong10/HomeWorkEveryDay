dy, dx = [-1,1,0,0],[0,0,-1,1]
def road(roadlist,chance,top_hi):
    global result
    if result < len(roadlist):
        result = len(roadlist)
        print(roadlist)
    y,x = roadlist[-1]
    for d in range(4):
        yy,xx = y+dy[d], x+dx[d]
        if -1 < yy < N and -1 < xx < N and not visit[yy][xx]:
            if arr[yy][xx] < top_hi:
                roadlist.append((yy,xx))
                visit[yy][xx] = 1
                road(roadlist,chance,arr[yy][xx])
                visit[yy][xx] = 0
                roadlist.pop()
            elif chance and arr[yy][xx] -K < top_hi:
                roadlist.append((yy,xx))
                visit[yy][xx] = 1
                road(roadlist,chance-1,top_hi-1)
                visit[yy][xx] = 0
                roadlist.pop()

for tc in range(int(input())):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    top_hi,toplist = arr[0][0],[]
    result = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] > top_hi:
                top_hi = arr[y][x]
                toplist = [(y,x)]
            elif arr[y][x] == top_hi:
                toplist.append((y,x))
    for top in toplist:
        visit = [[0] * N for _ in range(N)]
        visit[top[0]][top[1]] = 1
        road([top],1,top_hi)
    print(f'#{tc+1} {result}')