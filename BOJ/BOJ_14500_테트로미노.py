import sys
input = sys.stdin.readline

def build(tmp):
  global answer
  while tmp:
    y,x,n,v,prev = tmp.pop()
    if n == 4:
      answer = max(answer,v)
    else:
      for d in range(4):
        if prev + d != 3:
          yy,xx = y+dy[d],x+dx[d]
          if -1<yy<N and -1<xx<M:
            tmp.append((yy,xx,n+1,v+board[yy][xx],d))

def tbuild(y,x):
  global answer
  arr = []
  for d in range(4):
    yy,xx = y+dy[d],x+dx[d]
    if -1<yy<N and -1<xx<M:
      arr.append(board[yy][xx])
  total = sum(arr) + board[y][x]
  if len(arr) == 3:
    answer = max(answer,total)
  if len(arr) == 4:
    for i in arr:
      answer = max(answer,total-i)

dy,dx = [-1,0,0,1],[0,-1,1,0]
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
answer = 0
for y in range(N):
  for x in range(M):
    tbuild(y,x)
    build([(y,x,1,board[y][x],-1)])
print(answer)
