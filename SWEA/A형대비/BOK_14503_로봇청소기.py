def robot(r,c,d):
    global cango, result
    if room[r][c] != 2:
        room[r][c] = 2
        result += 1
    if not cango:
        return
    else:
        for i in range(1,5):
            dd = (d+4-i) % 4
            if -1 < r+dir[dd][0] < N and -1 < c+dir[dd][1] < M and room[r+dir[dd][0]][c+dir[dd][1]] == 0:
                robot(r+dir[dd][0],c+dir[dd][1],dd)
                break
        else:
            if room[r-dir[d][0]][c-dir[d][1]] == 2:
                robot(r-dir[d][0],c-dir[d][1],d)
            else:
                cango = False

N,M = map(int,input().split())
r,c,d = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]
dir = [[-1,0],[0,1],[1,0],[0,-1]]
result = 0
cango = True
robot(r,c,d)
print(result)