def go(v):
    global result
    if v == 99:
        result = 1
        return
    for i in node[v]:
        go(i)

for _ in range(10):
    node = [[] for _ in range(100)]
    result = 0
    tc, N = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(N):
        node[arr[i*2]].append(arr[(i*2)+1])
    go(0)
    print(f'#{tc} {result}')