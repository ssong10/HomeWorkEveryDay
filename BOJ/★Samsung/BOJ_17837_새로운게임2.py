dy,dx = [0,0,-1,1],[1,-1,0,0]
def move(n):
    global result
    for i in range(M):
        find = False
        for dir,horses in position.items():
            for idx in range(len(horses)):
                j,d = horses[idx]
                if j == i:
                    y , x = dir[0] + dy[d-1],dir[1] + dx[d-1]
                    if not (-1 < y < N and -1 <x < N) or arr[y][x] == 2:
                        if d % 2:
                            horses[idx][1] += 1
                        else:
                            horses[idx][1] -= 1
                        d = horses[idx][1]
                        y , x = dir[0] + dy[d-1],dir[1] + dx[d-1]
                        if not (-1 < y < N and -1 <x < N) or arr[y][x] == 2:
                            y,x = dir
                    find = True
                    break
            if find:
                break
        if idx:
            position[dir] = horses[:idx]
        else:
            del position[dir]
        if arr[y][x] == 1:
            h = horses[idx:][::-1]
        else:
            h = horses[idx:]
        if (y,x) in position:
            position[(y,x)] += h
        else:
            position[(y,x)] = h
        if len(position[(y,x)]) >= 4:
            result = n+1
            return

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
position = {}
result = False
for i in range(M):
    y,x,d = map(int,input().split())
    position[(y-1,x-1)] = [[i,d]]
for n in range(1001):
    move(n)
    if result:
        break
if result:
    print(result)
else:
    print(-1)