N = int(input())
arr = list(map(int,input().split()))
result = 0
dp = [0]*N
for i in range(N):
  mx = 0
  for j in range(i):
    if arr[j] < arr[i]:
      dp[i] = max(mx,dp[j])
  dp[i] = mx +1
  result = max(result,dp[i])
  print(dp)
print(result)