def ckone(y,x,d):
    tmp = []
    while -1 < y  < N and -1 < x  < M:
        if not room[y][x]:
            tmp.append([y,x])
        if room[y][x] == 6:
            break
        y,x = y+dy[d],x+dx[d]
    return tmp

def back(camera):
    for i in range(1,6):
        for _ in range(len(camera[i])):
            [y,x] = camera[i].pop()
            for d in range(4):
                print(ckone(y,x,d))

N,M = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
camera = {1 :[], 2:[], 3:[] , 4:[], 5:[]}
for y in range(N):
    for x in range(M):
        if room[y][x] and room[y][x] != 6:
            camera[room[y][x]].append([y,x])
dy,dx = [-1,0,1,0], [0,1,0,-1]
back(camera)