dy,dx = [0,0,1,-1], [1,-1,0,0]

def dfs(tmp):
    global result
    for _ in range(len(tmp)):
        [y,x] = tmp.pop(0)
        for d in range(4):
            if not board[y+dy[d]][x+dx[d]]:
                board[y+dy[d]][x+dx[d]] += board[y][x] * dir[d]
                tmp.append([y+dy[d],x+dx[d]])
            else:
                print(board[y][x] * dir[d])
                result -= board[y][x] * dir[d]

M, E, W, N, S = map(int,input().split())
dir = [E/100, W/100, N/100, S/100]
board = [[0]* 30 for _ in range(30)]
board[15][15] = 1
tmp = [[15,15]]
result = 1
for _ in range(3):
    dfs(tmp)
    for b in board:
        print(b)
    print(tmp)
print(result)