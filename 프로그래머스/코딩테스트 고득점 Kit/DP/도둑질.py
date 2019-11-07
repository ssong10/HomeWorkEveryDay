def solution(money):
    dp=[[0] * len(money) for _ in range(3)]
    dp[0][0],dp[1][1] = money[0], money[1]
    for i in range(2,len(money)):
        if dp[0][i-1]:
            if dp[1][i-2] + money[i] > dp[0][i-1]:
                dp[2][i] = dp[1][i-2] + money[i]
            else:
                dp[2][i] = dp[0][i-1]
            dp[1][i] = dp[2][i]
            
        else:
            if dp[0][i-2] + money[i] > dp[1][i-1]:
                dp[2][i] = dp[0][i-2]+ money[i]
            else:
                dp[2][i] = dp[1][i-1]
            dp[0][i] = dp[2][i]
    return dp[2][-1]