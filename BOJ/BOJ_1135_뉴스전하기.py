def time(n):
  MAX = 0
  tmp = []
  for next_n in child[n]:
    tmp.append(time(next_n))
  tmp.sort(reverse=True)
  for i in range(len(tmp)):
    MAX = max(MAX,tmp[i]+i+1)
  return MAX

N = int(input())
arr = list(map(int,input().split()))
child = [[] for _ in range(N)]
for i in range(len(arr)):
  if arr[i] > -1:
    child[arr[i]].append(i)
answer = time(0)
print(answer)