def BFS():
    result = 0
    while tmp:
        for _ in range(len(tmp)):
            y,x = tmp.pop(0)
            for d in range(4):
                if -1 < x+dx[d] < N and -1 < y+dy[d] < N and (maze[y+dy[d]][x+dx[d]] == '0' or maze[y+dy[d]][x+dx[d]] == '3'):
                    tmp.append([y+dy[d], x+dx[d]])
                    maze[y+dy[d]][x+dx[d]] = '2'
        if end in tmp:
            return result
        result +=1
    return 0

for tc in range(int(input())):
    maze = []
    N = int(input())
    for _ in range(N):
        maze.append(list(input()))
    tmp = []
    for y in range(N):
        for x in range(N):
            if maze[y][x] == '3':
                end = [y,x]
            elif maze[y][x] == '2':
                start = [y,x]
                tmp.append(start)
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    print(f'#{tc+1} {BFS()}')