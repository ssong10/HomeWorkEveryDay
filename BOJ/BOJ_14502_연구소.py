dy, dx = [-1,1,0,0],[0,0,-1,1]

def depence(wall,v):
    global result
    check = [[0 for _ in range(M)] for _ in range(N)]
    cnt = len(blank)-3
    for w in wall:
        check[blank[w][0]][blank[w][1]] = 1
    while v:
        if cnt < result:
            break
        y,x=v.pop()
        for d in range(4):
            yy,xx = y+dy[d] , x+dx[d]
            if -1 <yy<N and -1 < xx < M and not check[yy][xx]:
                if not check[yy][xx] and not rooms[yy][xx]:
                    check[yy][xx] = 1
                    v.append((yy,xx))
                    cnt -= 1
    result = max(result,cnt)

N , M = map(int,input().split())
rooms = [list(map(int,input().split())) for _ in range(N)]
blank, virus = [],[]
result = 0
for i in range(N):
    for j in range(M):
        if rooms[i][j] == 0:
            blank.append((i,j))
        elif rooms[i][j] == 2:
            virus.append((i,j))
for i in range(len(blank)-2):
    for j in range(i+1,len(blank)-1):
        for k in range(j+1,len(blank)):
            depence([i,j,k],virus[:])
print(result)