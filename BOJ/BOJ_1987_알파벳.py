dy, dx = [-1,0,1,0],[0,-1,0,1]
R, C = map(int,input().split())
arr = [input() for _ in range(R)]
answer = 0
visited = [[0 for _ in range(C)] for _ in range(R)]
q = set([(0,0,arr[0][0])])
while q and answer <= 26:
  y,x,n = q.pop()
  answer = max(answer,len(n))
  for d in range(4):
    yy,xx = y+dy[d],x+dx[d]
    if -1<yy<R and -1<xx<C and arr[yy][xx] not in n:
      q.add((yy,xx,n+arr[yy][xx]))
print(answer)