def pprint(array):
  for i in range(len(array)):
    print(*array[i])
N = int(input())
K = int(input())
board = [[False] * N for _ in range(N)]
snake = [0,0]
for _ in range(K):
  y,x = map(int,input().split())
  board[y-1][x-1] = True
pprint(board)
L = int(input())
moves = [list(input().split()) for _ in range(L)]
print(moves)
