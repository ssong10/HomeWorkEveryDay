for tc in range(int(input())):
    prices = list(map(int,input().split()))
    months = list(map(int,input().split()))
    day = [0]+ months
    dp = [0] * 12
    dp1 = [0]*13
    for i in range(12):
        tmp = min(prices[0]*months[i], prices[1])
        dp[i] = min(tmp+dp[i-1],prices[2] +dp[i-3])
    print('#{} {}'.format(tc+1,min(prices[3],dp[-1])))
