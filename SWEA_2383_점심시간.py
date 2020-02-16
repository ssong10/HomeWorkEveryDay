def selectstair(n,tmp,tmp1):
    global result
    if n == len(pp):
        a = time(tmp,stairs[0])
        if result > a:
            b = time(tmp1,stairs[1])
            result = min(result,max(a,b))
    else:
        selectstair(n+1,tmp+[pp[n]],tmp1)
        selectstair(n+1,tmp,tmp1+[pp[n]])

def time(tmp,stair):
    y,x = stair
    times = []
    for i in tmp:
        times.append(abs(y-i[0])+abs(x-i[1]))
    times.sort()
    l = arr[y][x]
    for idx in range(len(times)):
        if idx < 3:
            times[idx] += l
        else:
            if times[idx - 3] > times[idx]:
                times[idx] = times[idx - 3] + l
            else:
                times[idx] += l
    if times:
        return times[-1]
    else:
        return 0

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    pp,stairs = [] , []
    result = 10 ** 6
    for y in range(N):
        for x in range(N):
            if arr[y][x]:
                if arr[y][x] == 1:
                    pp.append([y,x])
                else:
                    stairs.append([y,x])
    selectstair(0,[],[])
    print(f'#{tc+1} {result}')