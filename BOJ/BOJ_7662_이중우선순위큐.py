from heapq import heappush,heappop
import sys
input = sys.stdin.readline

def pop(hq):
  global check
  while hq:
    n,idx = heappop(hq)
    if not check[idx]:
      check[idx] = True
      return n

for _ in range(int(input())):
  N = int(input())
  max_heap = [] # 큰거 빼는거
  min_heap = [] # 작은거
  check = [False] * N
  cnt = 0
  for i in range(N):
    t, num = input().split()
    num = int(num)
    if t == 'I':
      cnt += 1
      heappush(max_heap,(-num,i))
      heappush(min_heap,(num,i))
    else: # D
      if num > 0: # 큰거빼자
        pop(max_heap)
      else:
        pop(min_heap)
  if sum(check) == cnt:
    print('EMPTY')
  elif sum(check) == cnt - 1:
    a = pop(min_heap)
    print(a,a)
  else:
    print(-pop(max_heap),pop(min_heap))