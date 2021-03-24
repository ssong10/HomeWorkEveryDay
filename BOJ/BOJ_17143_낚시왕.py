R, C, M = map(int,input().split())
dy,dx = [-1,1,0,0],[0,0,1,-1]
sharks = [[False for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    sharks[r-1][c-1] = (s,d-1,z)

t=0
for i in range(R):
    if sharks[i][t]:
        s,d,z = sharks[i][t]
        print(z)
        sharks[i][t] = False
        break
move = {}
for y in range(R):
    for x in range(C):
        if sharks[y][x]:
            s,d,z=sharks[y][x]
            yy,xx = (y + (dy[d] * s)) % (2*R-2), (x+(dx[d]*s)) % (2*C-2)
            dd = d
            if yy > R:
                dd += d%2
                yy = 2*R-2-yy
            if xx > R:
                dd += d%2
                xx = 2*C-2-xx

            print(yy,xx,dd)
print(sharks)