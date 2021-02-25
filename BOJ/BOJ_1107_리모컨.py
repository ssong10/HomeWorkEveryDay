def diff(answer):
  return abs(intNum - answer)

def comb(n,answer):
  global result
  if n == len(nums):
    if result > len(str(answer)) + diff(answer):
      result = len(str(answer)) + diff(answer)
    return
  for i in tmp[n]:
    comb(n+1,answer*10+i)

nums = input()
intNum = int(nums)
n = int(input())
wrong = [True] * 10
if n:
  for wrongNum in map(int,input().split()):
    wrong[wrongNum] = False
tmp = [set() for _ in range(len(nums))]
for i in range(len(nums)):
  for j in range(10):
    if wrong[j]:
      tmp[i].add(j)
      
result = diff(100)
minnum = ''
for i in range(1,10):
  if wrong[i]:
    minnum += str(i)
    break
if minnum:
  if wrong[0]:
    minnum += '0'*len(nums)
  else:
    minnum *= (len(nums)+1)
  result = min(result,len(minnum)+diff(int(minnum)))
for i in range(9,-1,-1):
  if wrong[i]:
    maxnum = str(i)*(len(nums)-1)
    if maxnum:
      result = min(result,len(maxnum)+diff(int(maxnum)))
    break
comb(0,0)
print(result)