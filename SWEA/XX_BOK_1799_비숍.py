N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
bsx = {}
bsy = {}
for y in range(N):
    for x in range(N):
        if board[y][x]:
            if y+x in bsx:
                bsx[y+x].append([y,x])
            else:
                bsx[y+x] = [[y,x]]
            if y-x in bsy:
                bsy[y-x].append([y, x])
            else:
                bsy[y-x] = [[y, x]]
print(bsx)
print(bsy)
print(len(bsx)+len(bsy)-2*N)

