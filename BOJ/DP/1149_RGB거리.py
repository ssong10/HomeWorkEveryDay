N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0,0,0] for _ in range(N)]
dp[0] = arr[0]
for i in range(1,N):
    for j in range(3):
        tmp = []
        for k in range(3):
            if not k == j:
                tmp.append(dp[i-1][k])
        dp[i][j] = min(tmp) + arr[i][j]
print(min(dp[N-1]))