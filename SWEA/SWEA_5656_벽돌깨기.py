from collections import deque
def drop(box,x,N):
    global result
    copybox = [[0]*W for _ in range(H)]
    for yy in range(H):
        for xx in range(W):
            copybox[yy][xx] = box[yy][xx]
    bomblist = deque()
    for y in range(H):
        if copybox[y][x]:
            bomblist.append([y,x])
            break
    while bomblist:
        for _ in range(len(bomblist)):
            [y,x]=bomblist.popleft()
            lenght = copybox[y][x]
            copybox[y][x] = 0
            for i in range(lenght):
                if x+i< W and copybox[y][x+i]:
                    bomblist.append([y,x+i])
                if -1< x-i and copybox[y][x-i]:
                    bomblist.append([y,x-i])
                if y+i < H and copybox[y+i][x]:
                    bomblist.append([y+i,x])
                if -1 < y-i and copybox[y-i][x]:
                    bomblist.append([y-i,x])
 
    for _ in range(H):
        for y in range(H-1):
            for x in range(W):
                if copybox[y][x] and not copybox[y+1][x]:
                    copybox[y][x],copybox[y+1][x] = copybox[y+1][x],copybox[y][x]
    if N == 1:
        ans = 0
        for y in range(H):
            for x in range(W):
                if copybox[y][x]:
                    ans += 1
        result = min(ans,result)
        return
    else:
        for x in range(W):
            drop(copybox,x,N-1)
 
for tc in range(int(input())):
    result = 10**6
    N,W,H = map(int,input().split())
    box = [list(map(int,input().split())) for _ in range(H)]
    for x in range(W):
        drop(box,x,N)
    print(f'#{tc+1} {result}')