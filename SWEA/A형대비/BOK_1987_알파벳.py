def gogo(s,y,x):
    global mx
    cango = False
    for d in range(4):
        if -1< y+dy[d] < R and -1 < x+dx[d] < C:
            idx = ord(board[y + dy[d]][x + dx[d]]) - 65
            if not visit[y+dy[d]][x+dx[d]] and abc[idx] == 0:
                abc[idx] = 1
                gogo(s+1, y+dy[d],x+dx[d])
                abc[idx] = 0
                cango = True
    if not cango:
        mx.append(s)

R,C = map(int,input().split())
board = [list(input()) for _ in range(R)]
abc = [0] * 26
abc[ord(board[0][0])-65] = 1
visit = [[0]*C for _ in range(R)]
visit[0][0] = 1
dy,dx = [-1,1,0,0] , [0,0,-1,1]
mx = []
gogo(1,0,0)
print(max(mx))