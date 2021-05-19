dy,dx = [-1,0,1,0],[0,-1,0,1]
def drop(board):
  for i in range(N):
    for y in range(N-i-1):
      for x in range(N):
        if board[y][x] > -1 and board[y+1][x] == -2:
          board[y][x],board[y+1][x] = board[y+1][x],board[y][x]
  return board
def spin(board):
  new_board = [[0] * N for _ in range(N)]
  for y in range(N):
    for x in range(N):
      new_board[y][x] = board[x][N-1-y]
  return new_board


def group(tmp,color,visit,board):
  blocks = [tmp[0]]
  rainbows = []
  while tmp:
    y,x = tmp.pop()
    for d in range(4):
      yy,xx = y+dy[d],x+dx[d]
      if -1<yy<N and -1<xx<N and not visit[yy][xx]:
        if board[yy][xx] == color:
          visit[yy][xx] = True
          tmp.append((yy,xx))
          blocks.append((yy,xx))
        elif board[yy][xx] == 0:
          visit[yy][xx] = True
          tmp.append((yy,xx))
          rainbows.append((yy,xx))
  for (yy,xx) in rainbows:
    visit[yy][xx] = False
  all = blocks + rainbows
  return [len(all),len(rainbows),all,color]
  
def find(board):
  global score
  visit = [[False]*N for _ in range(N)]
  max_blocks = [0,0,[]]
  for y in range(N):
    for x in range(N):
      if not visit[y][x] and board[y][x] > 0:
        visit[y][x] = True
        blocks = group([(y,x)],board[y][x],visit,board)
        if blocks[0] > 1 and max_blocks[:2] <= blocks[:2]:
          max_blocks = blocks
  if max_blocks[0] > 1:
    score += max_blocks[0]**2
    for (y,x) in max_blocks[2]:
      board[y][x] = -2
    board = drop(board)
    board = spin(board)
    board = drop(board)
    find(board)
score = 0
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
score = 0 
find(board)
print(score)