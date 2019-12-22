n = int(input())
dp = []
tri = [list(map(int,input().split())) for _ in range(n)]
dp.append(tri[0])
for i in range(1,n):
    tmp = []
    for j in range(i+1):
        if not j:
            tmp.append(dp[i-1][j] + tri[i][j])
        elif j == i:
            tmp.append(dp[i-1][j-1]+tri[i][j])
        else:
            tmp.append(max(dp[i-1][j]+tri[i][j], dp[i-1][j-1]+tri[i][j]))
    dp.append(tmp)
print(max(dp[-1]))