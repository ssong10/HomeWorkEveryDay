def chk(cnt,sqr,n):
    global tmp,y,x
    if cnt <= C:
        tmp = max(tmp, sqr)
        for i in range(M):
            if not used[i]:
                used[i] = 1
                chk(cnt+honey[y][x+i],sqr+(honey[y][x+i]**2),n+1)
                used[i] = 0

for tc in range(int(input())):
    N,M,C = map(int,input().split())
    honey = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    maxlist = []
    for y in range(N):
        line = []
        for x in range(N-M+1):
            tmp = 0
            used=[0]*M
            chk(0,0,0)
            line.append(tmp)
        maxlist.append(max(line))
        for x in range(N-M+1-M):
            for d in range(x+M,N-M+1):
                result=max(result,line[x]+line[d])
    print('#{} {}'.format(tc+1,max(sum(sorted(maxlist)[-2:]), result)))
