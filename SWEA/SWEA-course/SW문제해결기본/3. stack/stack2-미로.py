def DFS(y,x):
    for d in range(4):
        if -1< y+dy[d] < N and -1< x+dx[d] < N and maze[y+dy[d]][x+dx[d]] == '0':
            maze[y+dy[d]][x+dx[d]] = '2'
            DFS(y+dy[d],x+dx[d])
            
for tc in range(int(input())):
    maze = []
    N = int(input())
    for _ in range(N):
        maze.append(list(input()))
    for y in range(N):
        for x in range(N):
            if maze[y][x] == '2':
                start = [y,x]
            elif maze[y][x] == '3':
                end = [y,x]
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    DFS(start[0],start[1])
    result = 0
    for d in range(4):
        if -1< end[0]+dy[d] < N and -1< end[1]+dx[d] < N and maze[end[0]+dy[d]][end[1]+dx[d]] == '2':
            result = 1
            break
    print(f'#{tc+1} {result}')
    