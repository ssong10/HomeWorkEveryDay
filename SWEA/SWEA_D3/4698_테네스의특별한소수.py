numlist = [1, 1] + [0] * (10**6 - 1)
for i in range(2, int((10**6 + 1) ** 0.5) + 1):
    if not numlist[i]:
        for num in range(2 * i, 10**6 + 1, i):
            numlist[num] = 1

for tc in range(int(input())):
    D,A,B = map(int,input().split())
    result = 0
    for i in range(A,B+1):
        if not numlist[i] and str(D) in list(str(i)):
            result += 1
    print(f'#{tc+1} {result}')