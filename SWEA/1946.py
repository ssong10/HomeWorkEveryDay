for i in range(int(input())):
    print(f'#{i+1}')
    num = 0
    for j in range(int(input())):
        a,b = input().split( )
        for k in range(int(b)):
            print(a, end='')
            num += 1
            if num % 10 == 0:
                print('')
    print('')