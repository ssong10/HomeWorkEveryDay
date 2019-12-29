def back(i):
    global result
    if chk():
        if not result[0] or result[1] >= i:
            result = [True,i]
    if i < 3:
        for y in range(1,N):
            for x in range(1,H+1):
                if not visit[N*(y-1)+(x-1)]:
                    if x not in j[y] or x not in j[y+1]:
                        visit[N*(y-1)+(x-1)] = 1
                        j[y].add(x)
                        back(i+1)
                        j[y].remove(x)
                        visit[N*(y-1)+(x-1)] = 0

def chk():
    for i in range(1,N+1):
        x, y, s = i, 0 , 0
        while y <= H:
            if s == 0 and y in j[x]:
                x += 1
                s = 1
            elif s == 0 and y in j[x-1]:
                x -= 1
                s = 1
            else:
                y += 1
                s = 0
        if i != x:
            return False
    return True

N, M, H = map(int,input().split())
j = [set() for _ in range(H+1)]
visit = [0]* (N-1)*H
for _ in range(M):
    a, b = map(int,input().split())
    j[b].add(a)
    visit[N*(b-1)+(a-1)] = 1
result = [False,0]
back(0)
if result[0]:
    print(result[1])
else:
    print(-1)