N = int(input())
arr = [[[0] * (2**10) for _ in range(10)] for _ in range(N)]
for i in range(1,10):
  arr[0][i][2**i] = 1

for i in range(1,N):
  for n in range(10):
    for m in range(2**10):
      if m & 2**n:
        if n > 0:
          arr[i][n][m] += arr[i-1][n-1][m]
        if n+1<10:
          arr[i][n][m] += arr[i-1][n+1][m]
        arr[i][n][m] %= 1000000000
      else:
        if n > 0:
          arr[i][n][m+(2**n)] += arr[i-1][n-1][m]
        if n + 1 < 10:
          arr[i][n][m+(2**n)] += arr[i-1][n+1][m]
        arr[i][n][m+(2**n)] %= 1000000000
print(sum(map(lambda x:x[-1],arr[-1])) % 1000000000)