from collections import deque
dy, dx = [-1,1,0,0] , [0,0,-1,1]
def check(board):
  for row in board:
    for val in row:
      if val:
        return True
  return False

def oxyzen(tmp):
  while tmp:
    for _ in range(len(tmp)):
      y,x = tmp.popleft()
      visit[y][x] = 1
      for d in range(4):
        yy,xx = y+dy[d], x+dx[d]
        if -1<yy<N and -1 <xx<M :
          if board[yy][xx]:
            visit[yy][xx] += 1
          elif not visit[yy][xx]:
            visit[yy][xx] = 1
            tmp.append((yy,xx))
  for y in range(N):
    for x in range(M):
      if visit[y][x] > 1:
        board[y][x] = 0

N, M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

answer = 0
while check(board):
  visit = [[0]*M for _ in range(N)]
  oxyzen(deque([(0,0)]))
  answer += 1
print(answer)