def quick(arr):
    a = len(arr)
    if a <= 1:
        return arr
    mid = arr[a//2]
    left,right = [],[]
    for i in range(a):
        if i != a//2:
            if arr[i] < mid:
                left.append(arr[i])
            else:
                right.append(arr[i])
    left = quick(left)
    right = quick(right)
    left = left + [mid] +right
    return left

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int,input().split()))
    quicklist = quick(arr)
    print('#{} {}'.format(tc+1,quicklist[N//2]))
