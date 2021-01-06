num = 1
for i in range(3):
  num = num * int(input())
numlist = [0]*10
for s in str(num):
  numlist[int(s)] += 1
for n in numlist:
  print(n)