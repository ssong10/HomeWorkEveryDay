N, M = map(int,input().split())
for i in range(min(N,M),0,-1):
  if not (N % i) and not (M%i):
    break

print(i)
print(N*M//i)