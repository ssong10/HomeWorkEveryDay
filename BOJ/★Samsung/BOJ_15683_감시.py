dir = [
    [[0],[1],[2],[3]],
    [[1,3],[0,2]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
    [[1,2,3,0]]
]
dx,dy = [0,1,0,-1],[-1,0,1,0]

def back(i,cnt):
    global result
    if i == len(cameras):
        result = max(result,cnt)
    else:
        for dd in dir[cameras[i][2]-1]:
            tmp = []
            for d in dd:
                y,x = cameras[i][0] , cameras[i][1]
                while -1<y<N and -1<x<M:
                    if room[y][x] == 6:
                        break
                    elif not room[y][x]:
                        tmp.append([y,x])
                    y,x = y+dy[d],x+dx[d]
            for y,x in tmp:
                room[y][x] = '#'
            back(i+1,cnt+len(tmp))
            for y,x in tmp:
                room[y][x] = 0

N, M = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
cameras = []
anw,result = 0,0
for y in range(N):
    for x in range(M):
        if room[y][x] and room[y][x] < 6:
            cameras.append([y,x,room[y][x]])
        if not room[y][x]:
            anw += 1
back(0,0)
print(anw-result)