def back(n):
    global result
    if n == N:
        result += 1
    else:
        for x in range(N):
            if not board[n][x]:
                tmp = []
                for move in range(N-n):
                    for d in [-1,0,1]:
                        if -1 < x+d*move < N and not board[n+move][x+d*move]:
                            tmp.append([n+move, x+d*move])
                for [y,x] in tmp:
                    board[y][x] = 1
                back(n+1)
                for [y,x] in tmp:
                    board[y][x] = 0
N= int(input())
board = [[0] * N for _ in range(N)]
result = 0
back(0)
print(result)
