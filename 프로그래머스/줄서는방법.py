def solution(n, k):
    num = [False] * n
    answer = []
    tmp = 1
    k -= 1
    for i in range(1,n):
        tmp *= i
    for i in range(n-1,0,-1):
        cnt = k // tmp
        k -= cnt * tmp
        m = 0
        for j in range(n):
            if not num[j]:
                if m == cnt:
                    answer.append(j+1)
                    num[j] = True
                    break
                m += 1
        tmp /= i
    for i in range(n):
        if not num[i]:
            answer.append(i+1)
            break
    return answer

solution(3,5)