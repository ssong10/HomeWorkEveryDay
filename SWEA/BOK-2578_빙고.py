def bingos(arr):
    count = 0
    for i in arr:
        if sum(i) == 0:
            count += 1
    for j in range(5):
        tmp1 = 0
        for k in range(5):
            tmp1 += arr[k][j]
        if tmp1 == 0:
            count +=1
    tmp2,tmp3 = 0,0
    for i in range(5):
        tmp2 += arr[i][i]
        tmp3 += arr[i][4-i]
    if tmp2 == 0:
        count +=1
    if tmp3 == 0:
        count +=1
    return count

arr = [list(map(int,input().split( ))) for _ in range(5)]
bingo1 = [list(map(int,input().split( ))) for _ in range(5)]
bingo2 = []
result = 0
for i in range(5):
    for j in range(5):
        bingo2.append(bingo1[i][j])

for k in bingo2:
    result += 1
    for i in range(5):
        for j in range(5):
            if arr[i][j] == k:
                arr[i][j] = 0
    if bingos(arr) >2:
        print(result)
        break