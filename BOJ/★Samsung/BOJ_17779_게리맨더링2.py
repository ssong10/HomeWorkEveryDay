N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
print(arr)
for x in range(N):
    for y in range(N):
        if x+y < 3 and y-x < 2:
            arr[y][x] = 1
        elif x+y < 3 and x- y < 2:
            arr[y][x] = 2
        elif x+y > 5 and y-x < 2:
            arr[y][x] = 4
        elif x+y > 5 and x-y < 2:
            arr[y][x] = 3
        else:
            arr[y][x] = 5
for a in arr:
    print(a)