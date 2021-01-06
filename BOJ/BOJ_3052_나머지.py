numlist = [0] * 42
for _ in range(10):
  numlist[int(input()) % 42] += 1
answer = 0
for num in numlist:
  if num:
    answer += 1
print(answer)