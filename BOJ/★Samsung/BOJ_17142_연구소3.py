def pick(n,tmp):
    if len(tmp) == M:
        virus(set(),tmp,0)
        return
    for i in range(n,len(vs)):
        if not visit[i]:
            visit[i] = 1
            tmp.append(vs[i])
            pick(i,tmp)
            tmp.pop()
            visit[i] = 0

def virus(all_v,tmp,n):
    global result,chk
    if n >= result:
        return
    if all_v == tot:
        chk = True
        result = min(result,n)
        return
    next_v = []
    for y,x in tmp:
        for d in range(4):
            yy, xx = y+dy[d],x+dx[d]
            if -1 <yy < N and -1<xx < N and arr[yy][xx] != 1 and (yy,xx) not in all_v:
                next_v.append((yy,xx))
                if arr[yy][xx] == 0:
                    all_v.add((yy,xx))
    if next_v:
        virus(all_v,next_v,n+1)


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
vs,tot = [],set()
for y in range(N):
    for x in range(N):
        if arr[y][x] == 2:
            vs.append((y,x))
        elif arr[y][x] == 0:
            tot.add((y,x))
result,chk = 10**5,False
visit = [0] * (len(vs))
dy,dx = [-1,1,0,0],[0,0,-1,1]
pick(0,[])
if chk:
    print(result)
else:
    print(-1)