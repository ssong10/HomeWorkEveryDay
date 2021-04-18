N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
dy, dx = [0,1,0,-1],[-1,0,1,0]

def changedir(x,y):
  tmp = 1 if N/2 > y else 0
  return x+y == N-1 or x+tmp==y
flow = {
  (2,0) : 5,
  (1,1) : 10,
  (1,-1) : 10,
  (0,1) : 7,
  (0,2) : 2,
  (0,-1) : 7,
  (0,-2): 2,
  (-1,1): 1,
  (-1,-1): 1,
}

y,x,d = N//2, N//2, 0
while x + y:
  print(y,x,d)
  y,x = y+dy[d],x+dx[d]

  if changedir(x,y):
    d = (d + 1) % 4