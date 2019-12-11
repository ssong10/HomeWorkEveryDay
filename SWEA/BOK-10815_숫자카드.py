def search(arr, num): # num 이 arr에 있는지
    min = 0
    max = len(arr)-1
    while max >=  min:
        mid = (min+max)//2
        if num > arr[mid]:
            min = mid+1
        elif num < arr[mid]:
            max = mid-1
        else:
            return '1'       
    return '0' 
result = []
a = int(input())
a_card = sorted(list(map(int, input().split(' '))))
b = int(input())
b_card = list(map(int, input().split(' ')))
for i in b_card:
    result.append(search(a_card,i))
print(' '.join(result))