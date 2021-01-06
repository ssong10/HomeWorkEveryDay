N = int(input())
numlist = set(map(int,input().split()))
M = int(input())
checklist = list(map(int,input().split()))

for num in checklist:
  if num in numlist:
    print(1)
  else:
    print(0)