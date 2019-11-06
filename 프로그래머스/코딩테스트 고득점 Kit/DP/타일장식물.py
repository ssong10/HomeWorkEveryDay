def solution(N):
    answer = [1,1]
    if N >=2:
        for i in range(2,N+1):
            answer.append(answer[i-1]+answer[i-2])
    return 2*sum(answer[-2:])