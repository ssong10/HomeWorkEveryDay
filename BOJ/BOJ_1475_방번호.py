N = input()
arr = [0] * 10
for s in N:
  arr[int(s)] += 1
arr[6] = (arr[6]+arr[9]+1)//2
print(max(arr[:9]))