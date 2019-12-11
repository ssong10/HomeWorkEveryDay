from collections import deque

def wave(sands):
    global result
    crush = []
    for _ in range(len(sands)):
        [y,x,n] = sands.popleft()
        tmp = 0
        for d in range(8):
            if arr[y + dy[d]][x + dx[d]] == 0:
                tmp += 1
        if tmp >= n:
            crush.append([y,x,n])
        else:
            sands.append([y,x,n])
    if crush:
        for c in crush:
            arr[c[0]][c[1]] = 0
        wave(sands)
        result += 1
    else:
        return

for tc in range(int(input())):
    H,W = map(int,input().split())
    arr = [list(input()) for _ in range(H)]
    sands = deque([])
    dy,dx = [-1,0,1,-1,1,-1,0,1],[-1,-1,-1,0,0,1,1,1]
    for y in range(H):
        for x in range(W):
            if arr[y][x].isdigit() and int(arr[y][x]) < 9 :
                tmp = 0
                for d in range(8):
                    if arr[y+dy[d]][x+dx[d]] == '.':
                        tmp += 1
                n = int(arr[y][x])-tmp
                if n > 0 :
                    sands.append([y, x, int(arr[y][x])-tmp])
                else:
                    arr[y][x] = 0
    result = 1
    wave(sands)
    print(result)
