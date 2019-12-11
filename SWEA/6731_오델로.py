for tc in range(int(input())):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 0
    for y in range(N):
        for x in range(N):
            tmp = 0
            for yy in range(N):
                for xx in range(N):
                    if y==yy or x ==xx and (y,x) != (yy,xx):
                        if arr[yy][xx] == 'B':
                            tmp += 1
            if tmp%2:
                result += 1
    print('#{} {}'.format(tc+1,result))