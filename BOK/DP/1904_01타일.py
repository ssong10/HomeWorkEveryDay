N = int(input())
resultprv = 1
result = 1
for i in range(2,N+1):
    result,resultprv = (resultprv+result)%15746,result%15746
print(result)