dy, dx = [-1,1,0,0],[0,0,-1,1]

def bfs(tmp):
    global tmpV, tmpO
    next_tmp = []
    while tmp:
        y,x = tmp.pop()
        check[y][x] = 1
        if board[y][x] == 'v':
            tmpV += 1
        elif board[y][x] == 'o':
            tmpO += 1
        for d in range(4):
            yy,xx = y+dy[d], x+dx[d]
            if -1<yy<R and -1 <xx <C and board[y][x] != '#' and not check[yy][xx]:
                check[yy][xx] = 1
                next_tmp.append((yy,xx))
    if next_tmp:
        bfs(next_tmp)


R, C = map(int,input().split())
board = [input() for _ in range(R)]
check = [[0 for _ in range(C)] for _ in range(R)]
V, O = 0,0
for y in range(R):
    for x in range(C):
        if board[y][x] != '#' and not check[y][x]:
            tmpV, tmpO = 0,0
            bfs([(y,x)])
            if tmpO > tmpV:
                O += tmpO
            else:
                V += tmpV
print(O, V)