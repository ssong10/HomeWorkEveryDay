d = [0,1]
for i in range(2,int(input())+1):
  d.append(d[-1]+d[-2])
print(d[-1])