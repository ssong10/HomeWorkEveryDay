def dfs(y,x,n,char):
    global result
    if n == 5:
        if char not in result:
            result.append(char)
    else:
        for d in range(4):
            yy,xx = y+dy[d], x+dx[d]
            if -1<yy<5 and -1<xx<5:
                dfs(yy,xx,n+1,char+board[yy][xx])


board = [list(input().split()) for _ in range(5)]
result = []
dy,dx = [-1,1,0,0], [0,0,-1,1]
for y in range(5):
    for x in range(5):
        dfs(y,x,0,board[y][x])
print(len(result)) 