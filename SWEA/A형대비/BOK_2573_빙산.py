def water(year):
    island = 0
    ices = {}
    visit = [[0]*M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if north[y][x]:
                ices[(y, x)] = north[y][x]
                if not visit[y][x]:
                    tmp = [(y,x)]
                    visit[y][x] = 1
                    while tmp:
                        yy, xx = tmp.pop(0)
                        for d in range(4):
                            if -1 < yy + dy[d] < N and -1 < xx + dx[d] < M and north[yy + dy[d]][xx + dx[d]] and not visit[yy + dy[d]][xx + dx[d]]:
                                tmp.append((yy + dy[d], xx + dx[d]))
                                visit[yy+ dy[d]][xx + dx[d]] = 1
                    island += 1
    if not island:
        print(0)
    elif island > 1:
        print(year)
    else:
        for ice, val in ices.items():
            y,x = ice
            for d in range(4):
                if -1<y+dy[d]<N and -1 < x+dx[d] < M and not north[y+dy[d]][x+dx[d]]:
                    ices[ice] -= 1
        for ice,val in ices.items():
            y, x = ice
            north[y][x] = max(0, val)
        water(year+1)



dy,dx = [-1,1,0,0], [0,0,-1,1]
N, M = map(int,input().split())
north = [list(map(int,input().split())) for _ in range(N)]
water(0)