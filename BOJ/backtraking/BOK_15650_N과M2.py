def back(choice):
    if len(choice) == M:
        print(*choice)
    else:
        for i in range(1,N+1):
            if not used[i-1] and (not choice or choice[-1] < i):
                used[i-1] = 1
                choice.append(i)
                back(choice)
                used[i-1] =0
                choice.pop()
N,M = map(int,input().split())
used = [0] * N
back([])