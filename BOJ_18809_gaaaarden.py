N, M, G, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
seed = {}
for y in range(N):
    for x in range(M):
        if arr[y][x] == 1:
            seed[(y,x)] = [0]
print(seed)