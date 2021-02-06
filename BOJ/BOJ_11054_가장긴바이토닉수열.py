N = int(input())
arr = list(map(int,input().split()))
left = [0] * N
right = [0] * N
for i in range(N):
  ii = -1-i
  tmp = [0,0]
  for j in range(i):
    if arr[j] < arr[i] and tmp[0] < left[j]:
      tmp[0] = left[j]
    jj = -j-1
    if arr[jj] < arr[ii] and tmp[1] < right[jj]:
      tmp[1] = right[jj]
  left[i] = tmp[0] + 1
  right[ii] = tmp[1] + 1
answer = 0
for i in range(N):
  answer = max(answer,left[i]+right[i]-1)
print(answer)