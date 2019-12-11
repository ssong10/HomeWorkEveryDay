for tc in range(int(input())):
    n, m= map(int,input().split( ))
    long = list(map(int,input().split( )))
    mx,mn = 0,100
    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum += long[i+j]
        if i == 0:
            mx,mn = sum,sum
        else:
            mx = sum if sum > mx else mx
            mn = sum if sum < mn else mn
    print(f'#{tc+1} {mx-mn}')