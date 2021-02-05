N = int(input())
arr = list(map(int,input().split()))
answer = max(arr)
tmp = 0
for i in range(N):
  if tmp + arr[i] > 0:
    tmp += arr[i]
    answer = max(tmp,answer)
  else:
    tmp = 0

print(answer)