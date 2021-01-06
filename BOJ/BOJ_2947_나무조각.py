arr = list(map(int,input().split()))
for _ in range(4):
  for i in range(4):
      if arr[i] > arr[i+1]:
        arr[i],arr[i+1] = arr[i+1],arr[i]
        print(*arr)