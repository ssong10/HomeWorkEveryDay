dy,dx = [-1,0,1,0],[0,-1,0,1]
def match(board,y,x,visit):
  tmp = [(y,x)]
  answer = []
  color = board[y][x]
  while tmp:
    y,x = tmp.pop()
    answer.append((y,x))
    for d in range(4):
      yy,xx = y+dy[d],x+dx[d]
      if -1<yy<12 and -1<xx<6 and board[yy][xx] == color:
        if not visit[yy][xx]:
          visit[yy][xx] = True
          tmp.append((yy,xx))
  return answer
def pop(board):
  global answer
  visit = [[False]*6 for _ in range(12)]
  delete = []
  flag = False
  for y in range(12):
    for x in range(6):
      if board[y][x] != '.' and not visit[y][x]:
        visit[y][x] = True
        tmp = match(board,y,x,visit)
        if len(tmp) > 3:
          delete += tmp
          flag = True
  if flag:
    answer += 1
    for (y,x) in delete:
      board[y][x] = '.'
    drop(board)
    pop(board)

def drop(board):
    for y in range(11,-1,-1):
      for x in range(6):
        if board[y][x] == '.':
          tmp = y
          while (board[tmp][x] == '.' and tmp > 0):
            tmp -= 1
          board[y][x],board[tmp][x] = board[tmp][x],board[y][x]
board = [list(input()) for _ in range(12)]
answer = 0
pop(board)
print(answer)