from collections import deque
dy,dx = [-1,0,1,0],[0,1,0,-1]

N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]
for y in range(N):
  for x in range(M):
    if board[y][x] != 'H':
      board[y][x] = int(board[y][x])
result = 0
visit = [[0] * M for _ in range(N)]

tmp = deque([[0,0]])
for d in range(4):
  yy,xx = y+dy[d]*X , x+dx[d]*X
  if -1<yy<N and -1<xx<M and board[yy][xx] != 'H':
    if visit[yy][xx]:
      result = -1
      return
    else:
      go(yy,xx,count+1)
  else:
    if result != -1:
      result = max(result,count+1)


print(result)