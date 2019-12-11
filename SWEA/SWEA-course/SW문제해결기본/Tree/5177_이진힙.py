def push(item):
    global top
    top += 1
    H[top] = item
    c, p = top,top//2
    while p:
        if H[p] > H[c]:
            H[p],H[c] = H[c],H[p]
            c = p
            p = c//2
        else:
            break

for tc in range(int(input())):
    N = int(input())
    H = [0] * (N+1)
    top = 0
    arr = list(map(int,input().split()))
    for i in arr:
        push(i)
    result = 0
    while N!= 1:
        result += H[N//2]
        N = N//2
    print('#{} {}'.format(tc+1,result))