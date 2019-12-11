for tc in range(int(input())):
    N,M = map(int,input().split())
    weights = sorted(list(map(int,input().split())))
    trucks = sorted(list(map(int,input().split())))
    result = 0
    while trucks and weights:
            weight = weights.pop()
            if weight <= trucks[-1]:
                trucks.pop()
                result += weight
    print('#{} {}'.format(tc+1,result))