R, C, M = map(int,input().split())
dy,dx = [-1,1,0,0],[0,0,1,-1]
next_d = [1,0,3,2]
sharks = [[False for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    sharks[r-1][c-1] = (s,d-1,z)
answer = 0
for t in range(C):
    for i in range(R):
        if sharks[i][t]:
            s,d,z = sharks[i][t]
            answer += z
            sharks[i][t] = False
            break
    move = {}
    for y in range(R):
        for x in range(C):
            if sharks[y][x]:
                s,d,z=sharks[y][x]
                yy,xx = (y + (dy[d] * s)) % (2*R-2), (x+(dx[d]*s)) % (2*C-2)
                dd = d
                if yy >= R:
                    dd = next_d[d]
                    yy = 2*R-2-yy
                if xx >= C:
                    dd = next_d[d]
                    xx = 2*C-2-xx
                if (yy,xx) in move:
                    (ss,sd,sz)= move[(yy,xx)]
                    if sz < z:
                        move[(yy,xx)] = (s,dd,z)
                else:
                    move[(yy,xx)] = (s,dd,z)
                sharks[y][x] = False
    for (y,x) in move:
        s,d,z = move[(y,x)]
        sharks[y][x] = (s,d,z)
print(answer)