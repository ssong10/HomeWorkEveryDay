dir = [
    [[0],[1],[2],[3]],
    [[1,3],[0,2]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
    [[1,2,3,4]]
]
dx,dy = [0,1,0,-1],[-1,0,1,0]

def back(i,cnt):
    for dd in dir[i]:
        tmp = []
        print(dd)
        for d in dd:
            yy,xx = cameras[i][0] + dy[d] , cameras[i][1]+dx[d]
            print(yy,xx)

N, M = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
cameras = []
for y in range(N):
    for x in range(M):
        if room[y][x] and room[y][x] < 6:
            cameras.append([y,x,room[y][x]])
visit = [False] * len(cameras)
back(0,0)

