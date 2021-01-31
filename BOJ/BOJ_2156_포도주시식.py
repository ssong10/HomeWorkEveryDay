N = int(input())
step = [0,0,0] + [int(input()) for _ in range(N)]

dp = [0] * (N+3)
for i in range(N):
  dp[i+3] = max(dp[i]+step[i+2]+step[i+3], dp[i+1]+step[i+3],dp[i+2])
print(dp[-1])