N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
islands = {}
node = [[] for _ in range(6)]
l = 0
dy,dx = [-1,1,0,0],[0,0,-1,1]
for y in range(N):
    for x in range(M):
        if arr[y][x] == 1:
            tmp = [(y,x)]
            l += 1
            node[l-1].append((y,x))
            arr[y][x] += 1
            while tmp:
                y,x = tmp.pop()
                for d in range(4):
                    yy, xx = y +dy[d],x+dx[d]
                    if -1 < yy < N and -1 < xx < M and arr[yy][xx] == 1:
                        tmp.append((yy,xx))
                        node[l-1].append((yy,xx))
                        arr[yy][xx] += 1
print(node)