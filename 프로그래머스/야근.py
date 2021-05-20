def solution(n, works):
    answer = 0
    MAX = max(works)
    count = [0] * (MAX + 1)
    for work in works:
        count[work] += 1
    flag = MAX
    for i in range(MAX,0,-1):
        if n <= 0:
            break
        if count[i]:
            if count[i] > n:
                tmp = n
            else:
                tmp = count[i]
                MAX -= 1
            count[i] -= tmp
            count[i-1] += tmp
            n -= tmp
    for j in range(1,MAX+1):
        answer += count[j]*(j ** 2)
    return answer