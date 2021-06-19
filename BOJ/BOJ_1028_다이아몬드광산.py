def down(x,y,tmp):
  for i in range(tmp+1):
    if not (arr[y+tmp+i][x-tmp+i] and arr[y+tmp+i][x+tmp-i]):
      return False
  return True

def isIn(x,y,tmp):
  return -1<x-tmp and x+tmp<M and y+(2*tmp)<N

def top(x,y,tmp):
  if tmp == 0:
    return True
  for i in range(1,tmp+1):
    if not (arr[y+i][x-i] and arr[y+i][x+i]):
      return False
  return True

N,M=map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
big = 0
for y in range(N):
  for x in range(M):
    if arr[y][x]:
      tmp = big
      while isIn(x,y,tmp) and top(x,y,tmp):
        if down(x,y,tmp):
          big = max(big,tmp+1)
        tmp += 1
print(big)