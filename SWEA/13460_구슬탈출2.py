N,M = map(int,input().split())
miro = [list(input()) for _ in range(N)]
point = []
dp = []
for y in range(N):
    for x in range(M):
        if miro[y][x] != '#':
            if (miro[y][x+1]=='#' or miro[y][x-1]=='#') & (miro[y+1][x]=='#' or miro[y-1][x]=='#'):
                point.append([y,x])
        if miro[y][x]=='O':
            hole = [y,x]
        elif miro[y][x] == 'R':
            red = [y,x]
        elif miro[y][x] == 'B':
            blue = [y,x]
dp.append(hole)
print(point)
for i in range(1,10):
    [y, x] = dp[-1]
    for p in point:
        print(p)
        if (p[0] == y) != (p[1] == x) and p not in dp:
            dp.append(p)
            break
print(dp)