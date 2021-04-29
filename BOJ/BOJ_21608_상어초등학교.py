dy,dx = [-1,0,1,0],[0,1,0,-1]
N = int(input())
visit = [[4]*N for _ in range(N)]
for i in [0,N-1]:
  for j in range(N):
    visit[i][j] -= 1
    visit[j][i] -= 1

board = [[0]*N for _ in range(N)]
friend = {}
for _ in range(N*N):
  a,b,c,d,e = map(int,input().split())
  friend[a] = set([b,c,d,e])
  seat = []
  for y in range(N):
    for x in range(N):
      if not board[y][x]:
        tmp = [0,visit[y][x],-y,-x]
        for dd in range(4):
          yy,xx = y+dy[dd],x+dx[dd]
          if -1<yy<N and -1<xx<N:
            next_f = board[yy][xx]
            if next_f and next_f in friend[a]:
              tmp[0] += 1
        if not seat:
          seat = tmp
        elif seat < tmp:
          seat = tmp
  y,x = -seat[2],-seat[3]
  board[y][x] = a
  visit[y][x] = -1
  for d in range(4):
    yy,xx = y+dy[d],x+dx[d]
    if -1<yy<N and -1<xx<N:
      visit[yy][xx] -= 1
total = 0
for y in range(N):
  for x in range(N):
    tmp = 0
    a = board[y][x]
    for d in range(4):
      yy,xx = y+dy[d],x+dx[d]
      if -1<yy<N and -1<xx<N:
        if board[yy][xx] in friend[a]:
          tmp += 1
    if tmp:
      total += 10 ** (tmp-1)
print(total)