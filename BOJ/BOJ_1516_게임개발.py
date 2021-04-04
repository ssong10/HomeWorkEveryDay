from collections import deque
N = int(input())
builds = [[[],set()] for _ in range(N+1)]
tmp = deque()
result = [0] * N

for i in range(N):
  a = list(map(int,input().split()))
  builds[i+1][1] = set(a[1:-1])
  if len(a) == 2:
    tmp.append([i+1,a[0]])
    result[i] = a[0]
  for child in a[1:-1]:
    builds[child][0].append([i+1,a[0]])
while tmp:
  i,v = tmp.popleft()
  for n_i, n_v in builds[i][0]:
    builds[n_i][1].discard(i)
    result[n_i-1] = max(result[n_i-1], v+n_v)
    if not len(builds[n_i][1]):
      tmp.append([n_i,v+n_v])

for r in result:
  print(r)