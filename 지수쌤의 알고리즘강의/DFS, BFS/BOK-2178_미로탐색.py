def DFS(y,x):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    visit[y][x] = 1
    tmp.pop(0)
    for d in range(4):
        if -1< y+dy[d] < N and -1 < x+dx[d] < M and visit[y+dy[d]][x+dx[d]] ==0 and miro[y+dy[d]][x+dx[d]] == '1':
            tmp.append([y+dy[d],x+dx[d]])

N,M = map(int,input().split())
miro = []
for _ in range(N):
    miro.append(list(input())) # 미로 만들어준다.
visit = [[0 for _ in range(M)] for _ in range(N)]
tmp = [[0,0]]
result = 1
while tmp:
    for i in tmp:
        DFS(i[0],i[1])
    result += 1
print(result)