N = int(input())
step = [int(input()) for _ in range(N)]

dp = [[0]*N for _ in range(3)]
dp[1][0] = step[0]

for i in range(1, N):
    dp[0][i] = max(dp[1][i-1],dp[2][i-1])
    dp[1][i] = dp[0][i-1]+step[i]
    dp[2][i] = dp[1][i-1]+step[i]
print(max(dp[1][-1],dp[2][-1]))