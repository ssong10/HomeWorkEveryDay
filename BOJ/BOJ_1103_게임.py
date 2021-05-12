import sys
sys.setrecursionlimit(10**8)

dy,dx = [-1,0,1,0],[0,1,0,-1]
def go(y,x):
  global flag
  if answer[y][x]:
    return answer[y][x]
  if not flag:
    return 0
  X = board[y][x]
  for d in range(4):
    yy,xx = y+dy[d]*X , x+dx[d]*X
    if -1<yy<N and -1<xx<M and board[yy][xx] != 'H':
      if visit[yy][xx]:
        flag = False
      visit[yy][xx] = True
      tmp = go(yy,xx)
      if answer[y][x] <= tmp:
        answer[y][x] = tmp + 1
      visit[yy][xx] = False
  return answer[y][x]
        
N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]
for y in range(N):
  for x in range(M):
    if board[y][x] != 'H':
      board[y][x] = int(board[y][x])
answer = [[0] * M for _ in range(N)]
visit = [[False] * M for _ in range(N)]
flag = True
go(0,0)
if flag:
  print(answer[0][0]+1)
else:
  print(-1)