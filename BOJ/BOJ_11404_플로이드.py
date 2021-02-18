n = int(input())
m = int(input())
INF = 2**100
arr = [[INF]*n for _ in range(n)]
for i in range(m):
  i,j,v = map(int,input().split())
  arr[i-1][j-1] = min(arr[i-1][j-1],v)

for i in range(n):
  for s in range(n):
    if i != s:
      for e in range(n):
        if s != e and arr[s][i] + arr[i][e] < arr[s][e]:
          arr[s][e] = arr[s][i] + arr[i][e]
for i in range(n):
  print(*map(lambda x:0 if x==INF else x,arr[i]))