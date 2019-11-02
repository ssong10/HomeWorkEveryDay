for tc in range(int(input())):
    a = ['Alice','Bob']
    N = int(input())+1
    n = 1
    while N //2 != 1:
        N = N//2
        print(N)
        n += 1
    print('#{} {}'.format(tc+1,n, a[n%2]))
