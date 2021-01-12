dy,dx = [-1,1,0,0], [0,0,-1,1]
def BFS(arr):
  while arr:
    y,x = arr.pop()
    for d in range(4):
      yy,xx = y+dy[d],x+dx[d]
      if -1<yy<N and -1<xx<N and visited[yy][xx]:
        arr.append((yy,xx))
        visited[yy][xx] = False
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
MIN,MAX = min(map(lambda x:min(x),board)), max(map(lambda x:max(x),board))
result = 0
for i in range(MIN-1,MAX):
  visited = list(map(lambda x: list(map(lambda y: y>i,x)),board))
  answer = 0
  for y in range(N):
    for x in range(N):
      if visited[y][x]:
        BFS([(y,x)])
        answer += 1
  result = max(result,answer)
print(result)
  