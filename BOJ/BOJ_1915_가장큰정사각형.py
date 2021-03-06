import sys
input = sys.stdin.readline
n, m = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(n)]
result = 0
for y in range(n):
  for x in range(m):
    tmp = board[y][x]
    if tmp:
      arr = []
      if y:
        arr.append(board[y-1][x])
      if x:
        arr.append(board[y][x-1])
      if x and y:
        arr.append(board[y-1][x-1])
      if len(arr) == 3:
        board[y][x] += min(arr)
      result = max(result,board[y][x])
print(result**2)
