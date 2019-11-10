def solution(prices):
    N = len(prices)
    result = []
    for i in range(N):
        tmp = 0
        for j in range(i+1,N):
            tmp += 1
            if prices[j] < prices[i]:
                break
        result.append(tmp)
    return result