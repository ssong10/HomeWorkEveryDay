N = int(input())
arr = list(map(int,input().split()))

MIN, MAX = arr[0], arr[0]
for i in range(N):
  if arr[i] < MIN:
    MIN = arr[i]
  if arr[i] > MAX:
    MAX = arr[i]
print(MIN, MAX)