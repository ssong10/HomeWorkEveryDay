import sys
input = sys.stdin.readline

dy, dx = [-1,0,1,0],[0,1,0,-1]
N = int(input())
K = int(input())
board = [[-1] * N for _ in range(N)]
board[0][0] = 1
head,tail = (0,0), (0,0)
d = 1
for _ in range(K):
  y,x = map(int,input().split())
  board[y-1][x-1] = 4

time = 0
L = int(input())
moves = [list(input().split()) for _ in range(L)]
move_cnt = 0
while True:
  time += 1
  hy,hx = head
  nhy,nhx = hy+dy[d], hx+dx[d]
  if -1 < nhy < N and -1< nhx < N:
    if board[nhy][nhx] == 4:
      pass
    elif board[nhy][nhx] == -1:
      # 빈칸일때만 꼬리 바꿔주기
      ty,tx = tail
      td = board[ty][tx]
      tail = (ty+dy[td],tx+dx[td])
      board[ty][tx] = -1
    else:
      break

    # 움직이는지
    if move_cnt < len(moves) and int(moves[move_cnt][0]) == time:
      if moves[move_cnt][1] == 'D':
        d = (d+1) % 4
      else:
        d = (d-1) % 4
      move_cnt += 1

    # 머리 바꿔주기
    head = (nhy,nhx)

    # 머리방향
    board[nhy][nhx] = d
  else:
    break
print(time)