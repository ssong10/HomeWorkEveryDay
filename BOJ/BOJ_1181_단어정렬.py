import sys
i = sys.stdin.readline
arr = {i().strip() for _ in range(int(i()))}
for a in sorted(arr,key=lambda x:[len(x),x]):
  print(a)