import sys
input = sys.stdin.readline
N, K = map(int, input().split())
items = []
for i in range(N):
  w,v = map(int,input().split())
  items.append([w,v])
weight = [[0] * (K+1) for _ in range(N+1)]
for i in range(1,N+1):
  for j in range(1,K+1):
    w,v = items[i-1]
    if w <= j:
      weight[i][j] = max(v + weight[i-1][j-w],weight[i-1][j])
    else:
      weight[i][j] = weight[i-1][j]
print(weight[N][K])