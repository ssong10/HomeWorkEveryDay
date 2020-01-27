dir = [(1,1),(1,-1),(-1,-1),(-1,1)]
def move(move_dir):
    [a,b,c,d] = move_dir
    for y in range(N):
        for x in range(N):
            if y < N-b-c and -1+d < x < N-a:
                eat(y,x,move_dir)
            if chk:
                return
             
def eat(y,x,move_dir):
    global result,chk
    tmp = set()
    for d in range(4):
        for _ in range(move_dir[d]):
            y += dir[d][0]
            x += dir[d][1]
            if desserts[y][x] in tmp:
                return
            else:
                tmp.add(desserts[y][x])
    result = max(len(tmp),result)
    chk = True
        
for tc in range(int(input())):
    N = int(input())
    desserts = [list(map(int,input().split())) for _ in range(N)]
    result = -1
    chk = False
    for k in range(N-1,1,-1):
        for i in range(1,k):
            move([i,k-i]*2)
    print(f'#{tc+1} {result}')