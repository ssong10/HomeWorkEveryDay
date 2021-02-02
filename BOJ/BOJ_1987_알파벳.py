import sys
sys.setrecursionlimit(10**6)
dy, dx = [-1,0,1,0],[0,-1,0,1]
def go(tmp):
  global answer
  if answer == 26:
    return
  y,x,n = tmp
  for d in range(4):
    yy,xx = y+dy[d],x+dx[d]
    if -1 <yy<R and -1 <xx < C:
      p = idx(arr[yy][xx])
      if not visited[p]:
        answer = max(answer,n+1)
        visited[p] = True
        go((yy,xx,n+1))
        visited[p] = False

def idx(a):
  return ord(a)-ord('A')

R, C = map(int,input().split())
arr = [input() for _ in range(R)]
answer = 0
visited = [False] * 26
visited[idx(arr[0][0])] = True
go((0,0,1))
print(answer)