def solution(citations):
    answer = 0
    for i in range(max(citations)):
        index = [0,0]
        for citation in citations:
            if citation >= i:
                index[0] += 1
            else:
                index[1] += 1
        if index[0] >= i and index[1] <=i:
            answer = i
        else:
            break
    return answer