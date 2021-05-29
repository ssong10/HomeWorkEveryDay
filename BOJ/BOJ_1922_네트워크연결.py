N = int(input())
M = int(input())
answer = 0
budgets = [list(map(int,input().split())) for _ in range(M)]
budgets.sort(key=lambda x:x[2],reverse=True)
parents = [i for i in range(N)]
def find(a):
  if parents[a]==a:
    return a
  parents[a] = find(parents[a])
  return parents[a]

def union(a,b):
  p1 = find(a)
  p2 = find(b)
  if p1!= p2:
    parents[p1] = p2

cnt = 1
while cnt < N:
  a,b,c=budgets.pop()
  a -= 1
  b -= 1
  if find(a) != find(b):
    union(a,b)
    cnt += 1
    answer += c
print(answer)
