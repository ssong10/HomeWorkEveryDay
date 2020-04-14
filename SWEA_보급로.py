dy,dx = [1,0,-1,0],[0,1,0,-1]

def bfs(tmp):
    global result
    while tmp:
        y,x = tmp.popleft()
        for d in range(4):
            yy,xx = y+dy[d],x+dx[d]
            if -1 < yy < N and -1 < xx < N:
                if not visit[yy][xx] or (visit[yy][xx] and visit[yy][xx] > visit[y][x]+arr[yy][xx]):
                    visit[yy][xx] = val
                    tmp.append([yy,xx,dd])
    if tmp2:
        bfs(tmp2)
for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    bfs([[0,0]])
    print(f'#{tc+1} {visit[N-1][N-1]}')