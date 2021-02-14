def back(i,tmp):
  if i == N:
    if len(tmp) == 6:
      print(*tmp)
    return
  back(i+1,tmp+[nums[i]])
  back(i+1,tmp)

while True:
  arr = list(map(int,input().split()))
  if arr[0] == 0:
    break
  N = arr[0]
  nums = arr[1:]
  visited = [False] * len(nums)
  back(0,[])
  print()