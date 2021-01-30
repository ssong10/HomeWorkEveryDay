T = int(input())
arr = [0,1,2,4]
for _ in range(T):
  n = int(input())
  if len(arr)<n+1:
    for _ in range(n+1-len(arr)):
      arr.append(arr[-3]+arr[-2]+arr[-1])
  print(arr[n])
