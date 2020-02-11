dy, dx = [-1,0,1,0] , [0,1,0,-1]

N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
go = list(map(int,input().split()))
voyager,results = False, [0] * 4
for d in range(4):
    visit = [[[0,0,0,0] for _ in range(M)] for _ in range(N)]
    if voyager:
        break
    flag = False
    tmp = 0
    y,x,dd = go[0]-1,go[1]-1,d
    while not flag:
        visit[y][x][dd] = 1
        yy ,xx = y+dy[dd],x+dx[dd]
        if -1 < yy< N and -1 < xx <M:
            if visit[yy][xx][dd]:
                voyager = True
                flag = True
            elif arr[yy][xx] == 'C':
                flag = True
            elif arr[yy][xx] == '/':
                if dd == 0:
                    dd = 1
                elif dd == 1:
                    dd = 0
                elif dd == 2:
                    dd=3
                elif dd == 3:
                    dd=2
            elif not arr[yy][xx] =='.':
                if dd == 0:
                    dd = 3
                elif dd == 1:
                    dd = 2
                elif dd == 2:
                    dd = 1
                elif dd == 3:
                    dd = 0
            y,x,dd = yy,xx,dd
        else:
            flag = True
        tmp += 1
    results[d] = tmp
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