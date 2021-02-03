import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [0]*(N+1)

for i in range(1,N+1):
  [t,p] = arr[i-1]
  dp[i] = max(dp[i],dp[i-1])
  if i+t-1 <= N:
    dp[i+t-1] = max(dp[i-1]+p,dp[i+t-1])
print(dp[-1])