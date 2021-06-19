print(p)
import sys
input = sys.stdin.readline
def check(i):
  for n_i in members[i]:
    if not visit[n_i-1]:
      visit[n_i-1] = True
      check(n_i)
N, M = map(int,input().split())
trues = list(map(int,input().split()))
members = dict(list([x+1,set()] for x in range(N)))
orders = [list(map(int,input().split()))[1:] for _ in range(M)]
for order in orders:
  for i in range(len(order)):
    for j in range(len(order)):
      if i != j:
        members[order[i]].add(order[j])
        members[order[j]].add(order[i])
visit = [False] * N
for i in trues[1:]:
  visit[i-1] = True
  check(i)
  
answer = 0
for order in orders:
  for o in order:
    if visit[o-1]:
      break
  else:
    answer += 1
print(answer)