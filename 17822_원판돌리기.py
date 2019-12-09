from collections import deque
N, M, T = map(int,input().split())
pan = [deque(map(int,input().split())) for _ in range(N)]
spins = [list(map(int,input().split())) for _ in range(T)]
dy,dx = [-1,1,0,0] , [0,0,-1,1]
for spin in spins:
    for i in range(N):
        if not (i+1) % spin[0] :
            if spin[1]:
                for _ in range(spin[2]):
                    pan[i].append(pan[i].popleft())
            else:
                for _ in range(spin[2]):
                    pan[i].appendleft(pan[i].pop())
    same = set()
    for y in range(N):
        for x in range(M):
            if pan[y][x]:
                for d in range(4):
                    yy,xx = y+dy[d],x+dx[d]
                    if -1< yy< N and xx < M and pan[y][x] == pan[yy][xx]:
                        if xx == -1:
                            xx = M-1
                        same.add((y,x))
                        same.add((yy,xx))
    for yx in same:
        pan[yx[0]][yx[1]] = 0
    result,cnt = 0,0
    for y in range(N):
        for x in range(M):
            if pan[y][x]:
                result += pan[y][x]
                cnt += 1
    if not same:
        avg = result/cnt
        result = 0
        for y in range(N):
            for x in range(M):
                if pan[y][x]:
                    if pan[y][x] > avg:
                        pan[y][x] -= 1
                    elif pan[y][x] < avg:
                        pan[y][x] += 1
                    result += pan[y][x]
print(result)
