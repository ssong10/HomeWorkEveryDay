MIN , MAX = map(int,input().split())
total = [True] * (MAX-MIN+1)
answer = len(total)
root = int(MAX**0.5)+1
sosu = [False]*2+ [True] * (root-1)
for i in range(2,root+1):
  if sosu[i]:
    for j in range(2*i,root+1,i):
      sosu[j] = False
    s = i**2
    start = -(MIN%s)
    if start:
      start += s
    for j in range(start,MAX-MIN+1,s):
      total[j] = False
print(sum(total))