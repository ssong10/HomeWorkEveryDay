def back(dir,minsum):
    global result
    if dir == [N-1,N-1]:
        result = min(result,minsum)
    elif minsum < result:
        [y,x] = dir
        for d in range(2):
            if y+dy[d] < N and x+dx[d] < N:
                back([y+dy[d],x+dx[d]],minsum+board[y+dy[d]][x+dx[d]])

for tc in range(int(input())):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    result = 10 ** 6
    dy,dx = [1,0] ,[0,1]
    back([0,0],board[0][0])
    print('#{} {}'.format(tc+1,result))