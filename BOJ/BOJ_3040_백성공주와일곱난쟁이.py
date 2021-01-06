numlist = []
total = -100

def find(numlist,total):
  for i in range(8):
    for j in range(i+1,9):
      if numlist[i]+numlist[j] == total:
        return (i,j)


for _ in range(9):
  number = int(input())
  total += number
  numlist.append(number)

i,j = find(numlist,total)  
for k in range(9):
  if k != i and k != j:
    print(numlist[k])
