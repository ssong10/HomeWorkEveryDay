from collections import deque
dy, dx = [-1,0,1,0], [0,-1,0,1]

def distance(s_y,s_x,e_y,e_x):
  tmp = deque([(s_y-1,s_x-1)])
  result = 0
  visit = [[False] * N for _ in range(N)]
  visit[s_y-1][s_x-1] = True
  while tmp:
    for _ in range(len(tmp)):
      y,x = tmp.popleft()
      if y == e_y-1 and x == e_x-1:
        return result
      for d in range(4):
        yy,xx = y+dy[d], x+dx[d]
        if -1<yy<N and -1<xx<N and board[yy][xx] != 1:
          if not visit[yy][xx]:
            visit[yy][xx] = True
            tmp.append((yy,xx))
    result += 1
def close(s_y,s_x):
  tmp = deque([(s_y-1,s_x-1)])
  visit = [[False] * N for _ in range(N)]
  visit[s_y-1][s_x-1] = True
  time = 0
  while tmp:
    candidate = []
    for _ in range(len(tmp)):
      y,x = tmp.popleft()
      if board[y][x] > 1:
        candidate.append([y,x,board[y][x],time])
      for d in range(4):
        yy,xx = y+dy[d], x+dx[d]
        if -1<yy<N and -1<xx<N:
          if not visit[yy][xx] and board[yy][xx] != 1:
            visit[yy][xx] = True
            tmp.append((yy,xx))
    if candidate:
      candidate.sort()
      return candidate[0]
    time += 1

N, M, V = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
Y,X = map(int,input().split())
person = []
visit = [False] * M
for i in range(M):
  a,b,c,d = map(int,input().split())
  board[a-1][b-1] = i + 2
  f = distance(a,b,c,d)
  if not f:
    V = -1
  person.append((a,b,c,d,distance(a,b,c,d)))

if V != -1:
  for _ in range(M):
    man = close(Y,X)
    if not man:
      V = -1
      break
    y,x,i,v = man
    a,b,c,d,f = person[i-2]
    board[a-1][b-1] = 0
    V -= v + f
    if V < 0:
      V = -1
      break
    V += 2*f
    Y,X = c,d
print(V)