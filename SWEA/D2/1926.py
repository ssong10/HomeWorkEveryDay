result = []
for i in range(1,int(input())+1):
    clap = 0
    for j in str(i):
        if int(j) in [3,6,9]:
        	clap +=1
    if clap > 0:
        result.append('-' * clap)
    else:
        result.append(str(i))
print(' '.join(result))