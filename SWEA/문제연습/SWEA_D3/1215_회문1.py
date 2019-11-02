for tc in range(1,11):
    N = int(input())
    arr = list(input() for _ in range(8))
    result = 0
    for y in range(8):
        for x in range(8):
            if x+N < 9:
                if arr[y][x:x+N] == arr[y][x:x+N][::-1]:
                    result += 1
            if y+N < 9:
                pal = ''
                for i in range(N):
                    pal += arr[y+i][x]
                if pal == pal[::-1]:
                    result += 1
    print('#{} {}'.format(tc,result))