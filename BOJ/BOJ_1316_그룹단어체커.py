def checker(word):
  prev = ''
  char = set()
  for w in word:
    if prev != w and w in char:
      return False
    char.add(w)
    prev = w
  return True

N = int(input())
answer = 0
for _ in range(N):
  word = input()
  if checker(word):
    answer += 1
print(answer)