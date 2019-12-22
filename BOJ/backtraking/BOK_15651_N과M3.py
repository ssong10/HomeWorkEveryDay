def back(n):
    if n == M:
        print(*result)
    else:
        for i in range(1, N + 1):
            result.append(i)
            back(n + 1)
            result.pop()


N, M = map(int, input().split())
result = []
back(0)