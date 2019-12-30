def divide(y,x,d_1,d_2):
    global result
    tmp = [0,0,0,0,0]
    for r in range(N):
        for c in range(N):
            if x+y <= r+c <= x+y+d_1+d_1 and x-y -d_2-d_2 <= c-r <= x-y:
                tmp[4] += arr[r][c]
            elif -1 < r < y+d_2 and -1 < c <= x:
                tmp[0] += arr[r][c]
            elif -1 < r <= y+d_1 and x < c <= N:
                tmp[1] += arr[r][c]
            elif y+d_2 <= r <= N and -1 < c < x-d_2+d_1:
                tmp[2] += arr[r][c]
            elif y+d_1 < r <= N and x- d_2 + d_1 <= c <= N:
                tmp[3] += arr[r][c]
    result = min(result,max(tmp)-min(tmp))

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 10 ** 6
for a in range(2,N):
    for b in range(1,a):
        for y in range(N-a):
            for x in range(a-b,N-b):
                divide(y,x,b,a-b)

print(result)