from collections import deque
def DFS(q):
  answer = 1
  while q:
    for _ in range(len(q)):
      f = q.popleft()
      for n_f in [f+U,f-D]:
        if -1 < n_f < F and not visited[n_f]:
          visited[n_f] = True
          q.append(n_f)
          if n_f == G-1:
            return answer
    answer += 1
  return 'use the stairs'

F, S, G, U, D = map(int,input().split())

visited = [False] * F
visited[S-1] = True
if S == G:
  print(0)
else:
  answer = DFS(deque([S-1]))
  print(answer)
