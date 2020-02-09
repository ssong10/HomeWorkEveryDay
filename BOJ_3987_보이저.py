dy, dx = [-1,0,1,0] , [0,1,0,-1]
def signal(y,x,d,n):
    global voyager
    if voyager:
        return
    visit[y][x] = 1
    yy ,xx = y+dy[d],x+dx[d]
    if -1 < yy< N and -1 < xx <M:
        if visit[yy][xx]:
            voyager = True
            return
        elif arr[yy][xx] == 'C':
            return n
        elif arr[yy][xx] == '/':
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d=3
            elif d == 3:
                d=2
        elif not arr[yy][xx] =='.':
            if d == 0:
                d = 3
            elif d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 0
        return signal(yy,xx,d,n+1)
    else:
        return n

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
go = list(map(int,input().split()))
voyager,results = False, [0] * 4
for d in range(4):
    visit = [[0] * M for _ in range(N)]
    results[d] = signal(go[0]-1,go[1]-1,d,1)
if voyager:
    print('Voyager')
else:
    a = results.index(max(results))
    if a==0:
        print('U')
    elif a == 1:
        print('R')
    elif a == 2:
        print('D')
    else:
        print('L')
    print(max(results))