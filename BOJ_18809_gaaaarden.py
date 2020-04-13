def pick_g(i,p):
    for i in range(len(used)):
        if p == G:
            pick_r(0,0)
            return
        if not used[i]:
            used[i] = 1
            pick_g(i+1,p+1)
            used[i] = 0

def pick_r(i,p):
    for i in range(len(used)):
        if p == R:
            
            return
        if not used[i]:
            used[i] = 2
            pick_r(i+1,p+1)
            used[i] = 0

N, M, G, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
seed = {}
for y in range(N):
    for x in range(M):
        if arr[y][x] == 2:
            seed[(y,x)] = [0]

used = [0] * len(seed)
pick_g(0,0)
