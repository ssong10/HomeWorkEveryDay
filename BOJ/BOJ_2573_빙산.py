def isIn(y,x):
  return -1<y< N and -1 <x<M

def melt(year):
  while True:
    # 다녹았나 확인
    if sum(map(sum,ice)) == 0:
      return 0

    ## 분리됐나 확인
    island = 0
    visit = [[False]*M for _ in range(N)]
    for y in range(N):
      for x in range(M):
        if ice[y][x] and not visit[y][x]:
          island += 1
          if island > 1:
            return year
          visit[y][x] = True
          q = [(y,x)]
          while q:
            i,j = q.pop()
            for d in range(4):
              yy, xx= i+dy[d],j+dx[d]
              if isIn(yy,xx) and ice[yy][xx] and not visit[yy][xx]:
                visit[yy][xx] = True
                q.append((yy,xx))
    # 빙하 얼마나 녹을지
    melt = [[0]*M for _ in range(N)]
    for y in range(N):
      for x in range(M):
        if ice[y][x]:
          for d in range(4):
            yy, xx= y+dy[d],x+dx[d]
            if isIn(yy,xx) and not ice[yy][xx]:
              melt[y][x] += 1
    # 빙하 녹음
    for y in range(N):
      for x in range(M):
        if melt[y][x]:
          ice[y][x] = max(ice[y][x]-melt[y][x],0)
    year += 1


dy,dx = [-1,1,0,0],[0,0,-1,1]
N, M = map(int,input().split())
ice = [list(map(int,input().split())) for _ in range(N)]
answer = melt(0)
print(answer)