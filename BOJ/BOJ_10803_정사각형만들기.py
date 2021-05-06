import sys
sys.setrecursionlimit(10**8)
INF = 10**10
n, m = map(int,input().split())
def find(y,x):
  if y < x :
    y,x = x,y
  if not y % x:
    dp[y][x] = y//x
  if dp[y][x] != INF:
    return dp[y][x]
  dp[y][x] = min(dp[y][x],1 + find(y-x,x))
  if y >= x*3:
    dp[y][x] = min(dp[y][x],find(y-x,x)+1)
  else:
    for i in range(1,x//2+1):
      a = find(y,x-i)
      b = find(y,i)
      dp[y][x] = min(dp[y][x],a+b)
    for i in range(1,y//2+1):
      a = find(y-i,x)
      b = find(i,x)
      dp[y][x] = min(dp[y][x],a+b)
  return dp[y][x]
dp = []
if n < m :
  n,m = m,n
for i in range(n+1):
  dp.append([INF]*(m+1))
find(n,m)
print(dp[-1][-1])
