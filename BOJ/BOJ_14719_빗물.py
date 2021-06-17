N,M = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
l,r = 0,M-1
l_v,r_v = 0,0
while l < r:
  if arr[l] < arr[r]:
    if l_v < arr[l]:
      l_v = arr[l]
    else:
      answer += l_v - arr[l]
    l += 1
  else:
    if r_v < arr[r]:
      r_v = arr[r]
    else:
      answer += r_v - arr[r]
    r -= 1
print(answer)