dir = [[-1,0],[1,0],[0,1],[0,-1]]

def next(y,x,d):
    yy,xx = y+dir[d][0],x+dir[d][1]
    if yy == -1:
        yy = N-1
    elif yy == N:
        yy = 0
    if xx == -1:
        xx = M-1
    elif xx == M:
        xx = 0
    return yy,xx

def move(y,x,d,memory):
    global result,visit
    if arr[y][x] =='@':
        result = 'YES'
        return
    if result =='YES':
        return
    yy,xx = next(y,x,d)
    a = arr[yy][xx]
    if a == "<":
        d = 3
    elif a == '>':
        d = 2
    elif a == '^':
        d = 0
    elif a == 'v':
        d = 1
    elif a == '_':
        if memory:
            d = 3
        else:
            d = 2
    elif a == '|':
        if memory:
            d = 0
        else:
            d = 1
    elif a == '?':
        for dd in range(4):
            tmp = next(yy,xx,dd)
            if not (y == tmp[0] and x ==tmp[1]):
                if memory not in visit[tmp[0]][tmp[1]]:
                    visit[tmp[0]][tmp[1]].add(memory)
                    move(tmp[0],tmp[1],dd,memory)
        return
    elif a == '.':
        pass
    elif a == '@':
        result = 'YES'
        return
    elif a == '+':
        if memory == 15:
            memory = 0
        else:
            memory += 1
    elif a == '-':
        if memory:
            memory -= 1
        else:
            memory = 15
    else:
        memory = int(a)
    if memory not in visit[yy][xx]:
        visit[yy][xx].add(memory)
        move(yy,xx,d,memory)

for tc in range(int(input())):
    result = 'NO'
    N,M = map(int,input().split())
    arr = list(input() for _ in range(N))
    visit = [[set() for _ in range(M)] for _ in range(N)]
    num = int(arr[0][0]) if arr[0][0].isdigit() else 0 
    move(0,0,2,num)
    print(f'#{tc+1} {result}')
