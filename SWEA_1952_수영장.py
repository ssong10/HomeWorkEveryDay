for tc in range(int(input())):
    d, m ,mm, y = map(int,input().split())
    days = list(map(int,input().split()))
    pay = [[0]*12 for _ in range(2)]
    for i in range(12):
        pay[0][i] = min(d * days[i],m)
        pay[1][i] = min(pay[0][i] + pay[1][i-1],pay[1][i-3]+mm)
    print(f'#{tc+1} {min(pay[1][11],y)}')