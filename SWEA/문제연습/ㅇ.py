dy,dx = [-1,1,0,0], [0,0,-1,1]
def time():
    virus[-1] = virus[-1] | virus[0]
    virus[0] = set([])
    for idx,val in virus[1].items():
        if idx == 1:
            for v in val:
                (y,x) = v
                for d in range(4):
                    yy,xx = y+dy[d],x+dx[d]
                    if (yy,xx) not in virus[-1]:
                        for v in virus[1].items():
                            if (yy,xx) in v:
                                break
                        else:
                            virus[0].add((yy,xx))
            virus[1][1] = set([])
        else:
            virus[1][idx-1] = virus[1][idx]
            virus[1][idx] = set([])

for tc in range(int(input())):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    virus = {-1:set([]),0:set([]),1:dict()} # 죽,활,비활
    for y in range(N):
        for x in range(M):
            if arr[y][x]:
                n = arr[y][x] 
                if n in virus[1].keys():
                    virus[1][n].add((y,x))
                else:
                    virus[1][n] = set([(y,x)])
    time()
    print(virus)
    