dy, dx = [-1,1,0,0], [0,0,-1,1]
def go(cells,k):
    if k:
        new_cells = {}
        for idx,val in cells.items():
            if val[1] != -1:
                if val[1] == 0:
                    y,x = idx
                    for d in range(4):
                        yy,xx = y+dy[d],x+dx[d]
                        if (yy,xx) not in cells.keys():
                            if (yy,xx) in new_cells.keys():
                                new_cells[(yy,xx)] = max(val[0],new_cells[(yy,xx)])
                            else:
                                new_cells[(yy,xx)] = val[0]
                if val[2] == 1:
                    val[2] = val[0]
                    val[1] -= 1
                else:
                    val[2] -= 1
        for idx,val in new_cells.items():
            cells[idx] = [val,1,val]
        go(cells,k-1)
    else:
        result = 0
        for cell,val in cells.items():
            if val[1]>-1:
                result += 1
        print(f'#{tc+1} {result}')

for tc in range(int(input())):
    N, M , K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cells = {}
    for y in range(N):
        for x in range(M):
            if arr[y][x]:
                cells[(y,x)] = [arr[y][x],1,arr[y][x]] # 현재, status, 고정
    go(cells,K)