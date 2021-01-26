def comb(tmp,n):
  if len(tmp) == M:
    print(*tmp)
    return
  for i in range(N):
    comb(tmp+[arr[i]],i)

N, M = map(int,input().split())
arr = sorted(map(int,input().split()))
comb([],0)