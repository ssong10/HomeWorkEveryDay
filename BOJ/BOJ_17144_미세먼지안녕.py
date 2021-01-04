from collections import deque
R, C, T = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(R)]
dy,dx = [-1,1,0,0], [0,0,-1,1]
for _ in range(T):
    dusts = {}
    winds = []
    for y in range(R):
        for x in range(C):
            if room[y][x] > 0:
                dusts[(y,x)] = room[y][x]
            elif room[y][x] == -1:
                winds.append([y,x])

    for dust in dusts:
        y,x = dust[0], dust[1]
        for d in range(4):
            yy , xx = y+dy[d],x+dx[d]
            if -1 < yy < R and -1 < xx < C and room[yy][xx] != -1:
                room[yy][xx] += dusts[dust]//5
                room[y][x] -= dusts[dust]//5

    [y,x] = winds.pop()
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

    [y,x] = winds.pop()
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
print(sum(map(sum,room))+2)
