def drop(i):
    for y in range(H):
        if arr[y][i]:
            n = arr[y][i]
            bomb = [y,i,n]
            break
    bomblist.append(bomb)
    for y in range(bomb[0]-n+1,bomb[0]+n-1):
        if -1 < y < H:
            if y != bomb[0] and arr[y][i]:
                bomblist.append([y,i,arr[y][i]])
    for x in range(i-n+1,i+n-1):
        if -1 < x < W:
            if x != i and arr[bomb[0]][x]:
                bomblist.append([bomb[0],x,arr[bomb[0]][x]])
    print(bomblist)

for tc in range(int(input())):
    N, W, H = map(int,input().split()) #  W, H | 가로, 세로
    arr = [list(map(int,input().split())) for _ in range(H)]
    for i in range(W):
        bomblist = []
        drop(i)