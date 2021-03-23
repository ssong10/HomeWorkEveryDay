result_total = 0
result = []
for tc in range(int(input())):
  N = int(input())
  arr = list(map(int,input().split()))
  answer = [arr[0],0,0]
  tmp = [arr[0],0,0]
  for i in range(N):
    if arr[i] + 