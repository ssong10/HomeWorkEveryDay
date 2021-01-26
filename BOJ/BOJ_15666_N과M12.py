def back(tmp,n):
  if len(tmp) == M:
    print(*tmp)
    return
  prev = -1
  for i in range(n,N):
    if prev != arr[i]:
      prev = arr[i]
      back(tmp+[arr[i]],i)

N , M = map(int,input().split())
arr = sorted(map(int,input().split()))
back([],0)