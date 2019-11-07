def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1
    for y in range(n):
        for x in range(m):
            if not dp[y][x]: 
                if -1<y-1<n and dp[y-1][x] != -1:
                    dp[y][x] += dp[y-1][x]
                if -1<x-1<m and dp[y][x-1] != -1:
                    dp[y][x] += dp[y][x-1]
    return dp[n-1][-1]%1000000007