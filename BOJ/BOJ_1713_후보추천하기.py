N = int(input())
M = int(input())
student = list(map(int,input().split()))
result = []
for s in student:
  for i in range(len(result)):
    ## 있으면 추천수 + 1
    if result[i][0] == s:
      result[i][1] += 1
      break
  else:
    ## 없는데 꽉참
    if len(result) == N:
      out = [1000,N+1]
      for i in range(N):
        if result[i][1] < out[0]:
          out = [result[i][1],i]
      result.pop(out[1])
    result.append([s,1])
print(*sorted(map(lambda x:x[0],result)))