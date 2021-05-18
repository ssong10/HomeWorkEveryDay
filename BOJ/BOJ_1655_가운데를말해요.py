from heapq import heappush,heappop
N = int(input())
big = []
small = []
for i in range(N):
  num = int(input())
  if len(small) > len(big):
    heappush(small,-num)
    big_num = -heappop(small)
    heappush(big,big_num)
  else:
    heappush(big,num)
    small_num = heappop(big)
    heappush(small,-small_num)
  tmp = []
  if small:
    tmp.append(-small[0])
  if big:
    tmp.append(big[0])
  print(min(tmp))