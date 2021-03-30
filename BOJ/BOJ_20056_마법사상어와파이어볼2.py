dy, dx = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

even, odd = [0,2,4,6],[1,3,5,7]
def move(board):
  new_board = [[[] for _ in range(N)] for _ in range(N)]
  for y in range(N):
    for x in range(N):
      balls = board[y][x]
      for ball in balls:
        m,s,d = ball
        yy, xx = (y+(dy[d]*s)+N)%N, (x+(dx[d]*s)+N)%N
        new_board[yy][xx].append((m,s,d))
  for y in range(N):
    for x in range(N):
      count = len(new_board[y][x])
      if count > 1:
        tmp = []
        mm, ss, dd = 0,0,0
        for ball in new_board[y][x]:
          m,s,d = ball
          mm, ss, dd = mm+m, ss+s, dd+(d%2)
        if mm//5:
          if dd == 0 or dd == count:
            new_d = even
          else:
            new_d = odd
          for d in new_d:
            tmp.append((mm//5, ss//count,d))
        new_board[y][x] = tmp
  return new_board


N, M, K = map(int,input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
  R,C,M,S,D = map(int,input().split())
  board[R-1][C-1].append((M,S,D))

for _ in range(K):
  board = move(board)

result = 0
for y in range(N):
  for x in range(N):
    for ball in board[y][x]:
      m,s,d = ball
      result += m
print(result)