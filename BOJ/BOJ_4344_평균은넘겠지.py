C = int(input())
for _ in range(C):
  arr = list(map(int,input().split()))
  n, num = arr[0], arr[1:]
  avg = sum(num) / n
  over = 0
  for i in num:
    if avg < i:
      over += 1
  print(format(over/n * 100,".3f")+'%')