dy, dx = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

N, M, K = map(int,input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
  r, c, m, s, d = map(int,input().split())
  board[r-1][c-1].append((m,s,d))
for y in range(N):
  for x in range(N):
    balls = {}
    if board[y][x]:
      (m,s,d) = board[y][x]
      if (r,c) in balls:
        balls[(r,c)].append((m,s,d))
      else:
        balls[(r,c)] = [(m,s,d)]