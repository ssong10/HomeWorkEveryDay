arr = []
for i in range(8):
  arr.append([int(input()),i+1])
t = sorted(arr)[-5:]
print(sum(map(lambda x:x[0],t)))
print(*sorted(map(lambda x:x[1],t)))