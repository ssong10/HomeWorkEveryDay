N, K = map(int,input().split())
arr = [[1] + [0] * (K-1) for _ in range(N+1)]
for i in range(1,K): # i 개
  for j in range(N+1): # j 숫자
    for m in range(j+1):
      arr[j][i] += arr[j-m][i-1]
      arr[j][i] %= 1000000000
print(arr[-1][-1])