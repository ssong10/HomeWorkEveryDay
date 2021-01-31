N,M=map(int,input().split())
a=[False,False] + [True] * (M-1)
for i in range(2,int(M**0.5)+1):
  if a[i]:
    for j in range(i*2,M+1,i):
      a[j] = False
for i in range(N,M+1):
  if a[i]:
    print(i)