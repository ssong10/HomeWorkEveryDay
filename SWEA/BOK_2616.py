def check():
    result = []
    for y in range(19):
        for x in range(19):
            a = game[y][x]
            if a != 0:
                for d in range(4):
                    tmp = 0
                    for move in range(1,5):
                        if -1< y+(dy[d] * move)< 19 and -1 < x+ (dx[d] * move) < 19 and game[y+(dy[d] * move)][x+ (dx[d] * move)] == a:
                            tmp +=1
                        else:
                            break      
                    if -1< y+(dy[d] * 5)< 19 and -1 < x+ (dx[d] *5) < 19:
                        if game[y+(dy[d] * 5)][x+ (dx[d] * 5)] != a:
                            tmp += 1
                    else:
                        tmp += 1
                    if -1< y-dy[d]< 19 and -1 < x-dx[d] < 19:
                        if game[y-dy[d]][x-dx[d]] != a:
                            tmp += 1
                    else:
                        tmp +=1
                    if tmp == 6:
                        result.append([a,y,x])
    if result:
        print(result[0][0])
        print(result[0][1]+1, result[0][2]+1)
    else:
        print(0)

game = []
for _ in range(19):
    game.append(list(map(int,input().split())))
dy=[-1,0,1,1]
dx=[1,1,1,0]
win = 0
check()