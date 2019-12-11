for T in range(int(input())):
    N = int(input())
    f = [1,1,1]
    for _ in range(3,N):
        f.append(f[-2]+f[-3])
    print(f[-1])