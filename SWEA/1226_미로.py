from collections import deque
dy,dx = [-1,1,0,0], [0,0,-1,1]

def dfs(tmp):
    global result
    while tmp:
        for i in range(len(tmp)):
            [y,x] = tmp.popleft()

            for d in range(4):
                yy,xx = y+dy[d] ,x+dx[d]
                if -1<yy<16 and -1<xx<16 and miro[yy][xx] == '0' and not visit[yy][xx]:
                    tmp.append([yy,xx])
                    visit[yy][xx] = 1
                if -1 < yy < 16 and -1 < xx < 16 and miro[yy][xx] == '3':
                    result = 1
                    return

for tc in range(1,11):
    tc = int(input())
    miro = [list(input()) for _ in range(16)]
    visit = [[0]*16 for _ in range(16)]
    result = 0
    for y in range(16):
        for x in range(16):
            if miro[y][x] == '2':
                tmp = deque([[y,x]])
                dfs(tmp)
    print('#{} {}'.format(tc,result))