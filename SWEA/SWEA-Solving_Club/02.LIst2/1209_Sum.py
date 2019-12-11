for tc in range(1,11):
    a = input()
    arr =[]
    for _ in range(100):
        arr.append(list(map(int,input().split( ))))
    result =[]
    for i in arr:
        result.append(sum(i))
    for j in range(100):
        tmp = 0
        for k in range(100):
            tmp += arr[k][j]
        result.append(tmp)
    tmp1 = 0
    tmp2 = 0
    for i in range(100):
        tmp1 += arr[i][i]
        tmp2 += arr[i][99-i]
    result.append(tmp1)
    result.append(tmp2)
    print(f'#{tc} {max(result)}')