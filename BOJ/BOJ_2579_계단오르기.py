N = int(input())
step = [int(input()) for _ in range(N)]
dp = [0]*N
if N>1:
    dp[1] = step[0]+step[1]
for i in range(2,N):
    dp[i] = max(dp[i-2]+step[i], dp[i-3]+step[i-1]+step[i])
print(dp[-1])