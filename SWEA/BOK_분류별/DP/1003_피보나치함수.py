for tc in range(int(input())):
    N = int(input())
    f = []
    f.append([1,0])
    if N > 0:
        f.append([0,1])
        for i in range(2,N+1):
            f.append(list(map(sum,f[-2:])))
    print(*f[-1])
