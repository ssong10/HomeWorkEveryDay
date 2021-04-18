dy,dx = [-1,0,1,0],[0,1,0,-1]
camera_dir = {
  1: [[0],[1],[2],[3]],
  2: [[0,2],[1,3]],
  3: [[0,1],[1,2],[2,3],[3,0]],
  4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
  5: [[0,1,2,3]]
}

def setCamera(i, answer):
  global result
  # i = 번호, answer = 사각지대
  if i == len(cameras):
    result = max(result,answer)
  else:
    y,x,n = cameras[i]
    for dd in camera_dir[n]:
      tmp = []
      for d in dd:
        ny,nx = y+dy[d],x+dx[d]
        while -1 < ny < N and -1 < nx < M:
          if room[ny][nx] == 6:
            break
          if not room[ny][nx]:
            tmp.append((ny,nx))
          ny ,nx = ny+dy[d],nx+dx[d]
      for ny,nx in tmp:
        room[ny][nx] = '#'
      setCamera(i+1,answer+len(tmp))
      for ny,nx in tmp:
        room[ny][nx] = 0

N, M = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
cameras = []
result = 0
full = N*M
for y in range(N):
  for x in range(M):
    if room[y][x]:
      if room[y][x] != 6:
        cameras.append((y,x,room[y][x]))
      full -= 1
setCamera(0,0)
print(full-result)