def func(arr):
    for num in reversed(sorted(arr)):
        tmp = num
        d = len(str(num))
        for i in range(d-1):
            if str(num)[i] > str(num)[i+1]:
                tmp = 0
                break
        if tmp > 0:
            return num
    return -1

for tc in range(int(input())):
    a = int(input())
    numlist = list(map(int,input().split( )))
    arr = []
    for i in range(a):
        for j in range(i):
            arr.append(numlist[i] * numlist[j])
    print(f'#{tc+1} {func(arr)}')