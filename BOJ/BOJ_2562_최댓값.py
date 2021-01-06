answer ,MAX = 0, 0
for i in range(9):
  num = int(input())
  if num > MAX:
    answer = i+1
    MAX = num
print(MAX)
print(answer)