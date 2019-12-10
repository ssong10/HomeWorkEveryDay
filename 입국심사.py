def back(wait,M,S):
    print(wait,M,S)
    if 0 >= M:
        print(S)
    else:
        S += 1
        for i in range(N):
            if not wait[i] % desk[i]:
                wait[i] -= desk[i]
            else:
                wait[i] += 1
            if not wait[i]:
                wait[i] += 1
                M -= 1
    back(wait,M,S)


for tc in range(int(input())):
    N,M = map(int,input().split())
    desk = [int(input()) for _ in range(N)]
    S = 0 
    wait = [0] * N
    back(wait,M,S)