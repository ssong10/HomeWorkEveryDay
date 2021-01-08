def find(s):
  tmp = [s]
  flag = False
  result = 0
  while tmp:
    print(tmp)
    result += 1
    for _ in range(len(tmp)):
      t = tmp.pop(0)
      visit[t] = True
      for i in V[t]:
        if i == e-1:
          return result
        if not visit[i]:
          tmp.append(i)
  return -1
n = int(input())
s,e = map(int,input().split())
m = int(input())
V = [[] for _ in range(n)]

visit = [False] * n
for _ in range(m):
  v,w = map(int,input().split())
  V[v-1].append(w-1)
  V[w-1].append(v-1)

print(find(s-1))