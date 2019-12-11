from collections import deque

def bfs():
    ans = 0
    while tmp:
        for _ in range(len(tmp)):
            y,x = tmp.popleft()
            for d in range(4):
                if -1< y+dy[d] < N and -1 < x+dx[d] < M and land[y+dy[d]][x+dx[d]] =='L' and not [y+dy[d],x+dx[d]] in visit:
                    visit.append([y+dy[d],x+dx[d]])
                    tmp.append((y+dy[d],x+dx[d]))
    return ans

N,M = map(int,input().split())
land = []
dy,dx = [-1,1,0,0] , [0,0,-1,1]
for _ in range(N):
    land.append(input())
result = 0
for i in range(N):
    for j in range(M):
        if land[i][j] == 'L':
            tmp = deque([(i,j)])
            visit = [tmp[0]]
            ans = bfs()
            if result < ans:
                result = ans
print(result)