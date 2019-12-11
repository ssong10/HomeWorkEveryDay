def inorder(v):
    global result
    if v == 0:
        return
    inorder(L[v])
    result += S[v]
    inorder(R[v])


for tc in range(1, 11):
    N = int(input())
    result = ''
    L, R, S = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)
    for _ in range(N):
        tmp = input().split()
        p = int(tmp[0])
        if len(tmp) == 4:
            L[p] = int(tmp[2])
            R[p] = int(tmp[3])
        elif len(tmp) == 3:
            L[p] = int(tmp[2])
        S[p] = tmp[1]
    inorder(1)
    print('#{}'.format(tc), result)