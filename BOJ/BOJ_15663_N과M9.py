def back(tmp):
  if len(tmp) == M and tuple(tmp) not in prev:
    prev.add(tuple(tmp))
    print(*tmp)
    return
  for i in range(N):
    if not visit[i]:
      visit[i] = True
      back(tmp+[arr[i]])
      visit[i] = False

N , M = map(int,input().split())
arr = sorted(map(int,input().split()))
visit = [False] * N
prev = set()
back([])

# --------------- #
def back(tmp):
  if len(tmp) == M:
    print(*tmp)
    return
  prev = -1
  for i in range(N):
    if prev != arr[i] and not visit[i]:
      prev = arr[i]
      visit[i] = True
      back(tmp+[arr[i]])
      visit[i] = False

N , M = map(int,input().split())
arr = sorted(map(int,input().split()))
visit = [False] * N
back([])