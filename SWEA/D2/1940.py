for i in range(int(input())):
    speed = 0
    meter = 0
    for j in range(int(input())):
        a = list(map(int,input().split( )))
        if a[0] == 1:
            speed += a[1]
            meter += speed
        elif a[0] == 2:
            speed -= a[1] if speed > a[1] else speed
            meter += speed
        else:
            meter += speed
    print(f'#{i+1} {meter}')