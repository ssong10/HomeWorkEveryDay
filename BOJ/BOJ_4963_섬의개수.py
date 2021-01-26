dy, dx = [-1,0,1,-1,1,-1,0,1],[-1,-1,-1,0,0,1,1,1]
def BFS(tmp):
  while tmp:
    y,x = tmp.pop()
    for d in range(8):
      yy,xx = y+dy[d],x+dx[d]
      if -1<yy<h and -1<xx<w and board[yy][xx] and not visit[yy][xx]:
        visit[yy][xx]= True
        tmp.append((yy,xx))
while True:
  answer = 0
  w,h = map(int,input().split())
  if w == 0 and h == 0:
    break
  board = [list(map(int,input().split())) for _ in range(h)]
  visit = [[False]*w for _ in range(h)]
  for y in range(h):
    for x in range(w):
      if board[y][x] and not visit[y][x]:
        visit[y][x] = True
        BFS([(y,x)])
        answer += 1
  print(answer)