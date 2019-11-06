def solution(triangle):
    for h in range(1,len(triangle)):
        for i in range(len(triangle[h])):
            tmp =[]
            if -1 < i <len(triangle[h-1]):
                tmp.append(triangle[h-1][i])
            if -1 < i-1 < len(triangle[h-1]):
                tmp.append(triangle[h-1][i-1])
            triangle[h][i] += max(tmp)
    return max(triangle[-1])
