N, K = map(int, input().split())
items = [list(map(int,input().split())) for _ in range(N)]
weight = [0] * K
for i in range(N):
  w, v = items[i]
  v += weight[w-1]
  for j in range(i,n):
    if (w+items[])
  print(weight)