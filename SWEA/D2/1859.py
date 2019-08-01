for i in range(int(input())):
    j = int(input())
    a = list(map(int,input().split( )))
    n=0
    m = a[j-1]
    for k in range(j-2,-1,-1):
        if a[k] > m:
            m = a[k]
        else:
            n += m-a[k]
    print(f'#{i+1} {n}')