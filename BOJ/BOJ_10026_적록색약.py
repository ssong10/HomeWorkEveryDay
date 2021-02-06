dy, dx = [-1,1,0,0],[0,0,-1,1]
def bfs(tmp,color,visit,dif):
  while tmp:
    y,x = tmp.pop()
    for d in range(4):
      yy,xx = y+dy[d],x+dx[d]
      if -1 < yy < N and -1 <xx < N:
        if same(arr[yy][xx],color,dif) and not visit[yy][xx]:
          visit[yy][xx] = True
          tmp.append((yy,xx))
def same(a,b,dif):
  if dif:
    return a==b
  if a == b:
    return True
  elif a != 'B' and b !='B':
    return True
  else:
    return False

N = int(input())

arr = [input() for _ in range(N)]
RB = [[False] * N for _ in range(N)]
GRB = [[False] * N for _ in range(N)]
count = [0,0]
for y in range(N):
  for x in range(N):
    if not RB[y][x]:
      count[0] += 1
      RB[y][x] = True
      bfs([(y,x)],arr[y][x],RB,True)
    if not GRB[y][x]:
      count[1] += 1
      GRB[y][x] = True
      bfs([(y,x)],arr[y][x],GRB,False)
print(*count)