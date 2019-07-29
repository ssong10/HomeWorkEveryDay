for i in range(int(input())):
    a,b,c,d = map(int,input().split( ))
    if a+c > 12:
        hh= a+c -12
    else:
        hh = a+c
    if b+d >=60:
        mm = b+d - 60 
        hh += 1
    else:
        mm = b+d
    print(f'#{i+1} {hh} {mm}')