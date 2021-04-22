import copy
def pick(count,idx):
  global result
  if count == 3:
    copy_arr = copy.deepcopy(board)
    kill, bye = 0, 0
    while total - kill- bye:
      deads = set()
      for i in range(M):
        if archers[i]:
          tmp = [N+M,-1,-1]
          for x in range(M):
            for y in range(N):
              # N, i
              d = N-y + abs(x-i)
              if (d < D+1) and copy_arr[y][x]:
                if d < tmp[0]:
                  tmp = [d,y,x]
          if tmp[1] + tmp[2] > 0:
            deads.add((tmp[1],tmp[2]))
      for dead in deads:
        y,x = dead
        kill += 1
        copy_arr[y][x] = 0
      for y in range(N-1,-1,-1):
        for x in range(M):
          if copy_arr[y][x]:
            copy_arr[y][x] = 0
            if y != N-1:
              copy_arr[y+1][x] = 1
            else:
              bye += 1
    result = max(result,kill)
  else:
    for j in range(idx,M):
      if not archers[j]:
        archers[j] = True
        pick(count+1,j)
        archers[j] = False

N, M, D = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
result = 0
enemy = []
total = 0
for y in range(N):
  for x in range(M):
    if board[y][x]:
      total +=1

archers = [False] * M

pick(0,0)
print(result)