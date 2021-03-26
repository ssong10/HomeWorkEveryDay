N, M, K = map(int,input().split())
dy,dx = [-1,1,0,0],[0,0,-1,1]
board = [list(map(int,input().split())) for _ in range(N)]

shark_dir = list(map(int,input().split()))
shark_move = {}

for i in range(M):
  tmp = {}
  for d in range(4):
    tmp[d+1] = list(map(int,input().split()))
  shark_move[i+1] = tmp

sharks = {}
for y in range(N):
  for x in range(N):
    if board[y][x]:
      shark_id = board[y][x]
      board[y][x] = [shark_id,K]
      sharks[shark_id] = (y,x,shark_dir[shark_id-1])
# board 에는 피냄새
# sharks 에는 상어 위치랑 방향
count = 0
while len(sharks) > 1 and count < 1001:
  count += 1
  for shark_id in sharks:
    y,x,d = sharks[shark_id]
    move = shark_move[shark_id][d]
    memo = []
    for dd in move:
      yy,xx = y+dy[dd-1], x+dx[dd-1]
      if -1 < yy < N and -1 < xx < N:
        if board[yy][xx]:
          if board[yy][xx][0] == shark_id:
            memo.append((yy,xx,dd))
        else:
          sharks[shark_id] = (yy,xx,dd)
          break
    else:
      sharks[shark_id] = memo[0]
  for i in range(M,0,-1):
    if i in sharks:
      y,x,d = sharks[i]
      if board[y][x]:
        prev = board[y][x][0]
        if board[y][x][1] == K+1:
          del sharks[prev]
      board[y][x] = [i,K+1]
  for y in range(N):
    for x in range(N):
      if board[y][x]:
        board[y][x][1] -= 1
        if not board[y][x][1]:
          board[y][x] = 0
if count == 1001:
  print(-1)
else:
  print(count)