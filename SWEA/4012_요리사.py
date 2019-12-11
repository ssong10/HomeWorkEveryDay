for tc in range(int(input())):
    N = int(input())
    result =[]
    food =[]
    for i in range(N):
        food.append(list(map(int,input().split( ))))
    cook =[]
    for i in range(N):
        cook.append(i+1)
    a = len(cook)
    for i in range((1<<a)//2):
        tmp = []
        tmp1 =[]
        for j in range(a):
            if i&(1<<j):
                tmp.append(cook[j])
            else:
                tmp1.append(cook[j])
        if len(tmp) == N//2:
            S = 0
            for i in tmp:
                for j in tmp:
                    if i != j:
                        S += food[i-1][j-1]
            for i in tmp1:
                for j in tmp1:
                    if i != j:
                        S -= food[i-1][j-1]
            result.append(abs(S))
    print(f'#{tc+1} {min(result)}')