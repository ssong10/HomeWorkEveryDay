N, K = map(int, input().split())
items = [list(map(int,input().split())) for _ in range(N)]
weight = [0] * K
for i in range(N):
  w, v = items[i]
  t = K-w
  while t:
    t -= 1
    weight[t] = v
  print(weight)