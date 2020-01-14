from collections import deque
def pick(n,tmp):
    if len(tmp) == M:
        virus(tmp)
        return
    for i in range(n,len(vs)):
        if not visit[i]:
            visit[i] = 1
            tmp.append(i)
            pick(i,tmp)
            tmp.pop()
            visit[i] = 0

def virus(tmp):
    global result,chk, tot
    visited = [[0] * N for _ in range(N)]
    n,time = 0,0
    Q = deque()
    for t in tmp:
        Q.append(vs[t])
    while Q:
        time += 1
        if time > result:
            return
        for _ in range(len(Q)):
            y,x = Q.popleft()
            for d in range(4):
                yy, xx = y+dy[d],x+dx[d]
                if -1 <yy < N and -1<xx < N and arr[yy][xx] != 1 and not visited[yy][xx]:
                    Q.append((yy,xx))
                    visited[yy][xx] = 1
                    if not arr[yy][xx]:
                        n += 1
        if n == tot:
            chk = True
            result = min(time,result)
            return 


N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
vs,tot = [],0
for y in range(N):
    for x in range(N):
        if arr[y][x] == 2:
            vs.append((y,x))
        elif arr[y][x] == 0:
            tot += 1
result,chk = 10**5,False
visit = [0] * (len(vs))
dy,dx = [-1,1,0,0],[0,0,-1,1]
if not tot:
    print(0)
else:
    pick(0,[])
    if chk:
        print(result)
    else:
        print(-1)
