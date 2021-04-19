N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
dy, dx = [0,1,0,-1],[-1,0,1,0]
result = 0

def changedir(x,y):
  tmp = 1 if N/2 > y else 0
  return x+y == N-1 or x+tmp==y

def wind(y,x,sand):
  global result, tmp
  if -1<x<N and -1<y<N:
    board[y][x] += sand
  else:
    result += sand
  tmp += sand
def per(p):
  return sands*p//100

y,x,d = N//2, N//2, 0
while x+y:
  y,x = y+dy[d],x+dx[d]
  sands = board[y][x]
  board[y][x] = 0
  tmp = 0
  wind(y+(dy[d]*2), x+(dx[d]*2),per(5))
  if dy[d]:
    a = [[dy[d],1,10],[dy[d],-1,10],[0,1,7],[0,-1,7],[0,2,2],[0,-2,2],[-dy[d],1,1],[-dy[d],-1,1]]
    for ny,nx,p in a:
      wind(y+ny,x+nx,per(p))
  else:
    a = [[1,dx[d],10],[-1,dx[d],10],[1,0,7],[-1,0,7],[2,0,2],[-2,0,2],[1,-dx[d],1],[-1,-dx[d],1]]
    for ny,nx,p in a:
      wind(y+ny,x+nx,per(p))
  wind(y+dy[d],x+dx[d],sands-tmp)
  if changedir(x,y):
    d = (d + 1) % 4

print(result)