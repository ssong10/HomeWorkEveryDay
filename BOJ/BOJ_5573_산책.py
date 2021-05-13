def go(y,x):
  while y != H and x != W:
    if board[y][x]:
      x+=1
    else:
      y+=1
  return y,x
H, W, N = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(H)]
count = [[0] * (W+1) for _ in range(H+1)]
count[0][0] = N-1
for y in range(H):
  for x in range(W):
    tmp = count[y][x]
    half = tmp // 2
    count[y+1][x] += half
    count[y][x+1] += half
    if tmp % 2: # 하나가 남으면
      if board[y][x]: # 오른 쪽
        count[y][x+1] += 1
      else:  # 아래쪽
        count[y+1][x] += 1
      board[y][x] = (board[y][x] + 1) % 2
y,x = go(0,0)
print(y+1,x+1)