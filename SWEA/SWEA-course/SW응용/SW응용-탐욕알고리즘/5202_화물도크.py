T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    times = []
    for _ in range(N):
        s, e = map(int, input().split())
        times.append((e, s))
    times.sort()
    te, ts = times[0][0], times[0][1]
    cnt = 1
    for i in range(1, N):
        if te <= times[i][1]:
            te, ts = times[i][0], times[i][1]
            cnt += 1
    print('#{}'.format(tc), cnt)