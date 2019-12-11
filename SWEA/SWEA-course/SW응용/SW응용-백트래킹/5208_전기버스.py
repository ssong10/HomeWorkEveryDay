def charge(station,n,cnt):
    global result
    if N <= station+n:
        result = min(cnt,result)
    else:
        tmp = 0
        find = 0
        for i in range(station+1,station+n+1):
            if tmp <= i+stations[i]:
                tmp = i+stations[i]
                find = i
        charge(find,stations[find],cnt+1)

for tc in range(int(input())):
    stations = list(map(int,input().split()))
    N = stations[0]
    result = 10**5
    energy = [0] * N
    charge(1,stations[1],0)
    print('#{} {}'.format(tc+1,result))