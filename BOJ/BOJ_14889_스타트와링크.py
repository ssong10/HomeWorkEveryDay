N = int(input())

score = [list(map(int,input().split())) for _ in range(N)]
total = sum(map(sum,score))
result = total
for i in range(1<<N):
  # i range(16)
  start, link = [], []
  for j in range(N):
    # (0,1,2,3)
    if i & (1<<j):
      (0000 ~ 1111) & (1, 10, 100 ,1000)
      1011 -> 1000, 10 , 1
      [1,2] [3,4]
      start.append(j)
    else:
      link.append(j)
  if len(start) == N//2:
    answer = 0
    for i in start:
      for j in start:
        answer += score[i][j]
    for i in link:
      for j in link:
        answer -= score[i][j]
    result = min(result, abs(answer))

print(result)
