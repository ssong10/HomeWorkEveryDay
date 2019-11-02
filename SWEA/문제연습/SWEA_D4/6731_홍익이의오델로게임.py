for tc in range(int(input())):
    N = int(input())
    arr = list(input() for _ in range(N))
    result = 0
    for y in range(N):
        for x in range(N):
            t = 0
            for yy in range(N):
                for xx in range(N):
                    if (yy==y or xx==x) and arr[yy][xx] == 'B':
                        t += 1
            if t % 2:
                result += 1
    print(f'#{tc+1} {result}')