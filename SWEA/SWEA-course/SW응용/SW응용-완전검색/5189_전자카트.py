def DFS(choice,n, sumA):
    global result
    if len(choice) == N and not choice[-1]:
        result = min(result,sumA)
    elif sumA < result:
        for i in range(N):
            if not i in choice and not n == i:
                choice.append(i)
                DFS(choice,i,sumA+board[n][i])
                choice.pop()

for tc in range(int(input())):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    result = 10 ** 6
    DFS([],0, 0)
    print('#{} {}'.format(tc+1,result))