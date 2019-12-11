from collections import deque
dy,dx = [-1,1,0,0],[0,0,-1,1]
def bfs(tmp):
    global result
    while tmp:
        for _ in range(len(tmp)):
            [y,x] = tmp.popleft()
            if [y,x] == [N-1,N-1]:
                result = min(result,visit[y][x])
            else:
                for d in range(4):
                    a = 9
                    yy,xx = y+dy[d],x+dx[d]
                    if -1<yy<N and -1<xx<N:
                        n = visit[y][x] + arr[yy][xx]
                        if n < result and (visit[yy][xx] == 0 or n < visit[yy][xx]) and n <= a:
                            visit[yy][xx] = n
                            tmp.append([yy,xx])
                            a = n

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    tmp = deque([[0,0]])
    result = sum(arr[0][0:N-1]) + sum(map(lambda x:x[N-1],arr))
    bfs(tmp)
    print(f'#{tc+1} {result}')