N, K = map(int,input().split())
ans = 1
K -= 1
if K > N - K:
  K = N-K
while K:
  ans = (ans * (N+1) // K ) % 100000000
  N += 1
  K -= 1
print(ans)

3 3
0 0 3
0 1 2
0 2 1
0 3 0
1 0 2
1 1 1
1 2 0
2 0 1
2 1 0
3 0 0