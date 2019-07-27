for i in range(int(input())):
    ms, n = map(int,input().split( ))  # 10, 2
    result = []
    g = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for m in range(ms):
        a,b,c = map(int,input().split( ))
        sum = 0.35 *a + 0.45 *b + 0.2 * c
        result.append(sum)
        if n == m+1:
            d = sum
    e = int((ms- sorted(result).index(d))*10 /ms - 10e-5)
    print(f'#{i+1} {g[e]}')