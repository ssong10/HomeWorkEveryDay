def binary(lo, hi):
    global answer
    mid = (lo + hi) >> 1
    if lo > hi:
        return
    if A[mid] == num:
        answer += 1
        return
    if A[mid] < num:
        binary(mid+1, hi)
    else:
        binary(lo, mid-1)

t = int(input())
for tc in range(1, t + 1):
    answer = 0
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for num in B:
        binary(0, n-1)
    print('#{} {}'.format(tc, answer))