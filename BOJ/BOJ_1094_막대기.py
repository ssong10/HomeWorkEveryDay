N = int(input())
answer = 0
for i in range(7):
  if (1<<i & N):
    answer += 1
print(answer)