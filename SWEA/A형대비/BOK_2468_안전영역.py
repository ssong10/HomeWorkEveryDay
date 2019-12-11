from collections import deque

def DFS(m):
    island = 0
    visit=[]
    for i in range(N):
        for j in range(N):
            if land[i][j] > m and [i,j] not in visit:
                visit.append([i,j])
                tmp = deque([[i,j]])
                while tmp:
                    for _ in range(len(tmp)):
                        y,x = tmp.popleft()
                        for d in range(4):
                            if -1< y+dy[d] < N and -1 < x+dx[d] < N and not [y+dy[d], x+dx[d]] in visit and land[y+dy[d]][x+dx[d]] > m:
                                visit.append([y+dy[d], x+dx[d]])
                                tmp.append([y+dy[d], x+dx[d]])
                island += 1
    print(island)
    return island


N = int(input())
land = []
for _ in range(N):
    land.append(list(map(int,input().split())))
mx,mn = 0,100
for l in land:
    mx = max(mx,max(l))
    mn = min(mn,min(l))
result = []
dy,dx = [-1,1,0,0] , [0,0,-1,1]
result = 0
for m in range(mn,mx):
    result = max(result,DFS(m))
print(result)

