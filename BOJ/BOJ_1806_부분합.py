N, M = map(int,input().split())
nums = list(map(int,input().split()))
answer = N
flag = False
tmp = 0
i,j = 0,0
while i < N:
  if tmp >= M:
    flag = True
    answer = min(answer,j-i)
  if tmp <= M and j < N:
    tmp += nums[j]
    j += 1
  else:
    tmp -= nums[i]
    i += 1
print(answer if flag else 0)