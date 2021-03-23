dy, dx = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

N, M, K = map(int,input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
  r,c,m,s,d = map(int,input().split())
  board[r-1][c-1].append((m,s,d))

for _ in range(K):
  # move
  tmp = {}
  for y in range(N):
    for x in range(N):
      if board[y][x]:
        for ball in board[y][x]:
          m,s,d= ball
          n_r, n_c = (y+(dy[d] * s))%N,(x+(dx[d]*s))%N
          if (n_r,n_c) in tmp:
            tmp[(n_r,n_c)].append((m,s,d))
          else:
            tmp[(n_r,n_c)] = [(m,s,d)]
  # crash
  new_board = [[[] for _ in range(N)] for _ in range(N)]
  for (y,x) in tmp:
    balls = tmp[(y,x)]
    if len(balls) > 1:
      tmp[(y,x)] = []
      total_m,total_v,total_d = 0, 0, 0
      for ball in balls:
        m,s,d = ball
        total_m += m
        total_v += s
        total_d += d % 2
      avg_m = total_m // 5
      avg_v = total_v // len(balls)
      if avg_m:
        for i in range(4):
          if total_d in [0,len(balls)]:
            d = 2 * i
          else:
            d = 2 * i + 1
          tmp[(y,x)].append((avg_m,avg_v,d))
    new_board[y][x] = tmp[(y,x)]
  board = new_board
answer = 0 
for y in range(N):
  for x in range(N):
    for m,s,d in board[y][x]:
      answer += m
print(answer)