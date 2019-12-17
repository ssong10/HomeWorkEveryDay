N = int(input())
for i in range(max(0,N-len(str(N))*9),N):
    result = i + sum(map(lambda x:int(x),str(i)))
    if result == N :
        print(i)
        break
else:
    print(0)