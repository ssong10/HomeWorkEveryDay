N,K = map(int,input().split())
steps = list(map(int,input().split()))
robot = [False] * N
result = 0
while K > 0:
  result += 1
  # spin
  steps = [steps[2*N-1]] + steps[:2*N-1]
  robot = [False] + robot[:N-1]
  # rotate
  for i in range(N-1,-1,-1):
    if robot[i]:
      if i == N-1:
        robot[i] = False
      elif steps[i+1] and not robot[i+1]:
        robot[i] = False
        robot[i+1] = True
        steps[i+1] -= 1
        if steps[i+1] == 0:
          K -= 1
  # robot setting
  if steps[0] and not robot[0]:
    steps[0] -= 1
    if steps[0] == 0:
      K -= 1
    robot[0] = True
print(result)