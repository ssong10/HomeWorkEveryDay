def attach(y,x,R,C):
    for dy in range(R):
        for dx in range(C):
            if notebook[y+dy][x+dx] and stk[dy][dx]:
                return False
    return True


def position():
    for y in range(N-R+1):
        for x in range(M-C+1):
            if attach(y,x,R,C):
                for yy in range(R):
                    for xx in range(C):
                        if stk[yy][xx]:
                            notebook[y+yy][x+xx] = 1
                return True
    return False

N, M, K = map(int,input().split())
notebook = [[0] * M for _ in range(N)]
for _ in range(K):
    R, C = map(int,input().split())
    stk = [list(map(int,input().split())) for _ in range(R)]
    
    for _ in range(4):
        if position():
            break
        else:
            R,C = C,R
            tmp = [[0] * C for _ in range(R)]
            for y in range(C):
                for x in range(R):
                    tmp[x][C-1-y] = stk[y][x]
            stk = tmp
print(sum(map(sum,notebook)))