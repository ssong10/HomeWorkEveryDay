prev, curr = 1,1
for i in range(int(input())-1):
  prev,curr = curr, (prev+curr)%10007
print(curr)