from collections import deque
def DFS():
    result = -1
    while tmp:
        for _ in range(len(tmp)):
            y,x = tmp.popleft()
            for d in range(4):
                if -1< y+dy[d] < N and -1 < x+dx[d] < M and tmt[y+dy[d]][x+dx[d]] == 0:
                    tmt[y+dy[d]][x+dx[d]] = 1
                    tmp.append((y+dy[d],x+dx[d]))
        result += 1
    for y in range(N):
        for x in range(M):
            if tmt[y][x] == 0:
                return -1
    return result
   
M,N = map(int,input().split())
tmt = []
for _ in range(N):
    tmt.append(list(map(int,input().split())))
tmp = deque()
for i in range(N):
    for j in range(M):
        if tmt[i][j] == 1:
            tmp.append((i,j))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
print(DFS())