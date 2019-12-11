def make(y,x,num):
    if len(num) == 7:
        numbers.add(num)
    else:
        for d in range(4):
            yy,xx = y+dy[d], x+dx[d]
            if -1< yy < 4 and -1 < xx < 4:
                make(yy,xx,num+arr[yy][xx])

for tc in range(int(input())):
    arr = [list(input().split()) for _ in range(4)]
    dy,dx = [-1,1,0,0],[0,0,1,-1]
    numbers = set()
    for y in range(4):
        for x in range(4):
            make(y,x,arr[y][x])
    print('#{} {}'.format(tc+1,len(numbers)))