from collections import deque
dy,dx = [0,1,0,-1],[1,0,-1,0]

def solution(board):
    answer = 0
    n = len(board)
    prices = [[10**10] * n for _ in range(n)]
    q = deque([[0,0,0,0],[0,0,0,1]])
    while q:
        for _ in range(len(q)):
            y,x,v,d = q.popleft()
            if prices[y][x] >= v:
                prices[y][x] = v
                for dd in range(4):
                    yy,xx = y+dy[dd],x+dx[dd]
                    if -1 < yy < n and -1 < xx < n and not board[yy][xx]:
                        if d == dd:
                            q.append([yy,xx,v+100,dd])
                        elif abs(d - dd) == 1 or abs(d-dd)==3:
                            q.append([yy,xx,v+600,dd])
    return prices[n-1][n-1]
solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])
solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])
solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]])