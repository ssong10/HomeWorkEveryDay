N, Q = map(int,input().split())
NN = 2**N
board = [list(map(int,input().split())) for _ in range(NN)]
Ls = list(map(int,input().split()))
dy, dx = [-1,0,1,0],[0,-1,0,1]

for i in range(Q):
  L = Ls[i]
  n = 2 ** L
  for y in range(2**(N-L)):
    for x in range(2**(N-L)):
      Y, X = y*n, x*n
      part = []
      for yy in range(n):
        part.append(board[Y+yy][X:X+n])
      for yy in range(n):
        for xx in range(n):
          board[Y+yy][X+xx] = part[n-xx-1][yy]
  ices = [[0] * NN for _ in range(NN)]
  for y in range(NN):
    for x in range(NN):
      if board[y][x]:
        for d in range(4):
          yy,xx = y+dy[d],x+dx[d]
          if -1<yy<NN and -1<xx<NN:
            ices[yy][xx] += 1
  for y in range(NN):
    for x in range(NN):
      if ices[y][x] < 3:
        if board[y][x]:
          board[y][x] -= 1
print(sum(map(sum,board)))

result = 0
visit = [[False] * NN for _ in range(NN)]
for y in range(NN):
  for x in range(NN):
    if board[y][x] and not visit[y][x]:
      visit[y][x] = True
      tmp = [(y,x)]
      count = 0
      while tmp:
        count += 1
        y,x = tmp.pop()
        for d in range(4):
          yy,xx = y+dy[d],x+dx[d]
          if -1<yy< NN and -1<xx <NN and board[yy][xx]:
            if not visit[yy][xx]:
              visit[yy][xx] = True
              tmp.append((yy,xx))
      result = max(count,result)
print(result)