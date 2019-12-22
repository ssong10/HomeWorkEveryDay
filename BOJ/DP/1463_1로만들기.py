N = int(input())
tmp = 0
dp = [0] * (N+1)
dp[1] = 0
for i in range(2,N+1):
    if not i % 3:
        dp[i] = min(dp[i//3],dp[i-1]) + 1
    elif not i % 2:
        dp[i] = min(dp[i//2],dp[i-1]) + 1
    else:
        dp[i] = dp[i-1]+ 1
print(dp[-1])
