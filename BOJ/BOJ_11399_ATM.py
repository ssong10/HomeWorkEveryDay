N = int(input())
arr = sorted(map(int,input().split()))
tmp = [0]
for i in range(N):
  tmp.append(tmp[-1]+arr[i])
print(sum(tmp))