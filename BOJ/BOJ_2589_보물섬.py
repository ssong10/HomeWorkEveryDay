from collections import deque

dy, dx = [-1,1,0,0], [0, 0, -1,1]
def bfs(tmp,answer):
    check = [[0 for _ in range(X)] for _ in range(Y)]
    check[tmp[0][0]][tmp[0][1]] = 1
    while tmp:
        for _ in range(len(tmp)):
            y,x = tmp.popleft()
            for d in range(4):
                yy , xx = y + dy[d] , x+dx[d]
                if -1 <yy < Y and -1 < xx < X:
                    if island[yy][xx] == "L" and not check[yy][xx]:
                        check[yy][xx] = 1
                        tmp.append((yy,xx))
        answer += 1
    return answer

Y, X = map(int,input().split())
island = [input() for _ in range(Y)]
result = 0
for y in range(Y):
    for x in range(X):
        if island[y][x] == 'L':
            tmp = deque([(y,x)])
            result = max(result,bfs(tmp,-1))
print(result)