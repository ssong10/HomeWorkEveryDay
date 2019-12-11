for tc in range(int(input())):
    N = int(input())
    prbs = list(map(int,input().split()))
    result = [1]+ [0] * (sum(prbs))
    for prb in prbs:
        tmp = [prb]
        for i in range(sum(prbs)):
            if result[i] and not result[prb+i]:
                tmp.append(prb+i)
        for j in tmp:
            result[j] = 1
    print('#{} {}'.format(tc+1,sum(result)))