a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
answer = input()
for i in a:
  answer = answer.replace(i,'.')
print(len(answer))