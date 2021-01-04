dy, dx = [-1,0,1,0],  [0,1,0,-1]

def findAir(room):
  air = []
  for y in range(R):
    for x in range(C):
      if room[y][x] == -1:
        air.append((y,x))
  return air

def dust(air,room):
  new_room = [[0] * C for _ in range(R)]
  for (y,x) in air:
    new_room[y][x] = -1
  for y in range(R):
    for x in range(C):
      val = room[y][x]
      if val > 0:
        tmp = 0
        for d in range(4):
          yy, xx = y+dy[d],x+dx[d]
          if -1<yy<R and -1 <xx < C and room[yy][xx] > -1:
            new_room[yy][xx] += (val // 5)
            tmp += 1
        new_room[y][x] += val - ((val//5)*tmp)
  return new_room
        
def circulation(air, wind):
  [y,x] = air
  if wind > 0:
    d = 0
    s,e = -1, y + 1
  else:
    d = 2
    s,e = y-1, R
  yy , xx = y+dy[d], x+dx[d]
  while room[yy][xx] != -1:
    if room[yy][xx] == -1:
      room[yy+dy[d]][xx+dx[d]] = 0
    else:
      if s <yy+dy[d]< e and -1 <xx+dx[d]<C:
        pass
      else:
        d = (d+wind) %4
      next_y , next_x = yy+dy[d], xx+dx[d]
      if room[next_y][next_x] == -1:
        break
      else:
        room[yy][xx],room[next_y][next_x] = room[next_y][next_x],0
      yy,xx = next_y, next_x

R, C, T = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R)]
air = findAir(room)
for _ in range(T):
  room = dust(air,room)
  circulation(air[0],1)
  circulation(air[1],-1)
  for r in room:
    print(r)
  print()
print(sum(map(sum,room))+2)