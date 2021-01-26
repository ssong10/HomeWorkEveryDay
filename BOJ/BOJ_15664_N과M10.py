def back(tmp,n):
  if len(tmp) == M:
    print(*tmp)
    return
  prev = -1
  for i in range(n,N):
    if prev != arr[i] and not visit[i]:
      prev = arr[i]
      visit[i] = True
      back(tmp+[arr[i]],i+1)
      visit[i] = False

N , M = map(int,input().split())
arr = sorted(map(int,input().split()))
visit = [False] * N
back([],0)