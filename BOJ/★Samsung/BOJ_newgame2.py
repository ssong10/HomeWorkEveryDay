dy,dx = [0,0,-1,1],[1,-1,0,0]

N, K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
# 0 : 흰,1 : 빨, 2: 파

horses = []
horseboard = [[[] for _ in range(N)] for _ in range(N])
print(horseboard)
for _ in range(K):
    # 행, 열, 방향
    horses.append([y,x,d-1])
gameend = False

for _ in range(1000):
    for horse in horses:
        y,x,d = horse
        yy,xx =y+dy[d], x+dx[d]
        if -1< yy <N and -1 < xx <N:
            if board[yy][xx] == 0:
                
                