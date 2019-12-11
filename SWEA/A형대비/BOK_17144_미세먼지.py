def bfs():
    dusts = {}
    winds = []
    for y in range(R):
        for x in range(C):
            if room[y][x] > 0:
                dusts[(y,x)] = room[y][x]
            if room[y][x] == -1:
                winds.append([y,x])
    for dust in dusts:
        y,x = dust[0], dust[1]
        for d in range(4):
            if -1 < y+dy[d] < R and -1 < x+dx[d] < C and room[y+dy[d]][x+dx[d]] != -1:
                room[y+dy[d]][x+dx[d]] += dusts[dust]//5
                room[y][x] -= dusts[dust]//5

    [y,x] = winds.pop(0)
    Y = y

    for _ in range(Y):
        if room[y][x] != -1:
            room[y][x],room[y-1][x] = room[y-1][x],0
        y,x = y-1,x
    for _ in range(C-1):
        if room[y][x] != -1:
            room[y][x],room[y][x+1] = room[y][x+1],0
        y,x = y,x+1
    for _ in range(Y):
        if room[y][x] != -1:
            room[y][x],room[y+1][x] = room[y+1][x],0
        y,x = y+1,x
    for _ in range(C-1):
        if room[y][x] != -1 and not room[y][x-1] == -1:
            room[y][x],room[y][x-1] = room[y][x-1],0
        y,x = y,x-1
    [y,x] = winds.pop(0)
    Y = y
    for _ in range(R-Y-1):
        if room[y][x] != -1:
            room[y][x],room[y+1][x] = room[y+1][x],0
        y,x = y+1,x
    for _ in range(C-1):
        if room[y][x] != -1:
            room[y][x],room[y][x+1] = room[y][x+1],0
        y,x = y,x+1
    for _ in range(R-Y-1):
        if room[y][x] != -1:
            room[y][x],room[y-1][x] = room[y-1][x],0
        y,x = y-1,x
    for _ in range(C-1):
        if room[y][x] != -1 and not room[y][x-1] == -1:
            room[y][x],room[y][x-1] = room[y][x-1],0
        y,x = y,x-1
    for r in room:
        print(r)
    print('---------------')

R, C, T = map(int,input().split())
room = []
dy,dx = [-1,1,0,0], [0,0,-1,1]
for _ in range(R):
    room.append(list(map(int,input().split())))
for _ in range(T):
    bfs()
result = 0
for r in room:
    result += sum(r)
print(result+2)
