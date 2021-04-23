N = int(input())
idx = {}
total = []
tmp = 0
for _ in range(N):
  string = input()
  n = len(string)
  for i in range(n):
    s = string[i]
    if s not in idx:
      idx[s] = tmp
      total.append(0)
      tmp += 1
    total[idx[s]] += 10 ** (n-i-1)
result = 0
total.sort()
for i in range(len(total)):
  a = total.pop()
  result += a * (9-i)
print(result)