import sys
sys.setrecursionlimit(10**6)

def BFS(y,x):
    land[y][x] = 0
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for d in range(4):
        if -1 < x+dx[d] < M and -1< y+dy[d] < N and land[y+dy[d]][x+dx[d]] != 0:
            BFS(y+dy[d],x+dx[d])

for tc in range(int(input())):
    M, N, K = map(int, input().split())
    land = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x,y = map(int, input().split())
        land[y][x] = 1
    result = 0
    for y in range(N):
        for x in range(M):
            if land[y][x] > 0:
                BFS(y,x)
                result += 1
    print(result)