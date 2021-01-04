dr, dc = [-1,0,1,0], [0,1,0,-1]
def isIn(rr,cc):
  if -1 < rr < N and -1 < cc < M:
    return True
  else:
    return False

def clean(robot):
  global answer
  r,c,d = robot
  if room[r][c] == 0:
    answer += 1
    room[r][c] = 2
  for i in range(4):
    dd = (d+3-i) % 4
    rr, cc = r+dr[dd] , c+dc[dd]
    if isIn(rr,cc) and not room[rr][cc]:
      clean([rr,cc,dd])
      break
  else:
    if isIn(r+dr[d-2],c+dc[d-2]) and room[r+dr[d-2]][c+dc[d-2]] != 1:
      clean([r+dr[d-2],c+dc[d-2],d])
    else:
      return

N, M = map(int,input().split())
robot = list(map(int,input().split()))
room = []
answer = 0
for _ in range(N):
  room.append(list(map(int,input().split())))
clean(robot)
print(answer)