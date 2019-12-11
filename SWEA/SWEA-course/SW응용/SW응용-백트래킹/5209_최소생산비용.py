def pick(choice, n):
    global result
    if n == N:
        result = min(result,choice)
    elif choice <= result:
        for i in range(N):
            if not used[i]:
                used[i] = 1
                pick(choice + arr[n][i], n + 1)
                used[i] = 0


for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    result = 10 ** 6
    pick(0, 0)
    print('#{} {}'.format(tc+1,result))