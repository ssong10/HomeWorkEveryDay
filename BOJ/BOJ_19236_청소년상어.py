import copy
dy, dx = [-1,-1,0,1,1,1,0,-1], [0,-1,-1,-1,0,1,1,1]
fish = {}
board = []

def solve(board,fish,y,x,answer):
  global result
  new_board = copy.deepcopy(board)
  new_fish = copy.deepcopy(fish)

  # eat
  num = new_board[y][x]
  d = new_fish[num][2]
  new_board[y][x] = -1
  new_fish[num] = [-1,-1,-1]
  answer += num
  if result < answer:
    result = answer
  # fish move
  for i in range(1,17):
    fish_y, fish_x, fish_d = new_fish[i]
    if fish_y > -1:
      for cd in range(8):
        dd = (fish_d+cd) % 8
        yy, xx = fish_y + dy[dd], fish_x + dx[dd]
        if -1<yy<4 and -1 <xx <4 and not (yy == y and xx == x):
          target = new_board[yy][xx]
          if target>0:
            new_fish[target] = [fish_y, fish_x, new_fish[target][2]]
          new_fish[i] = [yy,xx,dd]
          new_board[yy][xx], new_board[fish_y][fish_x] = i, target
          break
  # shark move
  for i in range(1,4):
    yy, xx = y + (dy[d] * i), x+ (dx[d] * i)
    if -1<yy<4 and -1<xx<4 and new_board[yy][xx] > 0:
      solve(new_board,new_fish,yy,xx,answer)



for y in range(4):
  board.append([0,0,0,0])
  row = list(map(int,input().split()))
  for x in range(4):
    num, d = row[x*2], row[x*2+1] -1
    board[y][x] = num
    fish[num] = [y,x,d]
result = 0
solve(board,fish,0,0,0)
print(result)