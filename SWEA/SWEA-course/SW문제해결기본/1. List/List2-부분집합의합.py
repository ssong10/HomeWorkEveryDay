for tc in range(int(input())):
    result = 0
    arr= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    a = len(arr)
    n,k = map(int,input().split( ))
    for i in range(1<<a):
        tmp = []
        for j in range(a):
            if i&(1<<j):
                tmp.append(arr[j])
        if len(tmp) == n and sum(tmp) == k:
            result +=1
    print(f'#{tc+1} {result}')