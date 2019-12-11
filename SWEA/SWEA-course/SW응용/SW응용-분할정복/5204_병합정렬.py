def merge_sort(arr):
    global answer
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    if left[-1] > right[-1]:
        answer += 1
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    if i != len(left):
        result.extend(left[i:])
    else:
        result.extend(right[j:])
    return result

for tc in range(int(input())):
    N = int(input())
    L = list(map(int,input().split()))
    answer = 0
    a = merge_sort(L)[N//2]
    print('#{} {} {}'.format(tc+1,a,answer))
