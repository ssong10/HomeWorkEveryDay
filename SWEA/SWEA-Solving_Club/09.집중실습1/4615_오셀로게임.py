dy,dx = [-1,-1,-1,0,0,1,1,1] , [-1,0,1,-1,1,-1,0,1]
for tc in range(int(input())):
    N,M = map(int,input().split())
    turns = []
    for _ in range(M):
        turns.append(list(map(int,input().split())))
    game = [[0 for _ in range(N)] for _ in range(N)]
    game[N//2-1][N//2-1], game[N//2][N//2] = 2,2
    game[N//2][N //2-1], game[N//2-1][N//2] = 1,1
    for turn in turns:
        y, x ,c = turn[0]-1 , turn[1]-1 , turn[2]
        game[y][x] = c
        for d in range(8):
            tmp = []
            for m in range(1, N):
                yy ,xx = y + dy[d] * m, x + dx[d]*m
                if -1< yy< N and -1 < xx < N and game[yy][xx]:
                    tmp.append(game[yy][xx])
                else:
                    break
            if turn[2] == 1:
                if 1 in tmp:
                    for i in range(len(tmp)):
                        if tmp[i] == 2:
                            game[y+dy[d]*(i+1)][x+dx[d]*(i+1)] = 1
                        else:
                            break
            else:
                if 2 in tmp:
                    for i in range(len(tmp)):
                        if tmp[i] == 1:
                            game[y+dy[d]*(i+1)][x+dx[d]*(i+1)] = 2
                        else:
                            break
        for g in game:
            print(g)
        print('-----------------')
    b,w =0,0
    for i in game:
        for j in i:
            if j ==1:
                b+=1
            if j == 2:
                w +=1
    print('#{} {} {}'.format(tc+1,b,w))

