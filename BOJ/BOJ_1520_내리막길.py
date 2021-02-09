import heapq
dy,dx = [-1,1,0,0],[0,0,-1,1]
def go(tmp):
  while tmp:
    v,y,x = heapq.heappop(tmp)
    for d in range(4):
      yy,xx = y+dy[d],x+dx[d]
      if -1<yy<M and -1 <xx < N and board[yy][xx] < -v:
        if arr[yy][xx]:
          arr[yy][xx] += arr[y][x]
        else:
          arr[yy][xx] = arr[y][x]
          heapq.heappush(tmp,(-board[yy][xx],yy,xx))

M, N = map(int,input().split()) # 4,5
board = [list(map(int,input().split())) for _ in range(M)]
arr =[[0]*N for _ in range(M)]
arr[0][0] = 1
go([(-board[0][0],0,0)])
print(arr[-1][-1])
