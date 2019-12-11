from collections import deque
def BFS():
    time = 0
    while True:
        time +=1
        for _ in range(len(fire)):
            y,x = fire.popleft()
            for d in range(4):
                yy = y+dy[d]
                xx = x+dx[d]
                if -1 < yy < h and -1 < xx < w and (room[yy][xx] == '@' or room[yy][xx] == '.'):
                    room[yy][xx] = '*'
                    fire.append([yy,xx])
        if man:
            for _ in range(len(man)):
                y,x = man.popleft()
                if y == 0 or y == h - 1 or x == 0 or x == w - 1:
                    return time
                for d in range(4):
                    yy = y+dy[d]
                    xx = x+dx[d]
                    if -1 < yy < h and -1 < xx < w and room[yy][xx] == '.':
                        room[yy][xx] = '@'
                        man.append([yy,xx])
        else:
            return 'IMPOSSIBLE'

for tc in range(int(input())):
    w,h = map(int,input().split())
    room = []
    dy,dx = [-1,1,0,0], [0,0,-1,1]
    for _ in range(h):
        room.append(list(input()))
    fire = deque([])
    man = deque([])
    for i in range(h):
        for j in range(w):
            if room[i][j] == '*':
                fire.append([i,j])
            if room[i][j] == '@':
                man.append([i,j])
    print(BFS())