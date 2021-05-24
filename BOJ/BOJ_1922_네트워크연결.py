# a = [
#   [1,2],
#   [3,4]
# ]
# def solution(a):
#   answer = 0
#   def MIN(y,x,a):
#     if y+x == 4:
#       return 
#         tmp += a[i][j]
#     return tmp
#   answer = MIN(0,0,a)

# solution(a)
# solution([[1,2],[5,6]])



N = int(input())
M = int(input())
answer = 0
budgets = [list(map(int,input().split())) for _ in range(M)]
budgets.sort(key=lambda x:x[2])
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

for i in range(len(budgets)):
  a,b,c=budgets[i]
  a -= 1
  b -= 1
  if find(a) != find(b):
    union(a,b)
    answer += c
print(answer)
