for tc in range(int(input())):
    colors = []
    block = [[0]*10 for _ in range(10)]
    purple =0
    for _ in range(int(input())):
        colors.append(list(map(int,input().split( ))))
    for i in colors:
        for row in range(i[0],i[2]+1):
            for col in range(i[1],i[3]+1):
                    block[col][row] += i[4]
    for i in range(10):
        for j in range(10):
            if block[i][j] == 3:
                purple +=1
    print(f'#{tc+1} {purple}')