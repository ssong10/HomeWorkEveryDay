for tc in range(int(input())):
    N, K = map(int,input().split())
    arr = input()
    a = set()
    for i in range(N//4):
        for k in range(0,N,N//4):
            a.add(arr[k:k+N//4])
        arr = arr[-1] + arr[:-1]
    numlist = []
    for h in a:
        numlist.append(int(h,16))
    print(f'#{tc+1} {sorted(numlist,reverse=True)[K-1]}')