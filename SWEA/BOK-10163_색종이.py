white = [[0]*101 for _ in range(101)]
N =int(input())
for n in range(N):
    a,b,c,d = map(int,input().split( ))
    for i in range(a,a+c):
        for j in range(b,b+d):
            white[i][j] = n+1
for n in range(N):
    tmp =0
    for i in range(101):
        for j in range(101):
            if white[i][j] == n+1:
                tmp += 1
    print(tmp)