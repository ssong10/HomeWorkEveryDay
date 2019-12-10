N = int(input())
dp = [0,1,1,1,1,1,1,1,1,1]
for _ in range(N-1):
    tmpdp = [0]*10
    for i in range(10):
        tmp = 0
        if -1 < i-1:
            tmp += dp[i-1]
        if i+1 < 10:
            tmp += dp[i+1]
        tmpdp[i] = tmp
    dp = tmpdp
print(sum(dp)%1000000000)
