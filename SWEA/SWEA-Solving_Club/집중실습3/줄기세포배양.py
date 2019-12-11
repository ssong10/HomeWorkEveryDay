dy,dx = [-1,1,0,0], [0,0,-1,1]
def time():
    new = dict()
    for idx,val in virus.items():
        if val[0] != -1:
            if val[0] == 0:
                (y,x) = idx
                for d in range(4):
                    yy,xx = y+dy[d],x+dx[d]
                    if (yy,xx) not in virus.keys():
                        if (yy,xx) in new.keys():
                            new[(yy,xx)] = max(val[1],new[(yy,xx)])
                        else:
                            new[(yy,xx)] = val[1]
            if val[2] == 1:
                val[2] = val[1]
                val[0] -= 1
            else:
                val[2] -= 1
    for idx,val in new.items():
        virus[idx[0],idx[1]] = [1,val,val]
 
for tc in range(int(input())):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    virus = {}
    for y in range(N):
        for x in range(M):
            if arr[y][x]:
                virus[(y,x)] = [1,arr[y][x],arr[y][x]] # [상태,파워,남은시간]
    for _ in range(K):
        time()
    result = 0
    for v in virus.values():
        if v[0] != -1:
            result += 1
    print(f'#{tc+1} {result}')