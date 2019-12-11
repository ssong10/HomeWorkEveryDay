def find(sdk,n):
    global result,chk
    if not result:
        if n == N:
            for s in sdk:
                print(*s)
            result += 1
        else:
            y,x = zero[n][0],zero[n][1]
            tmp = []
            for yy in range(9):
                for xx in range(9):
                    if yy==y or xx==x:
                        if sdk[yy][xx] not in tmp:
                            tmp.append(sdk[yy][xx])
            for yy in range(y//3*3,y//3*3+3):
                for xx in range(x//3*3,x//3*3+3):
                    if sdk[yy][xx] not in tmp:
                        tmp.append(sdk[yy][xx])
            for num in chk:
                if num not in tmp:
                    sdk[y][x] = num
                    find(sdk,n+1)
                    sdk[y][x] = 0

sdk = [list(map(int,input().split())) for _ in range(9)]
N , zero = 0 , []
for y in range(9):
    for x in range(9):
        if not sdk[y][x]:
            zero.append([y,x])
            N += 1
chk = [1,2,3,4,5,6,7,8,9]
result = 0
find(sdk,0)