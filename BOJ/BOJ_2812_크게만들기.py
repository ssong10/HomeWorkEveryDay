for _ in range(int(input())):
  N = int(input())
  arr = list(map(int,input().split()))
  tmp = [arr[0],0]
  for i in range(N):
    if arr[i] > tmp[0]:
      tmp = [arr[i],i]
  multi, div = 0,0
  while N >1:
    d = N % 2
    multi += 1
    div += d
    N = N//2 + d
  answer = 0
  print(multi,div)
  for i in range(len(arr)):
    if i == tmp[1]:
      answer += arr[i] * (2** (multi-div-1))
    else:
      answer += arr[i] * (2 ** (multi-1))
    print(answer)
  print('-----')
# 15 -> 7쌍 1 -> 4