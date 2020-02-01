dy, dx =[-1,1,0,0], [0,0,-1,1]

def move(coins, button):
    global result
    if button >= result:
        return
    else:
        y1,x1, y2, x2 = coins
        for d in range(4):
            drop = 0
            new_coins = [y1,x1, y2,x2]
            yy1, xx1, yy2 ,xx2 = y1+dy[d],x1+dx[d], y2+dy[d],x2+dx[d]
            if -1<yy1<N and -1 < xx1< M:
                if board[yy1][xx1] != '#':
                    new_coins[0], new_coins[1] = yy1,xx1
            else:
                drop += 1
            if -1<yy2<N and -1 < xx2< M:
                if board[yy2][xx2] !='#':
                    new_coins[2],new_coins[3] = yy2, xx2
            else:
                drop += 1
            if drop == 1:
                result = button
                return
            if coins != new_coins:
                move(new_coins, button+1)


N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]
coins = []
for y in range(N):
    for x in range(M):
        if board[y][x] == 'o':
            coins += [y,x]
result = 11
move(coins,1)
if result == 11:
    print(-1)
else:
    print(result)