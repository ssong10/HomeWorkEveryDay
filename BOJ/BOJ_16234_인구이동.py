from collections import deque

def dfs(tmp):
  while tmp:
    for _ in range(len(tmp)):
      y,x = tmp.popleft()
      unions[-1].append((y,x))
      visit[y][x] = True
      for d in range(4):
        yy, xx = y+dy[d], x+dx[d]
        if -1<yy<N and -1<xx<N and not visit[yy][xx]:
          if L-1 < abs(nations[y][x] - nations[yy][xx]) < R+1:
            tmp.append((yy,xx))
  

dy, dx = [-1,1,0,0] , [0,0,-1,1]
N, L, R = map(int,input().split())

nations = [list(map(int,input().split())) for _ in range(N)]


answer = 0 
while True:
  visit = [[False] * N for _ in range(N)]
  flag=False
  unions = []
  for y in range(N):
    for x in range(N):
      if not visit[y][x]:
        unions.append([])
        dfs(deque([(y,x)]))
  print(unions)
  for union in unions:
    popul , size = 0 , len(union)
    if size > 1:
      for (y,x) in union:
        popul += nations[y][x]
      for (y,x) in union:
        nations[y][x] = popul // len(union)
      flag = True
  if flag:
    print(nations)
    answer += 1
  else:
    break
print(answer)